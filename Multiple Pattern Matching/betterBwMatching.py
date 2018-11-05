import os
input = open(os.path.abspath('../input/rosalind_ba8d.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba8d.txt'), 'w')

def lastToFirst(index):
    character,count = lastcolwithpos[index]
    return firstcol.index((character, count))
    
def firstOccurence():
    ch = ''
    firstOccurences = {}
    for i,character in enumerate(firstcol):
        if character[0] != ch:
            firstOccurences[character[0]] = i
            ch = character[0]
    return firstOccurences

def countMatrix():
    countmatrix = {'A':[0],'C':[0],'G':[0],'T':[0],'$':[0]}
    for i,character in enumerate(lastcol):
        for option in countmatrix:
            prevcount = countmatrix[option][-1]
            if character == option: countmatrix[character].append(prevcount + 1)
            else: countmatrix[option].append(prevcount)
    return countmatrix
    
def bwMatching(pattern):
    top = 0
    bottom = len(lastcolwithpos) - 1
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            currlist = lastcol[top:bottom + 1]

            if symbol in currlist:
                top = firstoccurences[symbol] + countmatrix[symbol][top]
                bottom = firstoccurences[symbol] + countmatrix[symbol][bottom + 1] - 1

            else: return str(0)
        else: return top,bottom

inputstring = input.readline().strip()
patterns = input.readline().strip().split(' ')
input.close()

lastcol = list(inputstring)
countdict = {'A':0, 'C':0, 'G':0, 'T':0, '$':0}
lastcolwithpos = []

for i,letter in enumerate(lastcol):
    countdict[letter] += 1
    lastcolwithpos.append((lastcol[i], countdict[letter]))
    
firstcol = sorted(lastcolwithpos)
firstoccurences = firstOccurence()
countmatrix = countMatrix()

for p in patterns:
    print bwMatching(p)
output.close()
