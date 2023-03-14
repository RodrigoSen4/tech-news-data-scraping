from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    news = []
    title_news = search_news({"title": {"$regex": title, "$options": "i"}})

    for item in title_news:
        news.append((item["title"], item["url"]))

    return news


def search_by_date(date):
    try:
        news = []
        date_time = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        time = search_news({"timestamp": date_time})

        for item in time:
            news.append((item["title"], item["url"]))

        return news

    except ValueError:
        raise ValueError("Data inválida")


def search_by_category(category):
    news = []
    category_news = (
        search_news({"category": {"$regex": category, "$options": "i"}})
    )

    for item in category_news:
        news.append((item["title"], item["url"]))

    return news
