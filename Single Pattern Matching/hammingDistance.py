"""
BA1g: Given two strings, find number of mismatches.

Input: string \n string
Output: hamming distance
"""

import os
input = open(os.path.abspath('../input/rosalind_ba1g.txt'))

p,q = input.readlines()
hammingDist = 0
for i,base in enumerate(p.strip()):
    if base != q[i]: hammingDist += 1
print hammingDist
input.close()