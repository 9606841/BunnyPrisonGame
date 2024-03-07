#from Cell import Cell

import pygame

pygame.init()

#maze class
# render squares (path), collision detection for walls, create endpoints
# use wall img as collision detection and then force bunny to walk on path (seprate image) only


class Maze:

  def __init__(self, col, row, running):
    #self.col = col
   # self.row = row
    #self.thickness = 4
    #self.gridCells = 5
    self.running = running
    
  def Maze(self):
      pygame.init()
      if pygame.key.get_pressed()[pygame.K_SPACE] and self.running:
        pygame.display.set_caption('Maze, click to continue')
      elif pygame.mouse.get_pressed()[0]:
        self.running = False
      #Cell(cols, rows, self.thickness) for rows in range(self.row)
      #for cols in range(self.col)
        
  # display the maze
  def maDisplay():
    
