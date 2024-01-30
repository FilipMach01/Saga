import pygame
import sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Saga!')

speed = 4

# clock
clock = pygame.time.Clock()
fps = 60
# background
background_surf = pygame.image.load("graphic/background.png").convert()
background_blit = background_surf,(0,0)

# player
player_surf_front = pygame.image.load("graphic/player_from_front.png").convert_alpha()
player_rect = player_surf_front.get_rect(center = (400,300))

player_surf_back = pygame.image.load("graphic/player_from_back.png").convert_alpha()

player_surf_left = pygame.image.load("graphic/player_from_left.jpg").convert_alpha()

player_surf_right = pygame.image.load("graphic/player_from_right.jpg").convert_alpha()

Run = True
while Run:
  clock.tick(fps)
  for event in pygame.event.get():
      if event.type == QUIT:
          Run = False
  screen.blit(background_surf,(0,0))          
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    player_rect.top -= speed
    screen.blit(player_surf_back, player_rect)
  elif keys[pygame.K_s]:
    player_rect.bottom += speed
    screen.blit(player_surf_front, player_rect)
  elif keys[pygame.K_a]:
    player_rect.left -= speed
    screen.blit(player_surf_left, player_rect)
  elif keys[pygame.K_d]:
    player_rect.right += speed
    screen.blit(player_surf_right, player_rect)
  else:
    screen.blit(player_surf_front, player_rect)
  

  
  pygame.display.update()