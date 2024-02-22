import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Bunny Break')
color = (255, 255, 255)
screen.fill((color))

pygame.display.flip()

running = True
while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

pygame.quit()

