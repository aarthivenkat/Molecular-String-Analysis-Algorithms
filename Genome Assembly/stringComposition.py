import os
input = open(os.path.abspath('../input/rosalind_ba3a.txt'))

kmersInDNA = []
k = int(input.readline().strip())
text = input.readline().strip()
for i in range(len(text) - k +1):
     currPattern = text[i:i+k]
     if currPattern not in kmersInDNA:
       kmersInDNA.append(currPattern)
print '\n'.join(sorted(kmersInDNA))
