"""
BA1m: Number to pattern.
Follows the logic:
(12,3): starting with 12
12 % 4 = 0 = A
12 / 4 = 3 % 4 = G
3 / 4 = 0 % 4 = A
reverseString = AGA
string = AGA
Output AGA

Input: number
Output: string
"""

import os
input = open(os.path.abspath('../input/rosalind_ba1m.txt'))
conv = {0:'A',1:'C',2:'G',3:'T'}

index,k = input.readlines()
index = int(index.strip())
k = int(k.strip())
s = ""
currVal = index

for i in range(k):
    s += conv[currVal % 4]
    currVal = currVal/4
print s[::-1]
input.close()