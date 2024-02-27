import pygame
from pygame.constants import KEYDOWN, KEYUP
#from Bunny import Bunny

pygame.init()

screen = pygame.display.set_mode([500, 250])
pygame.display.set_caption('Bunny Break')
color = (255, 255, 255)
screen.fill((color))
gameStart = False
#bunny = Bunny

pygame.display.flip()

running = True
while running:

  if pygame.key.get_pressed()[pygame.K_SPACE] and pygame.KEYDOWN:
    gameStart = True
    print('Game Starting')
    c2 = (0, 0, 0)
    pygame.draw.rect(screen, c2, pygame.Rect(60, 60, 60, 60))
    pygame.display.flip()

  elif pygame.key.get_pressed()[pygame.K_SPACE] and pygame.KEYUP:
    color = (255, 255, 255)
    screen.fill(color)
    pygame.display.flip()

  else:
    pass

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

pygame.quit()
