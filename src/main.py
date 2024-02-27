import pygame
#from pygame.constants import KEYDOWN, KEYUP
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
  if pygame.key.get_pressed()[pygame.K_SPACE]:
    gameStart = True

  if gameStart == True:
    print('Game Starting')
    #c2 = (0, 0, 0)
    #pygame.display.flip()
    bg = pygame.image.load('PrisonBg.png')
    bg = pygame.transform.scale(bg, (500, 250))
    screen.blit(bg, (0, 0))
    pygame.display.flip()
    
    #instantiate bunny class & first minigame
  
  else:
    color = (255, 255, 255)
    screen.fill(color)
    pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

pygame.quit()
