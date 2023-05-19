age = 21
#if age>=18:
#    print ("Jesteś pełnoletni, możesz kupić alkohol")
#else:
#    print ("Jesteś za młody, niestety nie możesz kupić alkoholu")
isDrunk=True
#if age>=18 and not isDrunk:
#    print ("Jesteś pełnoletni, możesz kupić alkohol")
#else:
#    print ("Przepraszam, niestety nie możesz kupić alkoholu.")

isRestrictedArea=False
if age>=18 and not isDrunk and not isRestrictedArea:
    print ("Jesteś pełnoletni, możesz kupić alkohol")
else:
    print ("Przepraszam, niestety nie możesz kupić alkoholu.")
