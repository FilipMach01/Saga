import math
from dataclasses import dataclass


class Square:

    def __init__(self, a: float):
        self.a = a

    def obvod(self):
        return self.a * 4

    def obsah(self):
        return self.a * self.a


@dataclass
class Circle:

    r: float
    a: str = "circle"

    def obvod(self):
        return self.r * math.pi * 2

    def obsah(self):
        return math.pi * self.r ** 2
