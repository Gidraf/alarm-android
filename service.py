from turtle import title
from celery import Celery
import subprocess
import requests
from bs4 import BeautifulSoup
celery = Celery("lma_scheduler", broker="redis://127.0.0.1:6379/0")


@celery.task
def get_article(url,read_time):
    # logger.error("I am error")
    """Scrape URLs to generate article content."""
    text = requests.get(url).text
    link = BeautifulSoup(text, 'html.parser')
    title = getTitle(link)
    subprocess.call(f'''termux-vibrate -d 5000 -f && termux-notification  --sound --title "Time to read {title}" --id "{url}"  --action "xdg-open {url}"''', shell=True)


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



def getImage(link):
    """Attempt to get image."""
    image = ''
    if link.find("meta", property="og:image") is not None:
        image = link.find("meta", property="og:image").get('content')
    elif link.find("img") is not None:
        image = link.find("img").get('href')
    return image