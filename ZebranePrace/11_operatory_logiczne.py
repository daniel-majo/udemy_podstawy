# szczęście gdy weekend

##IsWeekend = True
##print ("IsWeekend=",IsWeekend)
##
##Temperature = 20
##print ("Temperature=",Temperature)
##
##ToDoList =" "
##print ("ToDoList=",ToDoList)
##
##IsHappy = (IsWeekend and Temperature >=20 and ToDoList==" ")
##print ("IsHappy=", IsHappy)


# brak szczęścia gdy tmp spada do 5 stopni

##IsWeekend = True
##print ("IsWeekend=",IsWeekend)
##
##Temperature = 5
##print ("Temperature=",Temperature)
##
##ToDoList =" "
##print ("ToDoList=",ToDoList)
##
##IsHappy = (IsWeekend and Temperature >=20 and ToDoList==" ")
##print ("IsHappy=", IsHappy)


# nie ma weekendu, nie ma temperatury i jest coś do zrobienia

IsWeekend = False
print ("IsWeekend=",IsWeekend)

Temperature = 5
print ("Temperature=",Temperature)

ToDoList ="Shopping"
print ("ToDoList=",ToDoList)

##IsHappy = (IsWeekend and Temperature >=20 and ToDoList==" ")
##print ("IsHappy=", IsHappy)
##
##IsHappy = (not IsWeekend and Temperature <20 and ToDoList!=" ")
##print ("IsHappy=", IsHappy)

IsHappy = (IsWeekend and Temperature >=20 and ToDoList==" "\
           or not IsWeekend and Temperature <20 and ToDoList!=" ")
print ("IsHappy=", IsHappy)
