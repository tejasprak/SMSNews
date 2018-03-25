import requests
import json
import threading
import time
def printit():
  threading.Timer(15.0, printit).start()
  url = ('https://newsapi.org/v2/top-headlines?'
         'country=us&'
         'apiKey=apiKey')
  response = requests.get(url)
  current_news = response.json()
  open("news", "w").close()
  with open('news', 'w') as outfile:
    json.dump(current_news, outfile)
  timer = time.time()
  print str(timer)  + " Got new JSON"

printit()
