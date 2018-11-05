"""
BA2h: Solves double minimization problem for median string
"""

import os
input = open(os.path.abspath('../input/rosalind_ba2h.txt'))

"""
Returns hamming distance between two strings
"""
def hammingDistance (p,q):
    hammingDist = 0
    for i,base in enumerate(p.strip()):
        if base != q[i]: hammingDist += 1
    return hammingDist  
    
vals = input.readlines()
kmer = vals[0].strip()
dnaCollection = vals[1].split()

kmerDist = 0
for text in dnaCollection:
    textDist = float("inf")
    for i in range(len(text) - len(kmer) +1):
            window = text[i:i+len(kmer)]
            if hammingDistance(window,kmer) < textDist:
                textDist = hammingDistance(window,kmer)
    kmerDist += textDist
print kmerDist
