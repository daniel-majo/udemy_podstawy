'''
Programowanie obiektowe

self - a ang. ja... 'sam osobiście, siebie
'''
class User:
    age = '18'
    first_name = "Jan"
    height = '80'

    def print_age(self, message):
        print(f'{self.first_name} ma {self.age} lat i {self.height} wzrostu. Wysłał/a wiadomość {message}')



user1 = User()
user2 = User()

user_list = [User(), User()]

user_list[0].first_name = 'Daniel'
user_list[1].first_name = 'Elzbieta'

user1.first_name = 'Daniel'
user2.first_name = 'Elżbieta'
    
user1.age = 44
# user2.age = 43

user1.height = 182
user2.height = 174

user1.print_age('jakiś dowoly tekst')
user2.print_age('jeszcze inny tekst')

print(user_list[0].print_age('Jakiś dowlny tekst'))
print(user_list[1].print_age('Jakiś iny dowlny tekst'))

