import requests
from send_email import send_email

api_key = "1482cdf6c9df493abb682d6980cf1816"

# creating a special request object. Make request
request = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2024-03-19&sortBy=publishedAt&apiKey"
                       "=1482cdf6c9df493abb682d6980cf1816")

# Get dictionary with data
content = request.json()
print(content)

news = ""
for article in content['articles']:
    news = news + str(article['title']) + "\n" + str(article['description'])

print(news)

message = f"""\
Subject: News titles and descriptions on Tesla

From: r00t7h3ll@gmail.com
{news}
"""

send_email(message)
