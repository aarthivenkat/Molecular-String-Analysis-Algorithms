"""
BA1l: for string of nucleotides, number is calculated by conv(nt)*4**(place).
Analogous to 121 = 100 + 20 + 1 = (1 * 10**2) + (2 * 10**1) + (1 * 10**0)
GG = (2 * 4**1) + (2 * 4**0)

Input: line
Output: number
"""

import os
input = open(os.path.abspath('../input/rosalind_ba1l.txt'))

"""
Converts each nucleotide to number value
"""
def conv(line):
    s = ""
    for char in line:
        if char == 'A': s += "0"
        if char == 'C': s += "1"
        if char == 'G': s += "2"
        if char == 'T': s += "3"
    return s

line = input.readline().strip()
numLine = conv(line)[::-1]
sum = 0
for i,num in enumerate(numLine):
    sum += int(num)*(4**i)
print sum
