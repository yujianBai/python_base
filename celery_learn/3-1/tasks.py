# auth Bernard
# date 2020-06-03

import time
from celery import Celery

broker = 'redis://localhost:6379/1'
backend = 'redis://localhost:6379/2'

app = Celery("my_tasko", broker=broker, backend=backend)

@app.task
def add(x, y):
    print("enter task add ...")
    time.sleep(2)
    return x + y
