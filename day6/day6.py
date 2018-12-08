import numpy as np
from scipy.spatial.distance import cdist



area = np.loadtxt('input.txt', dtype = 'int', delimiter = ',')
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


i_end = max_0-min_0+1
j_end = max_1-min_1+1
res = np.zeros(shape = (i_end, j_end))

i = 0
i_end = max_0-min_0+1
j_end = max_1-min_1+1
k = 0
while i < i_end:
    j = 0
    while j < j_end:
        temp = np.argsort(out[:, k])
        ind = np.argmin(out[:, k])
        if out[temp[0], k] != out[temp[1], k]:
            res[i, j] = ind
        else:
            res[i, j] = 99
        k += 1
        j += 1
    i += 1

#print(res)

# find finite areas

finite = list()
for n in np.arange(0, size[0]-1, 1):
    finite.append(n)

i = 0
while i < i_end:
    j = 0
    while j < j_end:
        if i == 0 or j == 0 or i == i_end-1 or j ==j_end-1:
            if finite.count(res[i,j]) > 0:
                finite.remove(res[i,j])
        j += 1
    i += 1

unique, counts = np.unique(res, return_counts=True)
count = dict(zip(unique, counts))

print(count)
print(finite)

res2 = dict()
for fin in finite:
    res2[fin] = count[fin]

max_area = max(res2.values())

print (max_area)
