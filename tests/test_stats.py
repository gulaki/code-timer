from codetimer import *
from time import sleep
from random import random
import matplotlib.pyplot as plt

def test_stats():
    waited, recorded = [], []

    @TimerStats.function_timer
    def randwait(a, b):
        a /= 1000
        b /= 1000
        wait = (b-a)*random()+a
        waited.append(wait)  # store each random wait time in ms
        sleep(wait)

    for i in range(100):
        randwait(0, 10)  # random wait period range in milli seconds.
        recorded.append(randwait.timer.lap)  # store each recorded lap time. This is not necessary for simple stats

    t = randwait.timer
    print(t)  # shows detailed results.

    plt.subplot(2, 2, 1)
    plt.plot(waited, recorded, '.')  # scatter plot of wait period vs. recorded period for each iteration.
    plt.subplot(2, 2, 3)
    plt.hist(waited, 50)  # histogram of wait periods
    plt.subplot(2, 2, 4)
    plt.hist(recorded, 50)  # histogram of recorded periods
    plt.show()

