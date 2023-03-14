from tech_news.database import search_news


def search_by_title(title):
    news = []
    title_news = search_news({"title": {"$regex": title, "$options": "i"}})

    for item in title_news:
        news.append((item["title"], item["url"]))

    return news


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
