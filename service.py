from celery import Celery
import subprocess
import requests
celery = Celery("lma_scheduler", broker="redis://127.0.0.1:6379/0")

@celery.task
def get_article(url,read_time):
    # logger.error("I am error")
    """Scrape URLs to generate article content."""
    text = requests.get(url).text
    subprocess.call(f'''termux-vibrate -d 5000 -f && termux-notification  --sound --title "Time to read {url}" --id "{url}"  --action "xdg-open {url}" --content{"Desciption here"}''', shell=True)
