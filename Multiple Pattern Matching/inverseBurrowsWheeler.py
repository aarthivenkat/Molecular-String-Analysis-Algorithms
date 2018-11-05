import os
input = open(os.path.abspath('../input/rosalind_ba8b.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba8b.txt'), 'w')

inputstring = input.readline().strip()
input.close()

lastcol = list(inputstring)
countdict = {'A':0, 'C':0, 'G':0, 'T':0, '$':0}
lastcolwithpos = []

for i,letter in enumerate(lastcol):
    countdict[letter] += 1
    lastcolwithpos.append((lastcol[i], countdict[letter]))
    
firstcol = sorted(lastcolwithpos)

finalstring = ""
start = ('$', 1)
lastcolindex = lastcolwithpos.index(start)

curr = firstcol[lastcolindex]
finalstring += curr[0]
while curr != start:
    lastcolindex = lastcolwithpos.index(curr)
    curr = firstcol[lastcolindex]
    finalstring += curr[0]

print finalstring
