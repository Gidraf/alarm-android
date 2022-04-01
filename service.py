from celery import Celery
import subprocess

celery = Celery("lma_scheduler", broker="redis://127.0.0.1:6379/0")

@celery.task
def get_article(url,read_time):
    # logger.error("I am error")
    """Scrape URLs to generate article content."""
    subprocess.call(f'''termux-vibrate -d 5000 -f && termux-notification  --sound --title "Time to read {url}" --id "{url}"  --action "xdg-open {url}"''', shell=True)
