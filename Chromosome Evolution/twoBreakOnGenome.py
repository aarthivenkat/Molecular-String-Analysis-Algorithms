import os
import sys
input = open(os.path.abspath('../input/rosalind_ba6k.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba6k.txt'), 'w')

p = input.readline().strip()  
p = ''.join(p.split("(")).split(")")[:-1]

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
    
    return ", ".join([str(elem) for elem in sorted(edges)]), len(nodes)

def twoBreak(x,y):
    currEdges = ["(%s, %s)" %(y[0], y[1]), "(%s, %s)" %(y[1], y[0]), "(%s, %s)" %(y[2], y[3]), "(%s, %s)" %(y[3],y[2])]
    
    chDic = {}
    chDic[currEdges[0]] = "(%s, %s)" %(y[0], y[2])
    chDic[currEdges[1]] = "(%s, %s)" %(y[1], y[3])
    chDic[currEdges[2]] = "(%s, %s)" %(y[2], y[0])
    chDic[currEdges[3]] = "(%s, %s)" %(y[3], y[1])

    for edge in currEdges:
        x = x.replace(edge, chDic[edge])
        x = x.replace(edge, chDic[edge])
    return x

def graphToGenome(x):
    extraneous = ["(", ")", ","]
    for e in extraneous:
        x = x.replace(e, "")
    x = [int(elem) for elem in x.split(" ")]

    cycles = []
    currI = 0
    while x:
        head = x[0]
        if head%2 == 1: diff = 1
        if head%2 == 0: diff = -1
        for i,elem in enumerate(x):
            if x[i+1] - head == diff:
                currI = i
                break
        cycles.append(x[0:i+2])
        x = x[i+2:]

    allCycles = ""
    for cycle in cycles:
        allCycles += format(cycleToChr(cycle))

    return allCycles

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
    
graph, maxNode = getColoredEdges(p)
indices = input.readline().strip().split(", ")
graph = twoBreak(graph,indices)

red = graph.replace("), (", ")  ,  (")
red = red.split("  ,  ")
red = [eval(item) for item in red]
black = []
for i in range(1,maxNode,2):
    black.append((i,i+1))

cycles = ""
allCycles = getCycles(red,black)
for cycle in allCycles:
    cycles += format(cycleToChr(cycle))
print cycles
      
      
