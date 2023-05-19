cargo=[40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
cargo.sort()
cargo.reverse()

print ('Lista paczek to:',cargo)

boxCapacity = 90
box=[]
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
while i<len(cargo) and (boxCapacity - sum(box) >=min(cargo)):
    if (boxCapacity - sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i+=1

print ("Ciężar wszystkich paczek wynosi:",sum(box))
print ("Paczki, które zostały spakowane do kontenera to:", box)
