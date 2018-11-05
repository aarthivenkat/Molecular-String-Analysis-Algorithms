import os
import math
input = open(os.path.abspath('../input/rosalind_ba9b.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba9b.txt'), 'w')

parameters = input.readline().strip().split()
k,m = [int(x) for x in parameters]
datapoints = {}
for i,elem in enumerate(input):
    if elem == '--------\n':
        centersEnd = i
        continue
    datapoints[i] = [float(x) for x in elem.strip().split()]

def euclidean(v,w):
    vcoords = datapoints[v]
    wcoords = datapoints[w]
    runningtotal = 0
    for i in range(m):
        runningtotal += (vcoords[i] - wcoords[i])**2
    return runningtotal**0.5
    
def centerDistance(centers):
    distToCenter = {} #key = elem. value = (center, distance) 
    for elem in datapoints:
        allc = {}
        for c in centers:
            allc[c] = euclidean(elem,c)
        keytomin = min(allc, key=allc.get)
        distToCenter[elem] = allc[keytomin]
    return distToCenter
        
def distortion():
    alldistances = centerDistance(range(centersEnd))
    n = len(alldistances) - centersEnd
    return (sum([x**2 for x in alldistances.values()])) / n
    
print '%.3f' % distortion()
