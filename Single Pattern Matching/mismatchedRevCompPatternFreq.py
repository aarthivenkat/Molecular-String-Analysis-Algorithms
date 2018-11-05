"""
BA1j: Goal: find most frequent kmers with <= d mismatches & reverse complements

For each k-window in line, generate all the neighbors (<= d mismatches).
for each neighbor, increment patternFreq[neighbor].
Repeat the same for line[::-1]. incremement the same patternFreq[neighbor] value.
Output neighbors that maximize patternFreq.

Input: line \n pattern int d
Output: Space-delimited list of k-mers with max frequency and d mismatches.
"""

import os
input = open(os.path.abspath('../input/rosalind_ba1j.txt'))

"""
Returns reverse complement of string
"""
def reverseComplement(line):
    reverse = line[::-1]
    complement = {'A':'T','G':'C','C':'G','T':'A'}
    return ''.join([complement[s] for s in reverse])

"""
Returns hamming distance between two strings
"""
def hammingDistance (p,q):
    hammingDist = 0
    for i,base in enumerate(p.strip()):
        if base != q[i]: hammingDist += 1
    if hammingDist < int(d): return True
    else: return False

"""
Returns all k-mers within hamming distance d of input kmer
"""
def neighbors(kmer,d):
    if int(d) == 0: return [kmer]
    if len(kmer) == 1: return ['A','C','G','T']
    bases = ['A','C','G','T']
    neighborhood = []
    suffixNeighbors = neighbors(kmer[1:],d)
    for neighbor in suffixNeighbors:
        if hammingDistance(kmer[1:],neighbor):
            for base in bases:
                neighborhood.append(base+neighbor)
        else:
            neighborhood.append(kmer[0]+neighbor)
    return neighborhood

"""
Reads input string text and outputs dictionary of k-mers and frequencies
"""
def patternFreqDict(text, pattern):
  for i in range(len(text) - pattern +1):
       currPattern = text[i:i+pattern]
       mismatchedKmers = neighbors(currPattern,d)
       for kmer in mismatchedKmers:
           if kmer in patternFreq: patternFreq[kmer] += 1
           else: patternFreq[kmer] = 1

"""
Reads dictionary of k-mers and outputs those with max frequency
"""
def maxFreqPatterns(freqDict):
  sortedByValue = sorted(((v,k) for k,v in freqDict.iteritems()), reverse=True)
  maxVal = sortedByValue[0][0]
  pattMaxVal = []
  for item in sortedByValue:
    if item[0] == maxVal:
      pattMaxVal.append(item[1])
    
  print ' '.join(pattMaxVal)
       
line,vals = input.readlines()
patt,d = vals.split()
patternFreq = {}
patternFreqDict(line.strip(),int(patt.strip()))
patternFreqDict(reverseComplement(line.strip()),int(patt.strip()))
maxFreqPatterns(patternFreq)
input.close()
