import sys  #import biblioteki zwracającej wartość zajętości pamięci
# wyrażenie listowe
evenNumbers = [element
                for element in range(400)
                if (element%2==0)
              ]
 
#wyrażenie generujące zajmuje mniej pamięci w systemie
evenNumbersGenerator = (element
                        for element in range(400)
                        if (element %2 ==0)

                )

#print(sys.getsizeof(evenNumbers))
#print(sys.getsizeof(evenNumbersGenerator)) # sprawdzenie zajętości pamięci
#print(evenNumbers)

#print(evenNumbersGenerator)

#for item in evenNumbersGenerator: # wyświetlenie kolejnych liczb z określonego zakresu
#    print(item)

liczby = (element
            for element in range(101)
            if (element**2)
          )

print(sum(liczby))

