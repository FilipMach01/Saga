from dataclasses import dataclass

import pygame
from pygame import Surface


@dataclass
class Resource:
    id: str
    filename: str
    scale: tuple[int, int]
    data: Surface = None


@dataclass
class ResourceManager:
    resources = {
        "player": {
            "front": Resource("player_front", "graphic/player_from_front.png", (65, 65))
        },
        "enemy": {
            "back": Resource("player_front", "graphic/enemy.png", (65, 65))
        }
    }

    def load(self, resource: Resource):
        surface = pygame.image.load(resource.filename).convert_alpha()
        surface = pygame.transform.scale(surface, resource.scale)
        resource.data = surface
        return surface

    def get(self, entity, side):
        resource = self.resources.get(entity).get(side)
        surface = self.load(resource)

        return surface
