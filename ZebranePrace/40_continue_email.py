persons=['Elizabeth','Steven@sales.mycompany.com','Sebastian','Margeret','Svetlana@mycomapny.eu','Raphael']

emails = []
domain = 'mycompany.com'
print ('------------bez continue--------------')
# bez użycia continue

'''for person in persons:
    if '@' in person:
        emails.append(person)
    else:
        email = person + '@' + domain
        emails.append(email)
for email in emails:
    print (email)'''
# z użyciem continue

print ('------------z continue--------------')
for person in persons:
    if '@' in person:
        emails.append(person)
        continue
    email = person + '@' + domain
    emails.append(email)

for email in emails:
    print (email)

