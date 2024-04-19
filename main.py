import requests

# creating a special request object. Make request
request = requests.get("https://newsapi.org/v2/everything?q=tesla&"
                       "from=2024-03-19&sortBy=publishedAt"
                       "&apiKey=1482cdf6c9df493abb682d6980cf1816")

# content = request.text
# print(content)
# print(type(content))

# Get dictionary with data
content = request.json()
print(content['articles'])

# title = []
#
# for article in content['articles']:
#     title.append(article['title'])
#
# print(type(title))
# access title and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])