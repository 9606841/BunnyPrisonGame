# Elisa Tandra, Kate Patterson, David Valdespino, Emily Tan

from os import truncate
import pygame
from maze import Maze
from slidePuzzle import slidePuzzle
#from memoryGame import MemoryGame


pygame.init()

screen = pygame.display.set_mode([500, 250])
pygame.display.set_caption('Bunny Break')
bg = pygame.image.load('PrisonBg.png')
bg = pygame.transform.scale(bg, (500, 250))
screen.blit(bg, (0, 0))
gameStart = False
#b = Bunny(250, 125, 0, False)
pygame.display.flip()

running = True
while running:
  if pygame.key.get_pressed()[pygame.K_SPACE]:
    gameStart = True

  if gameStart == True:
    #b.display
    color = (255, 255, 255)
    screen.fill((color))
    pygame.display.flip()

    #instantiate bunny class & first minigame

  else:
    bg = pygame.image.load('PrisonBg.png')
    bg = pygame.transform.scale(bg, (500, 250))
    screen.blit(bg, (0, 0))
    pygame.display.flip()

#  while gameStart == True:
 #   maze = Maze(1,1,True)
  #  maze.Maze()
    #memoryGame = MemoryGame(True)
    #memoryGame.memoryGame()
    
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

pygame.quit()
