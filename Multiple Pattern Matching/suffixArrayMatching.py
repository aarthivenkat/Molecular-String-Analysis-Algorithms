import sys
import os
input = open(os.path.abspath('../input/rosalind_ba7h.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba7h.txt'), 'w')

text = input.readline().strip()
patterns = [line.strip() for line in input.readlines()]
input.close()

def getSuffixes():
    suffixes = []
    for i, char in enumerate(text):
        suffixes.append(text[i:]+' '+str(i))
    return suffixes
    
def binarySearch(item):
    minidx = 0
    maxidx = len(text) - 1
    while minidx <= maxidx:
        #print minidx, maxidx
        mididx = (minidx + maxidx) / 2
        #print minidx,maxidx
        #print item, text[suffixArray[mididx] : (suffixArray[mididx] + len(item))]
        if item > text[suffixArray[mididx] : (suffixArray[mididx] + len(item))]: minidx += 1
        else: maxidx = mididx - 1

    #if item == text[suffixArray[mididx]: (suffixArray[mididx] + len(item))]:
    first = minidx
        
    minidx = first
    maxidx = len(text) - 1
    while minidx <= maxidx:
        mididx = (minidx + maxidx) / 2
        if item == text[suffixArray[mididx]: suffixArray[mididx] + len(item)]:
            minidx += 1
        else:
            maxidx = mididx - 1
    last = maxidx
    print first,last
    return suffixArray[first:last+1]

suffixes = sorted(getSuffixes())
suffixArray = [int(item.split()[1]) for item in suffixes]
positions = []
for pattern in patterns:
    positions.extend( binarySearch(pattern) )
output.write(' '.join([str(i) for i in positions]))
output.close()

