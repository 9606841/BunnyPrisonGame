# Elisa Tandra, Kate Patterson, David Valdespino, Emily Tan

from os import truncate
import pygame
from maze import Maze
from bunny import Bunny
#from memoryGame import MemoryGame (need to fix this? find error)


pygame.init()

screen = pygame.display.set_mode([500, 250])
pygame.display.set_caption('Bunny Break')
bg = pygame.image.load('PrisonBg.png')
bg = pygame.transform.scale(bg, (500, 250))
screen.blit(bg, (0, 0))
gameStart = False
bun = Bunny(250, 125, 0, False)
pygame.display.flip()

running = True
while running:
  if pygame.key.get_pressed()[pygame.K_SPACE]:
    gameStart = True

  if gameStart == True:
    #b.display
    bg = pygame.image.load('PrisonCellBg.png')
    bg = pygame.transform.scale(bg, (500, 250))
    screen.blit(bg, (0, 0))
    bun.bunDis(250)
    pygame.display.flip()

    #instantiate bunny class & first minigame

  else:
    bg = pygame.image.load('PrisonBg.png')
    bg = pygame.transform.scale(bg, (500, 250))
    screen.blit(bg, (0, 0))
    pygame.display.flip()

#edit while loop later
  
#  while gameStart == True:
 #   maze = Maze(1,1,True)
  #  maze.Maze()
    #memoryGame = MemoryGame(True)
    #memoryGame.memoryGame()
    
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

pygame.quit()
