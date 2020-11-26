import os
import matplotlib.pyplot as plt
import numpy as np

a = []
with open('/storage/timm/output/train/20201126-010303-tf_efficientnet_b8-672/summary.csv', 'r') as f:
    lines = f.read().splitlines()[1:]
    for line in lines:
        a.append([float(x) for x in line.split(',')])

a = np.array(a).transpose((1,0))
print(a)

fig = plt.figure()

plt.plot(a[1] / np.max(a[1]), label='training loss')
plt.plot(a[3]/100, label='eval acc')
plt.legend()
plt.savefig('/storage/plot.png')