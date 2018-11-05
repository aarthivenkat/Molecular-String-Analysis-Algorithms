import sys
import os
input = open(os.path.abspath('../input/rosalind_ba8e.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba8e.txt'), 'w')

text = input.readline().strip() + '$'
patterns = [x.strip() for x in input.readlines()]
patterns = [ 'ATCG' ]
K = 5
input.close()

def transform():
    suffixes = []
    for i, char in enumerate(text):
        suffixes.append(text[i:]+' '+str(i))
    
    patterns = sorted(suffixes)
    patterns = [int(item.split()[1]) for item in patterns]
    transform = []
    for pos in patterns:
        currText = text[pos:] + text[:pos]
        transform.append(currText[-1:])
    
    return ''.join(transform), patterns
    
def firstOccurence(firstcol):
    ch = ''
    firstOccurences = {}
    for i,character in enumerate(firstcol):
        if character[0] != ch:
            firstOccurences[character[0]] = i
            ch = character[0]
    return firstOccurences

def countMatrix(lastcol):
    countmatrix = {'A':[0],'C':[0],'G':[0],'T':[0],'$':[0]}
    for i,character in enumerate(lastcol):
        for option in countmatrix:
            prevcount = countmatrix[option][-1]
            if character == option: countmatrix[character].append(prevcount + 1)
            else: countmatrix[option].append(prevcount)
    return countmatrix

def partialMatrix(matrix):
    for character in matrix:
        l = matrix[character]
        matrix[character] = l[::K]
    print matrix
    return matrix
    
def partialArray(array):
    partial = []
    for i, elem in enumerate(array):
        if elem % K == 0: partial.append((i,elem))
    return partial

def iteratePartial(partial, top, bottom):
    diff = bottom - top + 1
    partialpos = []
    for j in range(top, bottom + 1):
        count = 0
        while j not in [x for x,y in partial]:
            lastsymboltup = lastcolwithpos[j]
            j = sorted(lastcolwithpos).index(lastsymboltup)
            count += 1

        for x,y in partial:
            if x == j:
                partialpos.append(y + count)
                break
    return partialpos

def bwMatching(pattern):
    top = 0
    bottom = len(lastcolwithpos) - 1
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            currlist = lastcol[top:bottom + 1]
            if symbol in currlist:
                diff = top % K
                maptop = int(top/K)
                topcount = partialmatrix[symbol][maptop]
                for i in range(diff):
                    print topcount
                    if lastcol[(maptop*K) + i] == symbol: topcount += 1
                    
                diff = (bottom + 1) % K
                mapbottom = int((bottom+1)/K)
                bottomcount = partialmatrix[symbol][mapbottom]
                for i in range(diff):
                    if lastcol[(mapbottom*K) + i] == symbol: bottomcount += 1
                
                top = firstoccurences[symbol] + topcount
                bottom = firstoccurences[symbol] + bottomcount - 1
            else:
                return ''
        else:
            return iteratePartial(partial,top,bottom)

bwt,array = transform()
partial = partialArray(array)
del array

lastcol = list(bwt)
countdict = {'A':0, 'C':0, 'G':0, 'T':0, '$':0}
lastcolwithpos = []
for i,letter in enumerate(lastcol):
    countdict[letter] += 1
    lastcolwithpos.append((lastcol[i], countdict[letter]))

firstoccurences = firstOccurence(sorted(lastcolwithpos))
countmatrix = countMatrix(lastcol)
partialmatrix = partialMatrix(dict(countmatrix))
del countmatrix

outputs = []
for p in patterns:
    for x in bwMatching(p):
        if x == '': continue
        outputs.append(str(x))
for y in sorted(outputs):
    output.write(y + ' ')
output.close()
