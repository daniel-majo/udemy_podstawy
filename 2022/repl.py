# generator haseł
from string import ascii_lowercase, ascii_uppercase,digits
from random import choices, shuffle 
special_charakters = '!@#$%^&*()'

numbers_of_characters = 16

password = choices(digits,k=2)

#password = password + choices(ascii_uppercase, k=2)
# to samo
password += choices(ascii_uppercase, k=2)

password += choices(digits, k=2)
password += choices(special_charakters, k=2)
password += choices(ascii_uppercase, k=2)
password += choices(ascii_lowercase,k=numbers_of_characters-6)
shuffle(password)
print(''.join(password))