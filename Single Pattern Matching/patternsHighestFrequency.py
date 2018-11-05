"""
BA1b: Create dictionary of all kmers and their frequency by reading through text.
Iterate through dictionary to find kmers with max frequency.

Input: full line \n int k
Output: kmers with max frequency
"""

import os
input = open(os.path.abspath('../input/rosalind_ba1b.txt'))

"""
Reads input string text and outputs dictionary of k-mers and frequencies
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
       
line,patt = input.readlines()
d = patternFreqDict(line.strip(),int(patt.strip()))
maxFreqPatterns(d)

  
  
