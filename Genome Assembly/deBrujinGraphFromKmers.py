import os
input = open(os.path.abspath('../input/rosalind_ba3e.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba3e.txt'), 'w')

text = input.readlines()
input.close()

def adjacencyList(kmers):
    kmerDict = {}
    for patt in kmers:
            kmerDict.setdefault(patt.strip()[:-1], []).append(patt.strip()[1:])
    for s in sorted(kmerDict.keys()):
        output.write(s + " -> " + ','.join(kmerDict[s]) + '\n')

adjacencyList(text)
output.close()
