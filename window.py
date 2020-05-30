import random
import pygame
import variables

from constant import DEFAULT_WIDTH, DEFAULT_HEIGHT, DEFAULT_FPS, GRID_SIZE
from fruit import Fruit
from snake import Snake

class Window:
  def __init__(self, snake, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, title='', fps=DEFAULT_FPS):
    self.width = width
    self.height = height
    self.max_row = height // GRID_SIZE - 1
    self.max_column = width // GRID_SIZE - 1
    self.fps = fps
    self.childs = [snake]
    self.snake = snake
    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode((self.width, self.height))
    self.snake.on_collided = lambda current_child, next_child: self.on_snake_collided(current_child, next_child)
    self.generate_food()
    pygame.display.flip()
    pygame.display.set_caption(title)

  def add(self, child):
    self.childs.append(child)

  def check_for_collision(self):
    num_of_child = len(self.childs)
    for i in range(num_of_child):
      current_child = self.childs[i]
      next_child_position = i + 1
      if num_of_child != next_child_position:
        for j in range(i + 1, num_of_child):
          next_child = self.childs[j]
          if current_child.x == next_child.x and current_child.y == next_child.y:
            if current_child.on_collided:
              current_child.on_collided(current_child, next_child)

  def check_for_event(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        variables.run = False
      else:
        for child in self.childs:
          child.check_for_event(event)

  def draw(self):
    pygame.time.delay(40)
    self.clock.tick(self.fps)
    self.screen.fill((0, 0, 0))
    if not self.snake.is_dead():
      for child in reversed(self.childs):
        child.move(self.max_row, self.max_column)
        child.draw(self.screen)

  def generate_food(self):
    while True:
      x = random.randint(0, self.max_column)
      y = random.randint(0, self.max_row)

      if self.snake.is_colliding(x, y):
        break

    self.add(Fruit(x, y))

  def on_snake_collided(self, current_child, next_child):
    if isinstance(current_child, Snake) and isinstance(next_child, Fruit):
      self.snake.eat()
      self.generate_food()
      self.childs.remove(next_child)

