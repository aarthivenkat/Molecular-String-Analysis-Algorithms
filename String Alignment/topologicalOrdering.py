import os
import sys
input = open(os.path.abspath('../input/rosalind_ba5a.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba5a.txt'), 'w')

edgeDict = {}
preDict = {}
path = {}
allNodes = []
for line in input:
    s = int(line.strip().split(' -> ')[0])
    t = [int(item) for item in line.strip().split(' -> ')[1].split(',')]
    if s not in edgeDict: edgeDict[s] = []
    for elem in t:
        if elem not in preDict: preDict[elem] = []
    edgeDict[s].extend(t)
    for elem in t: preDict[elem].append(s)
    allNodes.append(s)
    allNodes.extend(t)

input.close()
allNodes = list(set(allNodes))
candidates = []
for node in allNodes:
    if node not in edgeDict: 
        edgeDict[node] = []
    if node not in preDict:
        preDict[node] = []
        candidates.append(node)
        
topOrder = []
while candidates != []:
    k = candidates[0]
    topOrder.append(k)
    candidates.remove(k)
    temp = edgeDict[k]
    while edgeDict[k] != []:
        node = edgeDict[k][0]
        edgeDict[k].remove(node)
        preDict[node].remove(k)
        if preDict[node] == []: 
            candidates.append(node)
            
output.write(', '.join([str(item) for item in topOrder]))
output.close()
