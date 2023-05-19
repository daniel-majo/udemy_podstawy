'''funkcja, która nic nie zwraca tylko wyświetla'''

def display_sum(a,b):
    print(a+b)

sum = display_sum(2,3)# funkcja przyjmuje wartości ale nie zwraca wyniku stąd None
print(sum)

'''funkcja, która zwraca'''


def calculate_sum(a,b):
    return a + b
    
sum = calculate_sum(2,3) # funckja przyjmuje wartości i tutaj już zwraca bo mamy return
print(sum)

def print_message(): #funkcja nie przyjmuje żadnych wartości i nic nie zwraca
    print("Witam Cię")

print_message()
