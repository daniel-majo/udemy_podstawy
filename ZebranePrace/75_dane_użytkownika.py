#filename=input("Enter filename: ")
#print ("The file name is: %s" % (filename))
# pętla, któa działa do momentu kiedy nie wpiszemy wartości decymalnej /liczbowej/
while True:
    filesizeStr=input("Enter the max file size (MB): ")
    if filesizeStr.isdecimal():
        filesizeInt=int(filesizeStr)
        break
print ("The max size is %d" % (filesizeInt))
print ("Size in KB is %d" % (filesizeInt*1024))


