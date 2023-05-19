'''
JSONplaceholder - miejsce zastępcze na two przyszły json

Popbieranie anych z serwera i odczytywanie danych
    1:11
    2:5
    3:15


'''


import requests
import json


r = requests.get("https://jsonplaceholder.typicode.com/todos")
def count_task_frequency(tasks):
    completedTaskFrequencyByUser = dict()
    for entry in tasks:
        if (entry["completed"] == True):
           try: 
               completedTaskFrequencyByUser[entry["userId"]] += 1
           except KeyError:
               completedTaskFrequencyByUser[entry["userId"]] = 1
    return completedTaskFrequencyByUser

def users_with_top_completed_task(completedTaskFrequencyByUser):
    userIdOfMaxComletedAmountOfTasks = []
    maxAmountedOfCompletedTask = max(completedTaskFrequencyByUser.values())
    for userId, numberOfCompletedTasks in completedTaskFrequencyByUser.items():
        if (numberOfCompletedTasks == maxAmountedOfCompletedTask):
            userIdOfMaxComletedAmountOfTasks.append(userId)
    return userIdOfMaxComletedAmountOfTasks
def get_keys_with_top_values(my_dict): #wyrażenie słownikowe
    return [
        key
        for (key,value) in my_dict.items()
        if value == max(my_dict.values())
    ]
try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    completedTaskFrequencyByUser = count_task_frequency(tasks)
    usersWithTopComletedTasks = users_with_top_completed_task(completedTaskFrequencyByUser)
    print("Wręczamy ciasteczko użytkownikowi o nr id ",users_with_top_completed_task(completedTaskFrequencyByUser))

#sposób 1
'''
r = requests.get("https://jsonplaceholder.typicode.com/users")
users = r.json() #zmiana users w json
for user in users:
    if (user["id"] in usersWithTopComletedTasks):
        print("Wręczamy ciasteczko użytkownikowi o imieniu",user["name"])
'''            

#sposób 2
'''
for userId in usersWithTopComletedTasks:
    #r = requests.get("https://jsonplaceholder.typicode.com/users/", params="id="+str(userId))
    r = requests.get("https://jsonplaceholder.typicode.com/users", params="id="+str(userId))
    user = r.json()
    print("Wręczamy ciasteczko użytkownikowi o imieniu",user[0]["name"])
'''    
#sposób 3
def change_list_into_conj_of_param(my_list):
    conj_param = "id="
    lastIterationMunber = len(my_list)
    i = 0
    for item in my_list:
        i += 1
        if (i == lastIteration):
            conj_param += str(item)
        else:
            conj_param += str(item) + "&id="
    return conj_param

conj_param = change_list_into_conj_of_param(usersWithTopComletedTasks)

r = requests.get("https://jsonplaceholder.typicode.com/users", params="id=5&id=10")        
users = r.json()
for user in users:
    print("Wręczamy ciasteczko użytkownikowi o imieniu",user["name"])
    
    
