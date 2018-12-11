import numpy as np
import re
from PIL import Image

with open('test.txt') as f:
    temp = f.readlines()

rows = len(temp)
base = np.zeros(shape=(rows,4))

i = 0
for t in temp:
    str1 = re.split('<|>|, ', t)
    base[i, 0] = int(str1[1])
    base[i, 1] = int(str1[2])
    base[i, 2] = int(str1[4])
    base[i, 3] = int(str1[5])
    i +=1

min_x = min(base[:,0])
max_x = max(base[:,0])
min_y = min(base[:,1])
max_y = max(base[:,1])
dim_x = int(max_x-min_x+1)
dim_y = int(max_y-min_y+1)

n = 0
while n < 4:
    base_temp = np.zeros(shape=(rows,2))
    k = 0
    while k < rows:
        ind_x = int((base[k, 0]-min_x)+n*base[k, 2])
        ind_y = int((base[k, 1]-min_y)+n*base[k, 3])
        base_temp[k, 0] = ind_x
        base_temp[k, 1] = ind_y
        k += 1

    min_xt = min(base_temp[:,0])
    max_xt = max(base_temp[:,0])
    min_yt = min(base_temp[:,1])
    max_yt = max(base_temp[:,1])
    dim_xt = int(max_xt-min_xt+1)
    dim_yt = int(max_yt-min_yt+1)

    pic = np.zeros((dim_xt, dim_yt))
    m = 0
    while m < rows:
        pic[int(base_temp[m, 0]-min_xt), int(base_temp[m, 1]-min_yt)] = 1
        m += 1

    pic = pic.transpose()
    #fileN = 'test' + str(n) + '.txt'
    #np.savetxt(fileN, pic, fmt='%d')
    img = Image.new('1', (dim_yt, dim_xt))
    img.putdata(pic)
    img.save('my.png')
    n += 1
