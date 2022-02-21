from datetime import datetime
import requests
from bs4 import BeautifulSoup
import sqlite3
from celery import Celery
from celery.utils.log import get_task_logger
import subprocess

celery = Celery("lma_scheduler", broker="redis://127.0.0.1:6379/0")

# con = sqlite3.connect('articles.db')

logger = get_task_logger(__name__)

@celery.task
def get_article(url,read_time):
    # logger.error("I am error")
    """Scrape URLs to generate article content."""
    subprocess.call(f'''termux-vibrate -d 5000 -f && termux-notification  --sound --title "Time to read {url}" --ongoing''', shell=True)


def getImage(link):
    """Attempt to get image."""
    image = ''
    if link.find("meta", property="og:image") is not None:
        image = link.find("meta", property="og:image").get('content')
    elif link.find("img") is not None:
        image = link.find("img").get('href')
    return image

def getTitle(link):
    """Attempt to get a title."""
    title = ''
    link_title = link.title
    if link_title is not None and link_title.string is not None:
        title = link.title.string
    elif link.find("meta", property="og:title") is not None:
        title = link.find("meta", property="og:title").content
    elif link.findAll("h1") is not None:
        h1 = link.find("h1")[0]
        title = h1.text.strip()
    return title


def getDescription(link):
    """Attempt to get description."""
    description = ''
    if link.find("meta", property="og:description") is not None:
        description = link.find("meta", property="og:description").get('content')
    elif link.find("p") is not None:
        description = link.findAll("p")[0].text.strip()
    return description