import math
import random
inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable=random.random()
#print ('Ilość elementów listy inputdata',len(inputdata))


##if (len(inputdata))==factortable:
##    print ('ok')
i=0
while i<len(inputdata):
    minvalue=inputdata[i]-factortable*inputdata[i]
    maxvalue=inputdata[i]+factortable*inputdata[i]
    print('minvalue',minvalue,'maxvalue',maxvalue)
        
    mininteger = math.floor(minvalue)
    maxinteger = math.ceil(maxvalue)
    print('mininteger',mininteger,"\t",'inputdata',inputdata[i],"\t",'maxinteger',maxinteger)

    i+=1
##else:
##    print ('inputdata and factortable need to have equal number of elements')
