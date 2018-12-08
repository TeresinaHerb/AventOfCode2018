import numpy as np
from scipy.spatial.distance import cdist



area = np.loadtxt('test.txt', dtype = 'int', delimiter = ',')
size = area.shape

# construct second array
min_0 = min(area[:, 0])
max_0 = max(area[:, 0])
min_1 = min(area[:, 1])
max_1 = max(area[:, 1])

dim = (max_0-min_0+1) * (max_1-min_1+1)

comp = np.zeros(shape=(dim,2))
n = 0
i = min_0
j = min_1
while i < max_0+1:
    j = min_1
    while j < max_1+1:
        comp[n] = [i,j]
        n += 1
        j += 1
    i += 1

out = cdist(area, comp, metric = 'cityblock')

res = np.zeros(shape = (max_0, max_1))

i = 0
k = 0
while i < max_0:
    j = 0
    while j < max_1:
        temp = np.argsort(out[:, k])
        ind = np.argmin(out[:, k])
        if out[temp[0], k] != out[temp[1], k]:
            res[i, j] = ind
        else:
            res[i, j] = 99
        k += 1
        j += 1
    i += 1

res = np.transpose(res)
print(res)

# find finite areas
row = list()
col = list()
ref = list()
finite = set(row).symmetric_difference(set(ref))
