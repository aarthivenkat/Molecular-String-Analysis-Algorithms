import os
input = open(os.path.abspath('../input/rosalind_ba3m.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba3m.txt'), 'w')

lines = input.readlines()
input.close()
adjDict = {}
degreeDict = {}
def preProcessing(text):
    inOnly = []
    for line in text:
        s,t = line.strip().split(' -> ')
        t = [item for item in t.split(',')]
        adjDict[s] = t
    for k,vn in adjDict.iteritems():
        if k not in degreeDict: degreeDict[k] = [0,0]
        degreeDict[k][0] += len(vn)
        for v in vn:
            if v not in degreeDict: degreeDict[v] = [0,0]
            if v not in adjDict: inOnly.append(v)
            degreeDict[v][1] += 1
    for v in inOnly: adjDict[v] = []

def getMaxNonBranchingPaths():
    paths = []
    intermediate = []
    for v in adjDict.keys():
        if degreeDict[v] != [1,1] and degreeDict[v][0] > 0:
            for w in adjDict[v]:
                nonBranchingPath = [v,w]
                while degreeDict[w] == [1,1]:
                    u = adjDict[w][0]
                    nonBranchingPath.append(u)
                    w = u
                paths.append(nonBranchingPath)
                intermediate.extend(nonBranchingPath[1:-1])
    
    for v in adjDict.keys():
        if degreeDict[v] == [1,1] and v not in intermediate:
            w = adjDict[v][0]
            nonBranchingPath = [v,w]
            while degreeDict[w] == [1,1] and w != v:
                u = adjDict[w][0]
                degreeDict[w] = [0,0]
                nonBranchingPath.append(u)
                w = u
            paths.append(nonBranchingPath)
            intermediate.extend(nonBranchingPath)
    
    for path in paths:
        output.write('->'.join(path) + '\n')
    output.close()
 
preProcessing(lines)
getMaxNonBranchingPaths()
