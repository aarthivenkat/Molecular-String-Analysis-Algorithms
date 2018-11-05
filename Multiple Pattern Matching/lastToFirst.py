import os
input = open(os.path.abspath('../input/rosalind_ba8a.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba8a.txt'), 'w')

inputstring = input.readline().strip()
index = int(input.readline().strip())
input.close()

lastcol = list(inputstring)
countdict = {'A':0, 'C':0, 'G':0, 'T':0, '$':0}
lastcolwithpos = []
for i,letter in enumerate(lastcol):
    countdict[letter] += 1
    lastcolwithpos.append((lastcol[i], countdict[letter]))
    
firstcol = sorted(lastcolwithpos)

def lastToFirst(first, last):
    character,count = last[index]
    return first.index((character, count))

print lastToFirst(firstcol,lastcolwithpos)
