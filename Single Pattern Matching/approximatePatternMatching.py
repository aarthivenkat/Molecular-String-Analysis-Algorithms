"""
BA1h: Given string, search in k-length windows for approximate pattern. If found, add to list.
Approximate pattern = Hamming distance <= d.

Input: pattern \n line \n int d
Output: start positions of all approximate patterns in line
"""

import os
input = open(os.path.abspath('../input/rosalind_ba1h.txt'))

"""
Returns True if hamming distance between two strings <= d
"""
def hammingDistance (p,q):
    hammingDist = 0
    for i,base in enumerate(p.strip()):
        if base != q[i]: hammingDist += 1
    if hammingDist <= int(d): return True
    else: return False
    
"""
Iterates one base at a time, searching in len(pattern) intervals for pattern.
Appends position to list of approximate pattern found.
"""
def patternCount(text,pattern):
    patternPositions = []
    for i in range(len(text) - len(pattern) +1):
        if hammingDistance(pattern, text[i:i+len(pattern)]):
            patternPositions.append(str(i))
    return ' '.join(patternPositions)

patt,line,d = input.readlines()
print patternCount(line.strip(),patt.strip())
input.close()
