import pygame
import numpy

class MemoryGame:
  xcard_stack = numpy.array((0,37,74, 111, 148, 0, 37,74, 111, 148, 0, 37,74, 111, 148))
  ycard_stack = numpy.array((0, 0, 0, 0, 0, 25, 25, 25, 25, 25, 75, 75, 75, 75, 75))
  def __init__(self, back, word, width, height, x, y):
    self.back = random(0,2)
    self.word = word
    self.width = 25
    self.height = 37
    self.x = x
    self.y = y

#loading image backs cards setup
def backDisplay(self):
  if self.back = 0:
    surface = pygame.display.set_mode(self.width,self.height)
    backImg = ('Card1.png')
    surface.blit(backImg, (self.width, self.height))
    pygame.display.flip
  elif self.back = 1:
    surface = pygame.display.set_mode(self.width,self.height)
    backImg = ('Card2.png')
    surface.blit(backImg, (self.width, self.height))
    pygame.display.flip
  elif self.back = 2:
    surface = pygame.display.set_mode(self.width,self.height)
    backImg = ('Card3.png')
    surface.blit(backImg, (self.width, self.height))
    pygame.display.flip
