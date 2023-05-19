import requests
import json
import pprint
import webbrowser
'''
time stamp - znak czasu
od 1 stycznia 1970
'''

from datetime import datetime, timedelta
timeBefore = timedelta(days=7)
searchDate = datetime.today() - timeBefore
"""
API - Application Programming Interface
minimalnie 15 pkt
posegregowane malejąco
z ostatniego tygodnia
kategorii python

"""
params ={
    "site" : "stackoverflow",
    "sort": "votes",
    "order": "desc",
    "fromdate":"2022-11-20",
    "tagged":"python",
    "min": 15
    }
'''
r = requests.get("https://api.stackexchange.com/2.2/questions/", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])
'''






















    
