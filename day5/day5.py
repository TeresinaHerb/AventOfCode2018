import re
import collections

# First part
file = open('input.txt', 'r')
polymer = file.read().strip()
file.close()

def poly(polymer):
    i = 0
    while i < len(polymer)-1:
        if (polymer[i].lower() == polymer[i+1].lower()) and (polymer[i] != polymer[i+1]):
            polymer = polymer[:i] + polymer[i+2:]
            i = i-1
            if i < 1:
                i = 0
        else:
            i += 1
    return len(polymer)


res = poly(polymer)
print("Part 1: length of the resulting polymer is " + str(res))

options = collections.defaultdict(int)
#Part 2
from string import ascii_lowercase
for c in ascii_lowercase:
    test = re.compile(re.escape(c), re.IGNORECASE)
    temp = test.sub('', polymer)
    #temp = re.sub(c, '', polymer)
    res = poly(temp)
    #options[c]
    options[c] = res

#print (options.values())
min_opt = min(options.values())
print (min_opt)

for k,v in options.items():
    if v == min_opt:
        res = k

print (res)
