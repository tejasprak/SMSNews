# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
import requests
import json
from twilio.twiml.messaging_response import MessagingResponse
from goose import Goose

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    body = request.values.get('Body', None)
    # Start our response
    with open('news') as data_file:
        current_news = json.load(data_file)
    headlines = current_news['articles']
    message = ""
    if "news" in body or "News" in body:
        headlines = current_news['articles']
        i=0
        while i < 19:
            message = message + str(i+1) + ". " + headlines[i]['title'] + "\n"
            i=i+1
    elif "more" in body:
        i = int(body.split()[0])
        headlines = current_news['articles']
        url = headlines[i-1]['url']
        g = Goose()
        article = g.extract(url=url)
        message = article.cleaned_text[:1000]
        message2 = article.cleaned_text[1000:][:1000]
        message = message + "..."
    else:
        i=int(body)
        message = ""
        message = headlines[i-1]['description']
    resp = MessagingResponse()
    # Add a message
    resp.message(message)

    return str(resp)
if __name__ == "__main__":
    app.run(debug=True)
