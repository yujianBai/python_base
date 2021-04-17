# auth Bernard
# date 2021-04-17

import time

def add(a, b, sleep_time):
    time.sleep(sleep_time)
    return "{} add {} is {}".format(a, b, a + b)
