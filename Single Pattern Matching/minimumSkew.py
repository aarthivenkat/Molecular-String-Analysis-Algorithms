"""
BA1f: Find the indices where skew is the lowest in the whole string.

Input: line
Output: Space-delimited list of indices
"""

import os
input = open(os.path.abspath('../input/rosalind_ba1f.txt'))

text = input.readline().strip()
skew = 0
rollingSkew = [0]
for c in text:
    if c == 'C': skew -= 1
    if c == 'G': skew += 1
    rollingSkew.append(skew)

minSkew = min(rollingSkew)
minIndices = [str(i) for i,skew in enumerate(rollingSkew) if skew == minSkew]
print ' '.join(minIndices)

input.close()
