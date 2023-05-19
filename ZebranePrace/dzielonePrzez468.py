'''
liczby = [liczba
          for liczba in range(1,200)
          if liczba%4 == 0
          if liczba%6 == 0
          if liczba%8 == 0
          ]
          '''

    
for liczba in range(1,200):
    if (liczba%4==0) and liczba%6==0 and liczba%8==0:
        print(liczba)
