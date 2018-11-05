import os
input = open(os.path.abspath('../input/rosalind_ba3b.txt'))

s = input.readline()[:-1]
for line in input:
    s += line.strip()[-1] 
print s