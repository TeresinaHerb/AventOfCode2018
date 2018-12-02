startFreq = 0
currentFreq = startFreq

file = open('input.txt', 'r')
temp = file.read().strip()
file.close()

frequencies = list()
for x in temp.split():
    frequencies.append(int(x))

# part 1
for frequency in frequencies:
    currentFreq = currentFreq + frequency
    
print "Part 1: Resulting final frequency " + str(currentFreq)

# part 2

collectFreq = list()
collectFreq.append(startFreq)

# list with duplicate items
duplicateFreq = list()

while len(duplicateFreq) < 1:
    for frequency in frequencies:
        newFreq = collectFreq[-1]+frequency
        if newFreq in collectFreq:
            duplicateFreq.append(newFreq)
            break
        collectFreq.append(newFreq)
        
print "Part 2: First duplicate frequency " + str(duplicateFreq[0])
