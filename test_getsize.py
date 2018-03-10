from codetimer import *
import random
import matplotlib.pyplot as plt

data1 = []
data2 = []

mem = MemoryTracker(data1, data2)

for i in range(10000):
    for _ in range(random.randint(0, 2)):
        data1.append([random.random() for _ in range(100)])
    for _ in range(random.randint(1, 2)):
        data2.append([random.random() for _ in range(700)])
    mem.getsize(data1, data2)

plt.subplot()
plt.plot(mem.times, mem.sizes)
plt.xlabel('Elapsed time')
plt.ylabel('Memory consumption in %s' % mem.unit)
plt.show()
print('Test')
