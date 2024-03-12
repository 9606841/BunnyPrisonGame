import pygame
import random
import subprocess
subprocess.run(['pip', 'install', 'numpy'])
# import numpy still errors
import numpy
class MemoryGame:
  xcard_stack = numpy.array((0,37,74, 111, 148, 0, 37,74, 111, 148, 0, 37,74, 111, 148))
  ycard_stack = numpy.array((0, 0, 0, 0, 0, 25, 25, 25, 25, 25, 75, 75, 75, 75, 75))
  def __init__(self, back, word, width, height, x, y):
    self.back = random.randint(0,2)
    self.word = word
    self.width = 25
    self.height = 37
    self.x = x
    self.y = y

#loading image backs cards setup
def backDisplay(self):
  back = pygame.Surface((self.width, self.height))
  if self.back == 0:
    back = pygame.display.set_mode(self.width,self.height)
    backImg = pygame.image.load('Card1.png')
    back.blit(backImg, (self.width, self.height))
    pygame.display.flip
  elif self.back == 1:
    back = pygame.display.set_mode(self.width,self.height)
    backImg = pygame.image.load('Card2.png')
    back.blit(backImg, (self.width, self.height))
    pygame.display.flip
  elif self.back == 2:
    surface = pygame.display.set_mode(self.width,self.height)
    backImg = pygame.image.load('Card3.png')
    back.blit(backImg, (self.width, self.height))
    pygame.display.flip

def applyWords(self, word):
  front = pygame.Surface((self.width, self.height))
  display_surface = pygame.display.set_mode((self.x, self.y))
  pygame.display.set_caption('BunnyBreak')
  #insert font
  color = (23, 68, 69)
  font = pygame.font.SysFont('Arial', 30)
  text = font.render(self.word, True, color)
  textRect = text.get_rect()
  textRect.center= (self.x//2, self.y//2)
  while True:
    front.fill((255,255,255))
    front.blit(text, textRect)

def showCards(self):
  back.blit(front,0,0)
  screen.blit(back, (self.x,self.y))
  pygame.display.update()
