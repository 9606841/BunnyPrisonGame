import pygame
class MemoryGame:
  def __init__(self, running):
    self.running = True
    def MemoryGame():
      pygame.init()
      if pygame.key.get_pressed()[pygame.K_SPACE]:
       pygame.display.set_caption('Memory Game, click to continue')
      elif pygame.mouse.get_pressed()[0]:
        running = False
#def MermoryGame():
  #pygame.init()
  #screen = pygame.display.set_mode(500,500)
  #pygame.display.set_caption('Memory Game')
  #colors = (Color(199, 41, 10), Color(36, 102, 10), Color(81, 28, 97))
#def mousedPressed:

import pygame
import os

#initial module
pygame.init()

#set up display
width = 600
height = 600
screen = pygame.display.set_mode((width, height))

#upload images
image_folder = "images"  # folder containing images
image_files = sorted([os.path.join(image_folder, f) for f in os.listdir(image_folder) if
                      f.endswith("heartfront.png")])

images = [pygame.image.load(img) for img in image_files]

#set clock
fps = 3
clock = pygame.time.Clock()

#main loop
running = True
frame = 0
while running:
  screen.fill(0, 0, 0)
  screen.blit(images[frame], (0,0)) #draw first frame
  frame = (frame + 1) % len(images) #update frame
  pygame.display.flip() #update display

  #check for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  #limit frame rate
  clock.tick(fps)

pygame.quit()

