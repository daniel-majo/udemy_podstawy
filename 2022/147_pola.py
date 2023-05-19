'''
Stwórz trzy klasy
1) Rectangle - prostokąt
2) Square - kwadrat
3) Cube - sześcian

a) stwórz kontruktory (__init__)
b) metody obliczające powierzchnię kwadratu, prostokąta, sześcianu
c) metodę obliczającą objętość sześcianu

Zastanów się jak możesz wykorzystać do tego dziedziczenia, aby nie powtarzać kodu
'''


class Rectangle:
    def __init__(self, length_a: float, length_b: float):
        self.length_a = length_a
        self.length_b = length_b

    def area_rectangle(self):
        return self.length_a * self.length_b
    

class Square(Rectangle): #kwadrat
    def __init__(self, length_a: float):
        super().__init__(length_a, length_a)    
    
    def area_square(self):
        return self.length_a * self.length_a

class Cube(Square):
    def area_cube(self):
        return super().area_square() * 6

    def capacity_cube(self):
        return super().area_square() * self.length_a

prostokat = Rectangle(2,2)
print(prostokat.area_rectangle())
kwadrat = Square(3)
print(kwadrat.area_square())
kostka = Cube(2)
print(kostka.area_cube())
print(kostka.capacity_cube())