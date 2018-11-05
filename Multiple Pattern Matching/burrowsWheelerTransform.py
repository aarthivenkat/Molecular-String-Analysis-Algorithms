import sys
import os
input = open(os.path.abspath('../input/rosalind_ba7i.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba7i.txt'), 'w')

text = input.readline().strip()
input.close()

def getSuffixes():
    suffixes = []
    for i, char in enumerate(text):
        suffixes.append(text[i:]+' '+str(i))
    return suffixes

patterns = sorted(getSuffixes())
patterns = [int(item.split()[1]) for item in patterns]
transform = []
for pos in patterns:
    currText = text[pos:] + text[:pos]
    transform.append(currText[-1:])
    
print ''.join(transform)
    
output.close()
