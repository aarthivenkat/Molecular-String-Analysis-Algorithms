import os
input = open(os.path.abspath('../input/rosalind_ba3d.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba3d.txt'), 'w')

k = int(input.readline().strip())
text = input.readline().strip()
input.close()

def getUniqueKmers(length):
    kmersInDNA = []
    for i in range(len(text) - length +1):
        currPattern = text[i:i+length]
        if currPattern not in kmersInDNA:
            kmersInDNA.append(currPattern)
    return sorted(kmersInDNA)

def adjacencyList(kmers):
    kmerDict = {}
    for patt1 in kmers:
        for patt2 in kmers:
            if patt1[1:] == patt2[:-1]:
                if (patt1 + patt2[-1]) in patterns:
                    kmerDict.setdefault(patt1, []).append(patt2)
    for s in sorted(kmerDict.keys()):
        output.write(s + " -> " + ','.join(kmerDict[s]) + '\n')

patterns = getUniqueKmers(k)
patterns_1 = getUniqueKmers(k-1)
adjacencyList(patterns_1)
output.close()
