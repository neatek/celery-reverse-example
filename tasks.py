from celery import Celery
from time import sleep

app = Celery('tasks', broker='amqp://guest:guest@localhost:5671/',
             backend='db+sqlite:///results.db')


@app.task
def reverse(text):
    sleep(5)
    return text[::-1]
