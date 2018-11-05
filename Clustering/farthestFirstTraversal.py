import os
import math
input = open(os.path.abspath('../input/rosalind_ba9a.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba9a.txt'), 'w')

parameters = input.readline().strip().split()
k,m = [int(x) for x in parameters]
d = input.readlines()
datapoints = {}
for i,elem in enumerate(d):
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
        
def maxDistance(centers):
    alldistances = centerDistance(centers)
    return max(alldistances, key=alldistances.get)
    
def farthestFirstTraversal():
    cen = [0]
    while len(cen) < k:
        cen.append(maxDistance(cen))
    return cen
    
centers = farthestFirstTraversal()
for c in centers:
    print ' '.join([str(x) for x in datapoints[c]])
