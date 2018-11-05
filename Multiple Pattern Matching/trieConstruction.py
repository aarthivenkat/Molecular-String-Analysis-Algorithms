import os
import sys
input = open(os.path.abspath('../input/rosalind_ba7a.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba7a.txt'), 'w')

patterns = [line.strip() for line in input.readlines()]
input.close()

trie = {}

def trieConstruction():
    idx = 0
    root = 0
    for pattern in patterns:
        node = root
        if node not in trie: trie[node] = []
        for char in pattern:               
            symbol = char
            symbolIsEdge = False
            for edge,adj in trie[node]:
                if symbol == edge:
                    symbolIsEdge = True
                    node = adj
                    break
            if not symbolIsEdge:
                idx += 1
                trie[idx] = []
                trie[node].append((symbol, idx))
                node = idx
    return
    
trieConstruction()
for node in trie:
    adjNodes = trie[node]
    for adjNode in adjNodes:
        output.write("%d->%d:%s\n" %(node, adjNode[1], adjNode[0]))
output.close()
