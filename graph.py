import matplotlib.pyplot as plt
import numpy as np
from contestant import Contestant

scientist = Contestant(100000)
rawContestant = scientist.play()
labels = ["swap wins / runs","stay wins / runs"] 
winsData = []
runsData = []
width = 0.3
for ind, tup in enumerate(rawContestant):
    label, data = tup
    if ind % 2 == 0:
        runsData.append(data)
    else:
        winsData.append(data)
plt.xticks(np.arange(len(winsData)) + width/2, labels)
plt.title('Ratio of wins to loses \n depending on whether door is changed')
plt.bar(np.arange(len(runsData)), runsData, width=width)
plt.bar(np.arange(len(winsData)) + width, winsData, width=width)
plt.show()

