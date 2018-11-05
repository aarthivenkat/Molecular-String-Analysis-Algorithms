import os
import sys
input = open(os.path.abspath('../input/rosalind_ba7c.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba7c.txt'), 'w')

text = input.readline().strip()
input.close()

trie = {}

def getSuffixes():
    suffixes = []
    for i, char in enumerate(text):
        suffixes.append((text[i:],str(i)))
    return suffixes

def trieConstruction():
    idx = 0
    root = 0
    for pattern, start in patterns:
        currStart = int(start) - 1
        node = root
        if node not in trie: trie[node] = []
        for j,char in enumerate(pattern):
            symbol = char
            symbolIsEdge = False
            for edge,adj,s in trie[node]:
                if symbol == edge:
                    symbolIsEdge = True
                    node = adj
                    currStart += 1
                    break
            if not symbolIsEdge:
                idx += 1
                trie[idx] = []
                currStart += 1
                trie[node].append((symbol, idx, currStart))
                node = idx
    return

tree = {}
def treeConstruction():
    s = 0
    queue = []
    for tup in trie[s]:
        queue.append((s,tup))

    branchLength = 1
    firstidx = -1
    newBranch = True
    
    while queue:
        startnode,adj = queue.pop(0)
        symbol, endnode, stringidx = adj
        if newBranch: firstidx = stringidx
        
        if len(trie[endnode]) == 1: # if it's a non-branching node
            queue.insert(0, (startnode, trie[endnode][0]))
            branchLength += 1
            newBranch = False
            
        elif len(trie[endnode]) == 0: # if it's a leaf node
            if startnode not in tree: tree[startnode] = []
            tree[startnode].append((firstidx, branchLength))
            newBranch = True
            branchLength = 1
            
        elif len(trie[endnode]) > 1: # if it's a branching node
            if startnode not in tree: tree[startnode] = []
            tree[startnode].append((firstidx, branchLength))
            for adjnode in trie[endnode]: queue.insert(0, (endnode, adjnode))
            newBranch = True
            branchLength = 1

def prefixTrieMatching(text):
    symbol = text[0]
    idx = 0
    v = 0
    pattern = ""
    while True:
        if not trie[v]: return (idx - len(pattern))
        symbolIsEdge = False
        for edge,adj in trie[v]:
            if symbol == edge:
                symbolIsEdge = True
                idx += 1
                symbol = text[idx]
                pattern += symbol
                v = adj
                break
        if not symbolIsEdge:
            return -1

def trieMatching(string):
    j = 0
    while string:
        pos = prefixTrieMatching(string)
        if pos != -1:
            output.write(str(j) + " ")
        string = string[1:]
        j += 1

patterns = getSuffixes()
trieConstruction()
treeConstruction()

for node in tree:
    edges = tree[node]
    for start,length in edges:
        output.write(text[start:start+length] + '\n')
output.close()
