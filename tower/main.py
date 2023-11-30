import pygame as pg
#import constants as c
from .constants import *

def start_game():
  #initialise pygame
  pg.init()

  #create clock
  clock = pg.time.Clock()

  #create game window
  screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pg.display.set_caption("Tower Defense")

  #game loop
  run = True
  while run:

    clock.tick(FPS)

    #event handler
    for event in pg.event.get():
      #quit program
      if event.type == pg.QUIT:
        run = False

  pg.quit()

def main():
  start_game()
  
if __name__ == "__main__":
    main()