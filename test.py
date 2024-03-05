from tridy import Egg,Player
from calculator import Square,Circle

# kocka = Cat("micka")
# kocka_1 = Cat("kocour")
# print(kocka.name, kocka_1.name)



# ctverec_1 = Square(567)
#
# print(f"obvod je: {ctverec_1.obvod()}")
# print(f"obsah je: {ctverec_1.obsah()}")

kruznice:Circle = Circle(6)
kruznice_2 = Square("hello")
print(kruznice, kruznice_2)
print(kruznice.obvod(), kruznice.obsah())
print(kruznice_2.obvod())

egg = Egg(30,50)
print(egg.souradnice())

player = Player(30,50)
# palayer_movement = (40,30)
print(player.get_position())

if egg.souradnice() == player.get_position():
    print("colide")
else:
    print("not colide")