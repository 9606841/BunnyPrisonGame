import pygame

pygame.init()

#maze class
# render squares (path), collision detection for walls, create endpoints
# use wall img as collision detection and then force bunny to walk on path (seprate image) only - img might not work, will hv to render squares


class Maze:

  def __init__(self, col, row, running):
    self.col = col
    self.row = row
    self.running = running
    
  def Maze(self):
      pygame.init()
      if pygame.key.get_pressed()[pygame.K_SPACE] and self.running:
        pygame.display.set_caption('Maze, click to continue')
      elif pygame.mouse.get_pressed()[0]:
        self.running = False
    # maze wall
    #wall = pygame.image.load('mazewall.png')
    #wall = pygame.transform.scale(wall, (250, 250))  
    bl = pygame.Color(0, 0, 0)
  ` col = pygame.draw.rect(screen, bl, (0, 0, 20, 40))
  
  # display the maze
  def maDisplay():
    #screen.blit(wall, (125, 0))
    pygame.display.flip()
