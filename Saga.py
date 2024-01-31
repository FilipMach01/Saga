import pygame
import sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Saga!')

speed = 4
background_speed = 3
# clock
clock = pygame.time.Clock()
fps = 60
# background
background_surf = pygame.image.load("graphic/background.png").convert()
background_surf = pygame.transform.scale(background_surf, (1600,1200))
background_rect = background_surf.get_rect(center = (400,300))

# player
player_surf_front = pygame.image.load("graphic/player_from_front.png").convert_alpha()
player_rect = player_surf_front.get_rect(center = (400,300))

player_surf_back = pygame.image.load("graphic/player_from_back.png").convert_alpha()

player_surf_left = pygame.image.load("graphic/player_from_left.png").convert_alpha()

player_surf_right = pygame.image.load("graphic/player_from_right.png").convert_alpha()

Run = True
while Run:
  clock.tick(fps)
  for event in pygame.event.get():
      if event.type == QUIT:
          Run = False
            
  keys = pygame.key.get_pressed()
  screen.blit(background_surf,background_rect)
  if keys[pygame.K_w]:
    background_rect.top += background_speed
    if background_rect.top > 0:
      background_rect.top = 0
    screen.blit(player_surf_back, player_rect)
  
  elif keys[pygame.K_s]:
    background_rect.top -= background_speed
    if background_rect.top < -600: 
      background_rect.top = -600
    screen.blit(player_surf_front, player_rect)
  
  elif keys[pygame.K_a]:
    background_rect.left += background_speed
    if background_rect.left > 0:
        background_rect.left = 0
    screen.blit(player_surf_left, player_rect)
  
  elif keys[pygame.K_d]:
    background_rect.right -= background_speed
    if background_rect.right < 800:
        background_rect.right = 800
    screen.blit(player_surf_right, player_rect)
  
  else: 
     screen.blit(player_surf_front, player_rect) 
  
  
    
  
  pygame.display.update()