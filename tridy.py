import math
# class Cat:
#     def __init__(self, name):
#         self.name = name
#         print("meow")

# class Square:
#
#     def __init__(self, a):
#         self.a = a
#
#     def obvod(self):
#         return self.a * 4
#
#     def obsah(self):
#         return self.a * self.a
#
# class Circle:
#
#     def __init__(self, r):
#         self.r = r
#
#     def obvod(self):
#         return self.r * math.pi * 2
#
#     def obsah(self):
#         return  math.pi * self.r ** 2


class Egg():

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def souradnice(self):
        return self.x,self.y

class Player():

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x,self.y

    # def movement(self,dx,dy):
    #     self.x += dx
    #     self.y += dy

