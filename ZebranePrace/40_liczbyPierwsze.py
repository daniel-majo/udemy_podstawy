for pierwsza in range (2,31):

    for dzielnik in range (2,pierwsza):

        if pierwsza%dzielnik==0:
            print ('%2d nie jest liczbą pierwszą - dzielnikiem jest %2d' % (pierwsza, dzielnik))
            break
    else:
        print ('%2d jest liczbą pierwszą' % (pierwsza))
