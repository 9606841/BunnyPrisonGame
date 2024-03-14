import pygame
from pygame.locals import *
# get code to show up on screen
# create end game logic
# adjust graphics/colors(designers)
TILE_SIZE = 64
WIDTH = TILE_SIZE * 4
HEIGHT = TILE_SIZE * 4

screen = pygame.display.set_mode((512, 512))
empty = pygame.image.load("empty.png")
wall = pygame.image.load("wall.png")
goal = pygame.image.load("goal.png")

tiles = [empty, wall, goal]

maze = [
    [0,0,0,0,0,0,1,1],
    [0,0,1,0,0,1,1,0],
    [0,0,0,0,0,0,0,0],
    [0,0,1,1,0,1,0,0],
    [0,0,1,0,1,0,0,1],
    [1,0,1,0,1,1,0,0],
    [0,1,0,0,0,1,0,1],
    [0,0,0,0,0,0,0,2]
]

surface = pygame.display.set_mode((500, 500))
color = (22, 27, 41)

def draw():
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            tile = pygame.transform.scale(tiles[maze[row][column]], (64,64))
            screen.blit(tile, (x, y))
    pygame.display.flip()


px = 20
py = 20
run = True
def mazeRun():
  screen.fill((255,255,255))
  draw()
  player = pygame.draw.ellipse(screen, color, (px, py, 20,20))
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == KEYDOWN:
      r = py
      c = px
      if event.key == K_UP:
        r = r - TILE_SIZE
      if event.key == K_DOWN:
        r = r + TILE_SIZE
      if event.key == K_LEFT:
        c = c - TILE_SIZE
      if event.key == K_RIGHT:
        c = c + TILE_SIZE
      tile = tiles[maze[r // TILE_SIZE][c // TILE_SIZE]]
      if tile == empty:
        px = c
        py = r
      elif tile == goal:
        print('Well done')
        exit()
