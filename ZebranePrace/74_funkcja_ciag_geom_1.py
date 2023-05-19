''' Budujemy moduł służący do obliczeń na ciągach geometrycznych

a1 - pierwszy element ciągu
factor - współczynnik ciągu geometrycznego
index - oznacza  który element ciągu ma być wyliczony'''

def GiveGeomSeqElement(a1=2, factor=2, index=2):
    value=a1*pow(factor,index-1)
    return value
print ('Moduł służący do obliczeń na n-ty wyraz ciągu geometrycznego')
print ('2^64=', GiveGeomSeqElement(1,2,64))

    
