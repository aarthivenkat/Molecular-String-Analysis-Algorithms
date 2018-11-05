import os
import sys
input = open(os.path.abspath('../input/rosalind_ba6c.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba6c.txt'), 'w')

p = input.readline().strip()
p = ''.join(p.split("(")).split(")")[:-1]

q = input.readline().strip()
q = ''.join(q.split("(")).split(")")[:-1]

def getColoredEdges(x):
    def format(list):
        newList = ["%d" %elem for elem in list]
        return "(" + ' '.join(newList) + ")\n"
    
    def chrToCycle(list):
        y = []
        for elem in list:
            if elem > 0:
                y.extend([(2*elem) - 1, (2*elem)])
            else:
                y.extend([(-2*elem), (-2*elem) - 1])
        return y
        
    edges = []
    for chr in x:
        blocks = [int(elem) for elem in chr.split()]
        nodes = chrToCycle(blocks)
        nodes.append(nodes[0])
    
        for i in range(1, len(nodes) -1, 2):
            edges.append((nodes[i],nodes[i+1]))
    
    return edges

def getCycles(red,blue):
    adjDict = {}
    for pair in red:
        adjDict[(pair[0], 'red')] = pair[1]
        adjDict[(pair[1], 'red')] = pair[0]
    for pair in blue:
        adjDict[(pair[0], 'blue')] = pair[1]
        adjDict[(pair[1], 'blue')] = pair[0]

    visited = []
    allCycles = []

    for v in range(1, len(red) + len(blue) + 1):
        if v not in visited:
            start = v
            cycle = [v]
            visited.append(v)

            color = 'red'
            while True:
                v = adjDict[(v,color)]
                if v == start:
                    allCycles.append(cycle)
                    break
                else:
                    cycle.append(v)
                    visited.append(v)
                    if color == 'red': color = 'blue'
                    else: color = 'red'
    return allCycles

pEdges = getColoredEdges(p)
qEdges = getColoredEdges(q)

cycles = getCycles(pEdges,qEdges)

twoBreakDist = len(pEdges) - len(cycles)
print twoBreakDist
