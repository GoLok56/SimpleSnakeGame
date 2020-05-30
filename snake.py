import pygame

from constant import *
from gameobject import GameObject

SNAKE_SPACING = 3

class Snake(GameObject):
  def __init__(self, x, y, on_collided=None):
    super().__init__(x, y, on_collided)
    self.radius = GRID_SIZE // 2 - SNAKE_SPACING
    self.direction = DIR_RIGHT
    self.tails = []
    self.tail_total = 0

  def draw_tail(self, screen):
    for tail in self.tails:
      x = self.get_center(tail[0])
      y = self.get_center(tail[1])
      pygame.draw.circle(screen, (0, 0, 156), (x, y), self.radius)

  def draw(self, screen):
    self.draw_tail(screen)
    x = self.get_center(self.x)
    y = self.get_center(self.y)
    pygame.draw.circle(screen, (156, 0, 0), (x, y), self.radius)

  def get_center(self, position):
    return position * GRID_SIZE + self.radius + SNAKE_SPACING

  def check_for_event(self, event):
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT and self.direction != DIR_RIGHT:
        self.direction = DIR_LEFT
      elif event.key == pygame.K_RIGHT and self.direction != DIR_LEFT:
        self.direction = DIR_RIGHT
      elif event.key == pygame.K_UP and self.direction != DIR_DOWN:
        self.direction = DIR_UP
      elif event.key == pygame.K_DOWN and self.direction != DIR_UP:
        self.direction = DIR_DOWN

  def move_tail(self):
    if self.should_add_tail():
      self.tails.append([self.x, self.y])
    elif self.should_shift_tail():
      self.shift_tails()

  def should_add_tail(self):
    return len(self.tails) != self.tail_total

  def should_shift_tail(self):
    return self.tail_total != 0

  def shift_tails(self):
    last_tail_position = len(self.tails) - 1
    for i in range(last_tail_position):
      self.tails[i] = self.tails[i + 1]
    self.tails[last_tail_position] = [self.x, self.y]

  def move_head(self, max_row, max_column):
    if self.direction == DIR_LEFT:
      self.x = max_column if self.x == 0 else self.x - 1
    elif self.direction == DIR_RIGHT:
      self.x = 0 if self.x == max_column else self.x + 1
    elif self.direction == DIR_UP:
      self.y = max_row if self.y == 0 else self.y - 1
    elif self.direction == DIR_DOWN:
      self.y = 0 if self.y == max_row else self.y + 1

  def move(self, max_row, max_column):
    self.move_tail()
    self.move_head(max_row, max_column)

  def eat(self):
    self.tail_total += 1

  def is_colliding(self, x, y):
    return x != self.x and y != self.y and [self.x, self.y] not in self.tails

  def is_dead(self):
    return [self.x, self.y] in self.tails
