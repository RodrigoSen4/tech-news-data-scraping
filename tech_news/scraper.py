import requests
import time
from parsel import Selector
import re
from tech_news.database import create_news


def fetch(url):
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )

        if response.status_code != 200:
            raise requests.RequestException

    except (requests.RequestException):
        return None

    else:
        return response.text

    finally:
        time.sleep(1)


def scrape_updates(html_content):
    selector = Selector(text=html_content)

    links_list = selector.css("h2 a::attr(href)").getall()

    return links_list


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    next_page = selector.css("a.next::attr(href)").get()

    return next_page


def scrape_news(html_content):
    selector = Selector(text=html_content)

    reading_time_string = (
        selector.css(".meta-reading-time::text").get()
    )

    return {

        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".url.fn.n::text").get(),
        "reading_time": int(re.sub("[^0-9]", "", reading_time_string)),
        "summary": selector.xpath("//p").xpath("string()").get().strip(),
        "category": selector.css(".meta-category .label::text").get()
    }


def get_tech_news(amount):
    limit = amount
    page = fetch("https://blog.betrybe.com")
    news = []

    while True:
        links_list = scrape_updates(page)

        for link in links_list:
            news_page = fetch(link)
            news.append(scrape_news(news_page))

            if len(news) >= limit:
                break

        if len(news) >= limit:
            break

        else:
            next_page = scrape_next_page_link(page)
            page = fetch(next_page)

    create_news(news)
    return news

# Insira na função abaixo a quantidade de noticias a serem raspadas.