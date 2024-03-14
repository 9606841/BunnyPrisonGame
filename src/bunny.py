#Emily Tan, Elisa Tandra

import pygame

pygame.init()
screen = pygame.display.set_mode([500, 250])

class Bunny:

  def __init__(self, x, y, pos, isWalking):
    self.x, self.y, self.pos = x, y, pos
    #walking boolean
    self.isWalking = False
    #self.img = pygame.image.load('bunny.png')
    #self.rect = self.img.get_rect()
    #self.rect.center = (self.x, self.y)

  #walking
  def walk(self, x, y):
    self.x, self.y = x, y
    if not self.isWalking:
      #insert idle animation
      pass
    else:
      #insert walking animation
      self.isWalking = True

  #movement: need arrow key detection

    def move(self, x, y, pos, speed):
      self.x, self.y, self.pos, self.speed = x, y, pos, speed
      if pygame.key.get_pressed()[pygame.K_LEFT]:
        pass

        # x -=1 ? need to move x, add speed, pos necessary?
        # include animations LATER

  #display bunny
  def bunDis(self, x, y):
    self.x = x
    self.y = y
    bunIdle = pygame.image.load('BunIdle.png')
    bunIdle = pygame.transform.scale(bunIdle, (200,200))
    screen.blit(bunIdle, (self.x, self.y))
    pygame.display.flip()
