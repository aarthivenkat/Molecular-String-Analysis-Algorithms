import os
input = open(os.path.abspath('../input/rosalind_ba8c.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba8c.txt'), 'w')

def lastToFirst(index):
    character,count = lastcolwithpos[index]
    return firstcol.index((character, count))
    
def bwMatching(pattern):
    top = 0
    bottom = len(lastcolwithpos) - 1
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            currlist = lastcol[top:bottom + 1]
            if symbol in currlist:
                topidx = currlist.index(symbol)
                bottomidx = ''.join(currlist).rfind(symbol)

                prevtop = top
                top = lastToFirst(prevtop + topidx)
                bottom = lastToFirst(prevtop + bottomidx)

            else:
                return 0
        else:
            return bottom - top + 1

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
for p in patterns:
    print bwMatching(p),
    
