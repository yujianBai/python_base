# auth Bernard
# date 2020-06-07

import time
from celery_app import app

@app.task
def add(x, y):
    time.sleep(3)
    return x + y
