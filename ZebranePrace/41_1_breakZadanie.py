'''Dany jest tekst:

text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.'


Ten tekst to definicja pewnego pojęcia. Twoim zadaniem jest zbudowanie
streszczenia tej definicji poprzez wyświetlenie piewszych 20 słów

- podziel ten tekst ze względu na spacje i zapisz wynik w zmiennej words

- zadeklaruj zmienną short_text, która będzie pustym napisem

- zadeklaruj zmienną counter o wartości 0

- dla każdego słowa z listy words

    - dodaj przetwarzane słowo do short_text

    - zwiększ liczbę counter o 1

    - jeżeli liczba counter jest >= 20

    - wyświetl tekst

    - przerwij pętlę'''

text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.'

text=text[0:text.find('.')+1]
print (text)

short_text=' '
words=text.split(' ')


counter=0

for word in words:
    short_text += word + short_text
    counter += 1
    if counter >= 20:
        print(short_text)
        break
print ('----------------------')
