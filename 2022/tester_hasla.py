password = input('Podaj hasło: ')
lowercase_letter_counter = 0
uppercase_letter_counter = 0
numbers_couter = 0
special_characters = '!@#$%^&*()'

for char in password:
    if char.islower():
        lowercase_letter_counter +=1

    elif char.isupper():
        uppercase_letter_counter += 1

    elif char.isnumeric():
        numbers_couter+=1

    elif char in special_characters:
        special_characters +=1
print("Małe litery ", lowercase_letter_counter)
print("Duże litery ", uppercase_letter_counter)

if len(password) >= 16 and lowercase_letter_counter > 2 and uppercase_letter_counter > 2 and numbers_couter > 1 and special_characters > 2:
    print("Hasło jest OK!")
else:
    print("Hasło jest słabe")