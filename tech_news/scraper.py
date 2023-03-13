import requests
import time
from parsel import Selector


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


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    next_page = selector.css("a.next::attr(href)").get()

    return next_page


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
