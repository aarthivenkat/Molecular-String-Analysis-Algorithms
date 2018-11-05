import os
input = open(os.path.abspath('../input/rosalind_ba3c.txt'))

kmerDict = {}
kmers = input.readlines()

for patt1 in kmers:
    for patt2 in kmers:
        if patt1.strip()[1:] == patt2.strip()[:-1]:
            kmerDict.setdefault(patt1.strip(), []).append(patt2.strip())
for s in kmerDict.keys():
    for e in kmerDict[s]:
        print s + " -> " + e
