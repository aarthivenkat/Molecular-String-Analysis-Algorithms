import os
import sys
input = open(os.path.abspath('../input/rosalind_ba7e.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba7e.txt'), 'w')

text = input.readline().strip()
input.close()
firstStrEnd = text.find('#')

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
            leafnodes.append(endnode)
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
leafnodes = []
treeConstruction()
color = {}
for node in tree:
    edges = tree[node]
    for adj in edges:
        prev,nex,pos,length = adj
        if nex in leafnodes:
            if pos > firstStrEnd: color[nex] = ('red',node)
            else: color[nex] = ('blue',node)

for curr in leafnodes:
    while curr != 0 and curr in color:
        prevnode = color[curr][1]
        allColors = []
        allColored = True
        for adj in tree[prevnode]:
            prev,nex,pos,length = adj
            if nex in color: allColors.append(color[nex][0])
            else: allColored = False
        if allColored:
            if len(list(set(allColors))) == 1: color[prevnode] = (allColors[0],prev)
            else: color[prevnode] = ('purple',prev)
        curr = prevnode
        
purpleNodes = []
allPatterns = []
for node in color:
    if color[node][0] == 'purple': purpleNodes.append(node)

for node in purpleNodes:
    allPatterns.append(backtrack(0,node))
print max(allPatterns, key=len)
output.close()
