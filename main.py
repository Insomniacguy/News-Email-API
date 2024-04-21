import requests
from send_email import send_email

api_key = "1482cdf6c9df493abb682d6980cf1816"
topic = "tesla"

# creating a special request object. Make request
request = requests.get("https://newsapi.org/v2/everything?"
                       f"q={topic}&"
                       "from=2024-04-20&"
                       "sortBy=publishedAt&apiKey"
                       "=1482cdf6c9df493abb682d6980cf1816&"
                       "language=en")

# Get dictionary with data
content = request.json()
print(content)

news = ""
for article in content['articles'][0:10]:
    if article['title'] is not None and article['description'] is not None:
        news = (str(news) + str(article['title']) + str("\n")
                + str(article['description'] + str(2 * "\n")) + "\n" + article['url'])

print(news)

message = f"""\
Subject: Today's news

From: r00t7h3ll@gmail.com
{news}
"""

send_email(message)
