import os
input = open(os.path.abspath('../input/rosalind_ba3f.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba3f.txt'), 'w')

#GLOBAL VARS
adjDict = {}
stack = []
cycle = []

#PREPROCESSING
for line in input:
    v0,to,vn = line.split()
    adjDict[v0] = list(vn.split(','))
input.close()

curr = v0
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