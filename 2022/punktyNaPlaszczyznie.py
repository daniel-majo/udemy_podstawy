'''
Odbierz od użytkownika dwa dowolne punkty na płaszczyźnie(x1,x2,y1,y2), które tworzą odcinek.
Musisz zapytać użytkownika o cztery wartości.
Napisz jakie jest pole oraz promień okręgu, którego ten odcinek jest średnicą. 
Dla ułatwienia przyjmij, że PI ma wrtość 3.14
|AB| = sqrt((x2-x1)**2 + (y2-y1)**2)
'''
from math import sqrt
x1 = int(input('Podaj współrzędną A(x1): '))
y1 = int(input('Podaj współrzędną A(y1): '))
x2 = int(input('Podaj współrzędną B(x2): '))
y2 = int(input('Podaj współrzędną B(y2): '))

diameter = float(sqrt((x2-x1)**2 + (y2-y1)**2)) #srednica

area= 3.14 * (diameter/2) **2
circle_radius = diameter/2
print(f'Długość odcinka - {diameter:.2f}, pole koła - {area:.2f}, promień okręgu - {circle_radius:.2f}')