"""
BA1a: For each k-window of text, if the k-window matches the pattern,
incremement pattern count.

Input: full line \n short k-mer pattern
Output: pattern frequency
"""

import os
input = open(os.path.abspath('../input/rosalind_ba1a.txt'))

def patternCount(text,pattern):
    count = 0
    for i in range(len(text) - len(pattern) +1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

line,patt = input.readlines()
print patternCount(line.strip(),patt.strip())
input.close()