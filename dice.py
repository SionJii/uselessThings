import random
import matplotlib.pyplot as plt
import numpy as np

listS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for _ in range(10000):
    a = random.randrange(1, 7)
    b = random.randrange(1, 7)
    listS[a+b-2] += 1

print(listS)

for i in range(len(listS)):
    print(i+2, '나온 횟수:', listS[i])

x = np.arange(11)
years = ['2018', '2019', '2020']
values = [100, 400, 900]

plt.bar(x, listS)
plt.xticks(x, range(11)+1)

plt.show()
