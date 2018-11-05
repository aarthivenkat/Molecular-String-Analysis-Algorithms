"""
BA1c: Print reverse complement of line.

Input: line
Output: line, reverse complement
"""

import os
input = open(os.path.abspath('../input/rosalind_ba1c.txt'))

line = input.readline().strip()
reverse = line[::-1] #this is a fast way to reverse a line
complement = {'A':'T','G':'C','C':'G','T':'A'}
print ''.join([complement[s] for s in reverse])
