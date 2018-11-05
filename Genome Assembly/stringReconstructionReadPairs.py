import os
import sys
input = open(os.path.abspath('../input/rosalind_ba3j.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba3j.txt'), 'w')

#GLOBAL VARS
adjDict = {}
degreeDict = {}
stack = []
cycle = []

k,d = [int(i) for i in input.readline().split()]
text = input.readlines()
input.close()

def preProcessing(kmers):
    #ADJACENCY LIST
    for pair in kmers:
            patt1,patt2 = pair.strip().split('|')
            key = (patt1[:-1],patt2[:-1])
            val = (patt1[1:],patt2[1:])
            adjDict.setdefault(key, []).append(val)
    #DEGREE LIST
    for k,vn in adjDict.iteritems():
        if k not in degreeDict: degreeDict[k] = 0
        degreeDict[k] += len(vn)
        for v in vn:
            if v not in degreeDict: degreeDict[v] = 0
            degreeDict[v] -= 1
    #GET START VERTEX
    s = 0
    t = 0
    for k,v in degreeDict.iteritems():
        if v > 0:
            s += 1
            curr = k
        if v < 0:
            t += 1
    if s != 1 and t != 1: sys.exit("Eulerian path doesn't exist")
    return curr

def eulerianPath(curr):
    while True:
        if adjDict[curr]:
            stack.append(curr)
            neighbor = adjDict[curr].pop(0)
            curr = neighbor
        else:
            cycle.append(curr)
            curr = stack.pop()
        if all([a == [] for a in adjDict.values()]):
            break
    cycle.append(curr)
    while stack:
        cycle.append(stack.pop())
    cycle.reverse()
    return cycle

current = preProcessing(text)
path = eulerianPath(current)
prefPath = path[0][0]
suffPath = path[0][1]
for elem in path[1:]:
    prefPath += elem[0][-1]
    suffPath += elem[1][-1]
print prefPath
print suffPath
print prefPath[:k+d]
print suffPath[len(suffPath)-k-d:]
finPath = prefPath[:k+d] + suffPath[len(suffPath)-k-d:]
output.write(finPath)
output.close()
