import os
import sys
input = open(os.path.abspath('../input/rosalind_ba3i.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba3i.txt'), 'w')

#GLOBAL VARS
adjDict = {}
degreeDict = {}
stack = []
cycle = []

k = int(input.readline().strip())
input.close()

def allBinaryStrings(interval):
    kmers = [""]
    for c in range(interval):
        currKmers = []
        for item in kmers:
            currKmers.append(item+'0')
            currKmers.append(item+'1')
        kmers = currKmers
    return kmers

def preProcessing(kmers):
    #ADJACENCY LIST
    for patt in kmers:
            adjDict.setdefault(patt[:-1], []).append(patt[1:])
    #DEGREE LIST
    for k,vn in adjDict.iteritems():
        if k not in degreeDict: degreeDict[k] = 0
        degreeDict[k] += 1
        for v in vn:
            if v not in degreeDict: degreeDict[v] = 0
            degreeDict[v] -= 1
    #ANY START VERTEX
    start = k
    return start

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

kmers = allBinaryStrings(k)
current = preProcessing(kmers)
path = eulerianPath(current)
for elem in path[1:]: output.write(elem[-1])
output.close()
