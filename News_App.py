import requests
import json
query= input("What type of news are you interested in ? : ")
url="https://newsapi.org/v2/everything?q={query}&from=2025-04-20&sortBy=publishedAt&apiKey=c9b624f85bd94c63bc23ad389ecdb08f"
r = requests.get(url)
news=json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-------------------------------------------------------")