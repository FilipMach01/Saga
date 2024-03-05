import pygame
from pygame import QUIT

from entities import Player, Enemy
from utils import ResourceManager

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Saga!')

player = Player(0, 0, 10, "Jane")
enemies = [Enemy(0, 0, 10)]

manager = ResourceManager()
# screen.blit(manager.get("player", "front"),(400,300))
# screen.blit(manager.get("enemy", "back"),(0,0))
player.draw(screen,manager)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:  # or event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    pygame.display.update()

print(player)
print(enemies)
