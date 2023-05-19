def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

print ("Program wyznaczający równanie pierwiastki równania kwadratowego")
print ("Podaj wartości liczbowe dla a, b i c")
print ("------------------------------------------------")

a1=input('Podaj wartość a: ')
b1=input('Podaj wartość b: ')
c1=input('Podaj wartość c: ')

if not (check_int(a1) and check_int(b1) and check_int(c1)):
    print ("Liczby a, b i c muszą być całkowite aby wyznaczyć pierwiastki")
else:
    a=int(a1)
    b=int(b1)
    c=int(c1)
    if a==0:
        print ("a nie może być równe 0!")
    else:
        delta=b**2 - 4*a*c
        if delta<0:
            print ("nie ma pierwisatków")
        elif delta==0:
            x1=-b/(2*a)
            print ("Równanie ma jedno rozwiązanie %.2f" % (x1))
        else:
            x1=(-b-delta**0.5)/(2*a)
            x2=(-b+delta**0.5)/(2*a)
            print ("Równanie ma dwa rozwiązania %.2f i %.2f" % (x1,x2))
                




