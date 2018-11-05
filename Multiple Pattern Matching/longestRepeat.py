import os
import sys
input = open(os.path.abspath('../input/rosalind_ba7d.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba7d.txt'), 'w')

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
        queue.append((s,-1,0,tup))

    branchLength = 1
    firstidx = -1
    newBranch = True
    while queue:
        startnode,prevnode, endnode, adj = queue.pop(0)
        symbol, endnode, stringidx = adj
        if newBranch:
            firstidx = stringidx
        
        if len(trie[endnode]) == 1: # if it's a non-branching node
            queue.insert(0, (startnode, prevnode, endnode, trie[endnode][0]))
            branchLength += 1
            newBranch = False
            
        elif len(trie[endnode]) == 0: # if it's a leaf node
            if startnode not in tree: tree[startnode] = []
            tree[startnode].append((prevnode, endnode, firstidx, branchLength))
            newBranch = True
            branchLength = 1
            
        elif len(trie[endnode]) > 1: # if it's a branching node
            if startnode not in tree: tree[startnode] = []
            tree[startnode].append((prevnode, endnode, firstidx, branchLength))
            for adjnode in trie[endnode]: queue.insert(0,(endnode, startnode, endnode, adjnode))
            newBranch = True
            branchLength = 1
                   
def backtrack(start,end):
    pattern = ""
    currnode = end
    edges = tree[currnode]
    prevnode = edges[0][0] # where I stored prev
    while currnode != 0:
        for adj in tree[prevnode]:
            above,below,pos,length = adj
            if below == currnode:
                pattern = text[pos:pos+length] + pattern
                currnode = prevnode
                prevnode = tree[currnode][0][0]
                break
                
    return pattern

patterns = getSuffixes()
trieConstruction()
treeConstruction()

nodesWithChildren = []
allPatterns = []
for node in tree:
    if len(tree[node]) > 1 and node != 0: nodesWithChildren.append(node)

for node in nodesWithChildren:
    allPatterns.append(backtrack(0,node))
print max(allPatterns, key=len)
output.close()
