import pygame
import sys
from pygame.locals import QUIT
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Saga!')

enemies = []
enemies_to_delete = []
speed = 10
background_speed = 3
# clock
clock = pygame.time.Clock()
fps = 60
# background
background_surf = pygame.image.load("graphic/idk.jpg").convert()
background_surf = pygame.transform.scale2x(background_surf)
background_rect = background_surf.get_rect(center = (700,300))


menu_surf = pygame.image.load('graphic/dragon.png').convert()
# player

player_surf_front = pygame.image.load("graphic/player_from_front.png").convert_alpha()
player_surf_front = pygame.transform.scale(player_surf_front,(65,65))

player_surf_back = pygame.image.load("graphic/player_from_back.png").convert_alpha()
player_surf_back = pygame.transform.scale(player_surf_back,(65,65))

player_surf_left = pygame.image.load("graphic/player_from_left.png").convert_alpha()
player_surf_left = pygame.transform.scale(player_surf_left,(50,65))

player_surf_right = pygame.image.load("graphic/player_from_right.png").convert_alpha()
player_surf_right = pygame.transform.scale(player_surf_right,(50,65))


player_rect = player_surf_front.get_rect(center = (400,300))
# enemy
enemy_surf = pygame.image.load("graphic/enemy.png").convert_alpha()

# font
base_font = pygame.font.Font("graphic/Pixeltype.ttf",80) 
second_font = pygame.font.Font("graphic/Pixeltype.ttf",50) 


game_active = False
Run = True
while Run:
  clock.tick(fps)
  for event in pygame.event.get():
      if event.type == QUIT:
          Run = False
  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_SPACE]:
     game_active = True          
  
  if game_active == True:
    screen.blit(background_surf,background_rect)
    if keys[pygame.K_w]:
      background_rect.top += background_speed
      if background_rect.top > 0:
        background_rect.top = 0
      screen.blit(player_surf_back, player_rect)
    
    elif keys[pygame.K_s]:
      background_rect.top -= background_speed
      if background_rect.top < -1400: 
        background_rect.top = -1400
      screen.blit(player_surf_front, player_rect)
    
    elif keys[pygame.K_a]:
      background_rect.left += background_speed
      if background_rect.left > 0:
          background_rect.left = 0 
      screen.blit(player_surf_left, player_rect)
    
    elif keys[pygame.K_d]:
      background_rect.right -= background_speed
      if background_rect.right < 700:
          background_rect.right = 700
      screen.blit(player_surf_right, player_rect)
    
    else: 
      screen.blit(player_surf_front, player_rect) 
  else:
    #  screen.fill((110, 83, 173))
     screen.blit(menu_surf,(0,0))
     text_surf = base_font.render("Welcome to Saga!",True,(255,255,255))
     text_surf_rect = text_surf.get_rect(center = (400,300))
     press_space_surf = second_font.render("press space to start",True,(255,255,255))
     press_space_surf_rect = press_space_surf.get_rect(center = (400,450))
     screen.blit(text_surf,text_surf_rect)
     screen.blit(press_space_surf,press_space_surf_rect)
    

  # enemies
  # if len(enemies) < 0:
  #   # Generate new enemy
  #   new_enemy = {
  #       'surface': enemy_surf,
  #       'rect': enemy_surf.get_rect(center=(random.randint(-500, 500), random.randint(-500, 500))),
  #       'speed': 0.1
  #   }
  #   enemies.append(new_enemy)

  # for enemy in enemies:
  #   # Move the enemy towards the center of the screen
  #   dx = (400 - enemy['rect'].centerx) / 10
  #   dy = (300 - enemy['rect'].centery) / 10
  #   enemy['rect'].move_ip(dx * enemy['speed'], dy * enemy['speed'])

  #   # Remove the enemy if it has reached the center of the screen
  #   if enemy['rect'].center == (400, 300):
  #     enemies_to_delete.append(enemy)
  
  # for enemy in enemies:
  #     screen.blit(enemy['surface'], enemy['rect'])
  # for enemy in enemies_to_delete:
  #   enemies.remove(enemy)  
  
  pygame.display.update()