```python
import requests
import os

def get_ai_news():
    api_key = os.environ["NEWS_API_KEY"]
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "artificial intelligence OR AI model OR LLM",
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": api_key,
        "language": "en"
    }
    response = requests.get(url, params=params)
    return response.json().get("articles", [])

def send_telegram(message):
    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data={"chat_id": chat_id, "text": message, "parse_mode": "HTML"})

articles = get_ai_news()
if not articles:
    send_telegram("No new AI articles found this run.")
else:
    for article in articles[:3]:
        msg = f"<b>{article['title']}</b>\n\n{article['description']}\n\n{article['url']}"
        send_telegram(msg)
```
