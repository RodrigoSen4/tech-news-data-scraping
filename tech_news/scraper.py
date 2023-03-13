import requests
import time
from parsel import Selector
import re


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


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
