banknoty=[500,200,100,50,20,10,5,2,1]
banknoty.sort()
banknoty.reverse()

print ('Lista banknotów:',banknoty)

a = int(input('Podaj wartość jaką chciałbyś wpłacić '))
waluta=a
kasa=[]
i=0

''' dopóki coś się uda włożyć na listę
    dopóki suma elementów znajdujących się na liście box i kolejny element
    są ciągle jeszcze mniejsze niż pojemność (pudła)paczki boxCapacity'''

#while sum(box)+cargo[i]<boxCapacity and i<len(cargo):
    
''' dodawaj do zmiennej box kolejne elementy z listy cargo
        a następnie przejdź do kolejnej paczki...
        ta wersja nie jest zbyt doskonała, bo dodaje z listy wg. kolejności
        i nie wykorzystuje pojemności pudła na maxa'''
#    box.append(cargo[i])
#    i+=1

'''Przetwarzać mamy tak długo dopóki ilość wolnego miejsca w boxCapacity
jest większa lub równa od najmniejszego elementu listy cargo
'''
while i<len(banknoty) and (waluta - sum(kasa) >=min(banknoty)):
    if (waluta - sum(kasa)) >= banknoty[i]:
        kasa.append(banknoty[i])
    i+=1

print ("Wartość kwoty wynosi:",sum(kasa),"zł")
print ("Banknoty, które chciałbyś wpłacić mogłyby mieć wartości:", kasa)
