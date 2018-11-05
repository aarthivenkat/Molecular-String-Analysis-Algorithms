import os
import sys
input = open(os.path.abspath('../input/rosalind_ba6d.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba6d.txt'), 'w')

p = input.readline().strip()  
p = ''.join(p.split("(")).split(")")[:-1]

q = input.readline().strip()
q = ''.join(q.split("(")).split(")")[:-1]

def chrToCycle(list):
    y = []
    for elem in list:
        if elem > 0:
            y.extend([(2*elem) - 1, (2*elem)])
        else:
            y.extend([(-2*elem), (-2*elem) - 1])
    return y

def format(list):
  newList = ["%+d" %elem for elem in list]
  return "(" + ' '.join(newList) + ")"

def cycleToChr(x):
    y = []
    x.insert(0,x[-1])
    x = x[:-1]
    for i in range(0,len(x),2):
        if x[i+1] - x[i] == 1: y.append(x[i+1]/2)
        if x[i+1] - x[i] == -1: y.append(-x[i]/2)
    return y

def getColoredEdges(x):        
    edges = []
    for chr in x:
        blocks = [int(elem) for elem in chr.split()]
        nodes = chrToCycle(blocks)
        nodes.append(nodes[0])
    
        for i in range(1, len(nodes) -1, 2):
            edges.append((nodes[i],nodes[i+1]))
    
    return edges

def twoBreak(x,y):
    currEdges = [(y[0], y[1]), (y[1], y[0]), (y[2], y[3]), (y[3],y[2])]
    
    chDic = {}
    chDic[currEdges[0]] = (y[0], y[2])
    chDic[currEdges[1]] = (y[1], y[3])
    chDic[currEdges[2]] = (y[2], y[0])
    chDic[currEdges[3]] = (y[3], y[1])

    for edge in currEdges:
        x = [chDic[i] if i==edge else i for i in x]
    return x

def getCycles(red,blue):
    adjDict = {}
    for pair in red:
        adjDict[(pair[0], 'red')] = pair[1]
    for pair in blue:
        adjDict[(pair[0], 'blue')] = pair[1]

    visited = []
    allCycles = []

    for v in range(1, len(red) + 1):
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
    
redEdges= getColoredEdges(p)
blueEdges= getColoredEdges(q)

allRed = redEdges + [(y,x) for (x,y) in redEdges]
allBlue = blueEdges +[(y,x) for (x,y) in blueEdges]
cycles = getCycles(allRed, allBlue)

"""
Getting trivial node info
"""
trivialCycles = [elem for elem in allRed if elem in allBlue]
trivialNodes = []
for pair in trivialCycles: trivialNodes.extend([pair[0], pair[1]])
trivialNodes = list(set(trivialNodes))

"""
Get black edges
"""
blackEdges = []
for i in range(1,len(allRed),2):
    blackEdges.append((i,i+1))
allBlack = blackEdges + [(y,x) for (x,y) in blackEdges]

cycles = ""
allCycles = getCycles(allRed,allBlack)
for cycle in allCycles:
    cycles += format(cycleToChr(cycle))
print cycles

"""
Start iteration
"""
while len(trivialNodes) != len(allRed):
    nonTrivialNodes = [node for node in range(1,(len(redEdges)*2) + 1) if node not in trivialNodes]
    for edge in allBlue:
        if edge[0] in nonTrivialNodes:
            blue1 = edge[0]
            blue2 = edge[1]
            break
    
    for edge in allRed:
        if edge[0] == blue1:
            red1 = edge[1]
        if edge[0] == blue2:
            red2 = edge[1]
            
    allRed = twoBreak(allRed, [blue1,red1,blue2,red2])

    allCycles = getCycles(allRed,allBlack)
    cycles = ""
    for cycle in allCycles:
        cycles += format(cycleToChr(cycle))
    print cycles
    
    trivialCycles = [elem for elem in allRed if elem in allBlue]
    trivialNodes = []
    for pair in trivialCycles: trivialNodes.extend([pair[0], pair[1]])
    trivialNodes = list(set(trivialNodes))
