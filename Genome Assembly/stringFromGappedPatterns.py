import os
import sys
input = open(os.path.abspath('../input/rosalind_ba3l.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba3l.txt'), 'w')

k,d = [int(i) for i in input.readline().split()]
text = input.readlines()
input.close()

def getFinalString(kmers):
    prefPath = kmers[0].strip().split('|')[0]
    suffPath = kmers[0].strip().split('|')[1]
    for pair in kmers[1:]:
            patt1,patt2 = pair.strip().split('|')
            prefPath += patt1[-1]
            suffPath += patt2[-1]
    return prefPath[:k+d] + suffPath

output.write(getFinalString(text))
output.close()
