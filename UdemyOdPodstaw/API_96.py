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
        }

r = requests.get('https://api.thecatapi.com/v1/favourites/')

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format", r.text)
else:
    pprint(questions)
























    
