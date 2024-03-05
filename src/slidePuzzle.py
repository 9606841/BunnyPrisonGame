import pygame
class slidePuzzle:
  def __init__(self, running):
    self.running = True
    def slidePuzzle():
      pygame.init()
      if pygame.key.get_pressed()[pygame.K_SPACE] and running:
       pygame.display.set_caption('Memory Game, click to continue')
      elif pygame.mouse.get_pressed()[0]:
        self.running = False
