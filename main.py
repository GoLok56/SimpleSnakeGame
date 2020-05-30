import sys
import pygame
import variables

from snake import Snake
from window import Window

pygame.init()

def main():
  window = Window(Snake(2, 1), title='Snake Game')
  while variables.run:
    window.check_for_collision()
    window.check_for_event()
    window.draw()
    pygame.display.update()

  sys.exit()
  pygame.quit()

if __name__ == "__main__":
  main()