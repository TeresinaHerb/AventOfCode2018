import collections

# First part
file = open('input.txt', 'r')
temp = file.read().strip()
file.close()

codes = list()
for x in temp.split():
    codes.append(x)
    
doublesCount = 0
triplesCount = 0

for code in codes:
    letterCounts = collections.defaultdict(int)
    for c in code:
        letterCounts[c] += 1
    
    tempDouble = 0
    tempTriple = 0
    
    for count in letterCounts:
        if (letterCounts[count] == 2) and (tempDouble == 0):
            doublesCount += 1
            tempDouble += 1
        else:
            if (letterCounts[count] == 3) and (tempTriple == 0):
                triplesCount += 1
                tempTriple += 1
    
checksum = doublesCount * triplesCount

print "Part 1: Codes have " + str(doublesCount) + " doubles and " + str(triplesCount) + " triples, resulting in checksum " + str(checksum)

# Second part
string1 = ""
string2 = ""
x = 0
while x < len(codes)-1:
    string1 = codes[x]
    y = x+1
    while y < len(codes):
        string2 = codes[y]
    
        u = zip(string1,string2)
        nonMatches=[]
        matches = "" 
        for i,j in u:
            if i!=j:
                nonMatches.append(j)
            else:
                matches += j

        if len(nonMatches) == 1:
            print "Part 2: Codes " + string1 + " and " + string2 + " have these letters in common: " + matches
        y += 1
    x += 1
