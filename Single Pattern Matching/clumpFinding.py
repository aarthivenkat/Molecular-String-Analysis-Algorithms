"""
BA1e: For each L-window, find all the k-mers in that window with >= t frequency.
**Could be faster using BetterClumpFinding method**

Input: line \n int k int L int t
Output: all k-mers that form clumps
"""

import os
input = open(os.path.abspath('../input/rosalind_ba1e.txt'))

"""
Reads input string text and int k and outputs dictionary of k-mers and frequencies
"""
def patternFreqDict(text, pattern):
  patternFreq = {}
  for i in range(len(text) - pattern +1):
       currPattern = text[i:i+pattern]
       if currPattern in patternFreq:
         patternFreq[currPattern] += 1
       else: patternFreq[currPattern] = 1
  return patternFreq

"""
Reads dictionary of k-mers and outputs those with >= t frequency
"""
def tFreqPatterns(freqDict, t):
  sortedByValue = sorted(((v,k) for k,v in freqDict.iteritems()), reverse=True)
  for item in sortedByValue:
    if item[0] >= t and item[1] not in pattTVal:
      pattTVal.append(item[1])
       
line,var = input.readlines()
line = line.strip()
k,L,t = var.split()
pattTVal = []

"""
For each L-length window, create kmer dictionary, output those with >= t frequency
"""
for i in range(len(line) - int(L) +1):
    interval = line[i:i+int(L)]
    d = patternFreqDict(interval,int(k))
    tFreqPatterns(d, int(t))
print ' '.join(pattTVal)
