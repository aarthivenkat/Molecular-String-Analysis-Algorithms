"""
BA2b: Solve equivalent motif finding problem by finding median string.
Input: k \n string1 \n string2...
Output: one kmer that acts as median
"""

import os
input = open(os.path.abspath('../input/rosalind_ba2b.txt'))

"""
Return list of all combinations of length interval string.
E.g. interval = 1 return [A,C,G,T]
"""
def allCombinations(interval):
    kmers = [""]
    for c in range(interval):
        currKmers = []
        for item in kmers:
            currKmers.append(item+'A')
            currKmers.append(item+'C')
            currKmers.append(item+'G')
            currKmers.append(item+'T')
        kmers = currKmers
    return kmers

"""
Returns hamming distance between two strings
"""
def hammingDistance (p,q):
    hammingDist = 0
    for i,base in enumerate(p.strip()):
        if base != q[i]: hammingDist += 1
    return hammingDist  
    
vals = input.readlines()
k = int(vals[0].strip())
dnaCollection = vals[1:]

medianDist = float("inf")
median = ""

for kmer in allCombinations(k):
    kmerDist = 0
    for text in dnaCollection:
        textDist = float("inf")
        for i in range(len(text.strip()) - k +1):
                window = text.strip()[i:i+k]
                if hammingDistance(window,kmer) < textDist:
                    textDist = hammingDistance(window,kmer)
        kmerDist += textDist
    if kmerDist < medianDist:
        medianDist = kmerDist
        median = kmer
print median
