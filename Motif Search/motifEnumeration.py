"""
BA2a: Find all (k,d)-motifs in collection of strings
Input: k d\n string1 \n string2 \n...
Output: kmer1 kmer2 ...
"""

import os
input = open(os.path.abspath('../input/rosalind_ba2a.txt'))

"""
Reads input string text and outputs list of k-mers
"""
def patterns(text, k):
  for i in range(len(text) - k +1):
       currPattern = text[i:i+k]
       if currPattern in kmersInDNA:
         kmersInDNA[currPattern] += 1
       else: kmersInDNA[currPattern] = 1

"""
Returns hamming distance between two strings
"""
def hammingDistance (p,q,d):
    hammingDist = 0
    for i,base in enumerate(p.strip()):
        if base != q[i]: hammingDist += 1
    if hammingDist < d: return True
    else: return False

"""
Returns all k-mers within hamming distance d of input kmer
"""
def neighbors(kmer,d):
    if d == 0: return [kmer]
    if len(kmer) == 1: return ['A','C','G','T']
    bases = ['A','C','G','T']
    neighborhood = []
    suffixNeighbors = neighbors(kmer[1:],d)
    for neighbor in suffixNeighbors:
        if hammingDistance(kmer[1:],neighbor,d):
            for base in bases:
                neighborhood.append(base+neighbor)
        else:
            neighborhood.append(kmer[0]+neighbor)
    return neighborhood

vals = input.readlines()
k = int(vals[0].split()[0])
d = int(vals[0].split()[1])
vals = vals[1:]

output = []
kmersInDNA = {}
for dna in vals:
    patterns(dna.strip(),k)
for pattern in kmersInDNA.keys():
    for otherPattern in (neighbors(pattern,d)):
        count = 0
        for text in vals:
            currCount = 0
            for i in range(len(text.strip()) - k +1):
                currPattern = text.strip()[i:i+k]
                if hammingDistance(otherPattern, currPattern, d+1):
                    currCount += 1
            if currCount >= 1: count += 1
        if count == len(vals):
            output.append(otherPattern)

print ' '.join(list(set(output)))        
