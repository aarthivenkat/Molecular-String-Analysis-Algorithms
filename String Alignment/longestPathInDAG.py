import os
import sys
input = open(os.path.abspath('../input/rosalind_ba4d.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba4d.txt'), 'w')

a = int(input.readline().strip())
b = int(input.readline().strip())
edgeDict = {}
preDict = {}
path = {}
backtrack = {}
allNodes = []
for line in input:
    s = int(line.split('->')[0])
    t = int(line.split('->')[1].split(':')[0])
    e = int(line.split('->')[1].split(':')[1])
    edgeDict[(s,t)] = e
    if t not in preDict: preDict[t] = []
    preDict[t].append(s)
    allNodes.extend([s,t])
input.close()

for node in list(set(allNodes)):
    if node not in preDict: preDict[node] = []
    if node not in path: path[node] = float("-inf")
path[a] = 0

preDict[a] = []
topOrder = []
for k,v in preDict.iteritems():
    if set(v).issubset(topOrder):
        topOrder.append(k)

for num in topOrder:
    for p in preDict[num]:
        if path[p] + edgeDict[(p,num)] > path[num]: 
            path[num] = path[p] + edgeDict[(p,num)]
            backtrack[num] = p

output.write(str(path[b]) + '\n')

bt = [str(b)]
num = b
for x in backtrack:
    if backtrack[num] == a:
        bt.append(str(a))
        break
    bt.append(str(backtrack[num]))
    num = backtrack[num]

output.write('->'.join(bt[::-1]))
output.close()
