from dataclasses import dataclass
from typing import List
from abc import ABC, abstractmethod


@dataclass
class Entity(ABC):
    x: int
    y: int
    hp: int
    @abstractmethod
    def entity_name(self):
        pass

    def draw(self,screen,resource_manager):
        screen.blit(resource_manager.get(self.entity_name(),"front"),(self.x,self.y))


@dataclass
class Player(Entity):
    name: str

    def entity_name(self):
        return "player"


@dataclass
class Enemy(Entity):
    type: str = 'melee'
    entity_name = "enemy"



@dataclass
class Character:
    name: str
    mana: str
    hp: int
    level: int


@dataclass
class Item:
    name: str
    effect: str
    cost: int


@dataclass
class Skill(Item):
    description: str


@dataclass
class Inventory:
    items: list[Item]


@dataclass
class Event:
    name: str
    description: str


@dataclass
class Game:
    players: List[Player]
    enemies: List[Enemy]
    items: List[Item]
