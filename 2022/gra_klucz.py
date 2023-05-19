from random import randint
from math import sqrt

GAME_WIDTH = 10
GAME_HEIGHT = 10

key_x = randint(0,GAME_WIDTH)
key_y = randint(0,GAME_HEIGHT)

player_x = 0
player_y = 0
player_found_key = False

steps = 0
distance_before_move = sqrt((key_x-player_x)**2 + ((key_y-player_y)**2))
# pozycja klucza
#print(key_x,key_y)
while not player_found_key:
    steps += 1
    print()
    print('Możesz udać się w kierunkach jako [W/A/S/D}: ')
    move = input('Dokąd idziesz? ')
    match move.lower():
        case 'w':
            player_y += 1
            if player_y > GAME_HEIGHT:
                print('Uważaj na twarz! Ściana ')
                player_y = GAME_HEIGHT
        case 'a':
            player_x -= 1
            if player_x < 0:
                print('Uważaj na twarz! Ściana ')
                player_x = 0
        case 's':
            player_y -= 1
            if player_y < 0:
                print('Uważaj na twarz! Ściana ')
                player_y = 0
        case 'd':
            player_x += 1
            if player_x > GAME_WIDTH:
                print('Uważaj na twarz! Ściana ')
                player_x = GAME_WIDTH
        case 'q':
            print('Koniec gry! ')
            quit()
        case '_':
            print('Nie wiem dokąd idziesz! ')
            continue

    if player_x == key_x and player_y == key_y:
        print(f'Klucz do skarbu odnaleziony! WYkonałeś zadanie w {steps} ruchach')
        print(20*'-')
        quit()
    distance_after_move = sqrt((key_x-player_x)**2 + ((key_y-player_y)**2))
    if distance_before_move > distance_after_move:
        print('Ciepło! ')
    else:
        print('Zimno! ')
    distance_before_move = distance_after_move
    #print(player_x, player_y)
