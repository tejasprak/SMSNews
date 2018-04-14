from twilio.rest import Client
import requests
from eventregistry import *
import json


account_sid = ""
auth_token = ""
newsapi = ""
def sendMessage(message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            body=message,
            to="+",
            from_="+")

    print(message.sid)
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=apiKey')
response = requests.get(url)
current_news = response.json()
headlines = current_news['articles']
i=1
message = ""
for h in headlines:
    if(i<11):
        message = message + str(i) + ". " + h['title'] + "\n"
        i=i+1
print message
sendMessage(message)
