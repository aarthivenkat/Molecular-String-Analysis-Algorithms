"""
BA1n: Return neighbors of given pattern, defined by distance d
Recursively call on suffix of pattern.
If hamming distance bt suffix and pattern is <d, add any nt. If not, only add prefix.

Input: pattern \n d
Output: Newline-delimited list of neighbors
"""

import os
input = open(os.path.abspath('../input/rosalind_ba1n.txt'))

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
    print suffixNeighbors
    for neighbor in suffixNeighbors:
        if hammingDistance(kmer[1:],neighbor,d):
            for base in bases:
                neighborhood.append(base+neighbor)
        else:
            neighborhood.append(kmer[0]+neighbor)
    return neighborhood

pattern,d = input.readlines()
n = neighbors(pattern.strip(),int(d.strip()))
#print '\n'.join(n)
input.close()
