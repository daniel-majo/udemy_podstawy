animal = input('Podaj jakie zwierzę: ')
def PrintAnimal(animal):
           # this function prints a cat ascii-art
        txt_cat = r'''
    |\---/|
    | o_o |
     \_^_/'''
          
        # this function prints a bear ascii-art
        txt_bear = r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`'''
                       
        # this function prints a bat ascii-art
        txt_bat = r'''
       /\                 /\
      / \'._   (\_/)   _.'/ \
     /_.''._'--('.')--'_.''._\
     | \_ / `;=/ " \=;` \ _/ |
      \/ `\__|`\___/`|__/`  \/
              \(/|\)/  
         '''
        
        

        if animal == 'cat':
            print (txt_cat)
        elif animal == 'bear':
            print(txt_bear)
        elif animal == 'bat':
            print(txt_bat)
        else:
            print ("Nie mogę wydrukować tego  rysunku o nazwie '%s'" %animal)
        return
PrintAnimal(animal)
