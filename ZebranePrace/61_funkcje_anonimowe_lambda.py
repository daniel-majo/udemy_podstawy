def podwoj(x):
    return x*2

print(podwoj(4))

wynik = lambda x: x*2
print(wynik(4))

my_list = [2, 14, 18, 22, 7, 13]

#funkcj lambda i filter

my_list_filtered = list(filter(lambda x: x%2 == 0, my_list))
# lista wyrażeniowa
my_list_filtered2= [x for x in my_list if (x%2)==0]

print(my_list_filtered)
print(my_list_filtered2)
