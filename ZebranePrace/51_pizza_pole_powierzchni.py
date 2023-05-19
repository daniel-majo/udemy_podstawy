import math
# print (math.pi)
degree = 360
radian = degree*math.pi/180



print ('360 stopni[\u02DA]:',radian,'radianów')
print ('------------------')


degree = 45
radian = math.pi*degree/180



print ('45 stopni[\u02DA]:',radian,'radianów')
print ('------------------')

print ('360 stopni[\u02DA] to',math.radians(360),'radianów')
print ('45 stopni[\u02DA] to',math.radians(45),'radianów')

# promień pizzy
small_pizza_r = 0.22
big_pizza_r = 0.27
family_pizza_r = 0.38

# cena pizzy
small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22.00

# pole powierzchni pizzy
small_pp = (math.pi*small_pizza_r)**2
big_pp = (math.pi*big_pizza_r)**2
family_pp = (math.pi*family_pizza_r)**2

# cena za metr kwadratowy
small_cena_mkw = small_pizza_price/small_pp
big_cena_mkw = big_pizza_price/big_pp
family_cena_mkw = family_pizza_price/family_pp
print ('Pole powierzchni pizz')
print ('Small pizza is: ',small_pp)
print ('Big pizza is: ',big_pp)
print ('Family pizza is: ',family_pp)
print ('------------------')
print ('Cena pizz za metr kwadratowy')
print ('Small pizza is: ',small_cena_mkw)
print ('Big pizza is: ',big_cena_mkw)
print ('Family pizza is: ',family_cena_mkw)
print ('------------------')

math_ls = dir(math) 
print(math_ls)



