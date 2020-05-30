import pygame

from constant import GRID_SIZE
from gameobject import GameObject

FRUIT_SPACING = 5

class Fruit(GameObject):
  def __init__(self, x, y, on_collided=None):
    super().__init__(x, y, on_collided)
    self.size = GRID_SIZE - (2 * FRUIT_SPACING)

  def get_starting_point(self, position):
    return position * GRID_SIZE + FRUIT_SPACING

  def draw(self, screen):
    x = self.get_starting_point(self.x)
    y = self.get_starting_point(self.y)
    pygame.draw.rect(screen, (0, 156, 0), (x, y, self.size, self.size))
