## SMSNews
Server that will connect to Twilio and serve latest world news via SMS.

### Installation

```Python
prereq: flask, requests, json, twilio, goose
```
- Ensure you have Twilio account with balance, and enter Twilio API authentication token into **main.py**
```Python
python server.py
python bot.py
```
- Keep both running in different terminal windows, use **ngrok** binary to expose localhost to internet, and enter ngrok address into Twilio webhook field
### Usage
- Type in "news" for an overview of what's going on right now.
- For a further description you can type in the number corresponding to the headline you want to know more about, like "5" or "7".
- To read the article itself, you can type in the number of the article and then "more", like "5 more" or "7 more".

### How it works
Server Component - Written in Python using Flask and Goose(**server.py**)
- It receives the GET/POST request from Twilio and processes the received message.
- Depending on the message, it constructs a reply and returns it to the sender.
- **ngrok** exposes localhost/sms to the internet
Client Component - Written in Python (**bot.py**)
- Every ten minutes, this script sends a request to NewsAPI's server.
- It takes the JSON response and stores it locally for server.py to parse when replying.



 The user can message the Twilio number, which activates the hook to the SMSNews server. The SMSNews server will receive and process this response, and then reply a number which corresponds to an article and short description. If the user is still interested in reading more, he/she can reply to the bot requesting for more information and the whole article will be displayed. I built it by merging an API (NewsAPI) into Twilio using Python. This app has a server component and an API component, it takes commands via SMS and delivers the latest API results. I also migrated to DigitalOcean to host the app.

### Inspiration
Thinking of the 2011 Egyptian protests, where an "unprecedented" internet block occurred when all routes to Egyptian networks were shut down for two days, I realized that a tool to always provide current events via SMS would be extremely helpful. I decided to make a news interface through SMS that would allow users to be able to access current events, completely uncensored, through SMS. Due to the scarcity of internet in certain areas, it would allow people to stay up to date on current events anywhere in the world.

### Links
[Tejas Prakash's Website](http://tejasp.me)
[Devpost Page](https://devpost.com/software/sms-news)
[LosAltosHacks III](https://www.losaltoshacks.com/2018/)


Written for LosAltosHacks III on March 24, 2018.
Team Members: Tejas Prakash, Pranav Janjam
