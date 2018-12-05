import collections
import numpy
import re

# First part
claims = [claim.rstrip('\n') for claim in open('test.txt')]
fabric = collections.defaultdict(int)

for claim in claims:
    temp = re.split(' |@|,|:|x', claim)
    left = int(temp[3])
    top = int(temp[4])
    incL = int(temp[6])
    incT = int(temp[7])
    left_e = left + incL
    top_e = top + incT
    while left < left_e:
        top = int(temp[4])
        while top < top_e:
            fabric[left, top]
            fabric[left, top] += 1
            top +=1
        left +=1

results = fabric.values()
counter = 0
for res in results:
    if res > 1:
        counter += 1
print ("Part 1: Overlapping claims: " + str(counter))


#Second part
fabric = collections.defaultdict(list)
for claim in claims:
    temp = re.split(' |@|,|:|x', claim)
    left = int(temp[3])
    top = int(temp[4])
    incL = int(temp[6])
    incT = int(temp[7])
    left_e = left + incL
    top_e = top + incT
    while left < left_e:
        top = int(temp[4])
        while top < top_e:
            fabric[left, top].append(claim)
            top +=1
        left +=1

# delete all entries from dict with one entry
for k, v in fabric.items():
    if len(v) == 1:
         del fabric[k]

# check which value cannot be found in dict --> slice
data = fabric.values()
for claim in claims:
    noOver = False
    test = claim
    print (test)
    for sublist in data:
        res = test in sublist
        if res == True:
            print noOver
            break
        else:
            noOver = True
    if noOver == True:
        print ("Part 2: " + str(test))