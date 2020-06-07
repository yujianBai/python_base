#auth Bernard
#date 2020-06-07

from celery import Celery

app = Celery('demo')
app.config_from_object('celery_app.celeryconfig')

if __name__ == "__main__":
    pass