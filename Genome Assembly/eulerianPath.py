import os
import sys
input = open(os.path.abspath('../input/rosalind_ba3g.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba3g.txt'), 'w')

#GLOBAL VARS
adjDict = {}
degreeDict = {}
stack = []
cycle = []

#PREPROCESSING
for line in input:
    v0,to,vn = line.split()
    adjDict[v0] = list(vn.split(','))
    if v0 not in degreeDict: degreeDict[v0] = 0
    for v in list(vn.split(',')):
        if v not in adjDict: adjDict[v] = []
        degreeDict[v0] += 1
        if v not in degreeDict: degreeDict[v] = 0
        degreeDict[v] -= 1
input.close()

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

#FINDING PATH
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
output.write('->'.join(cycle))
output.close()
