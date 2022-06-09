from email import header
import requests

from webapp.db import db
from webapp.news.models import News

def get_html(url):
    headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.36 (Edition Yx 05)'
    }
    try:
        result = requests.get(url, headers = headers)
        result.raise_for_status()          # обязательно вносить строку, чтобы исключить ошибки сервера
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()