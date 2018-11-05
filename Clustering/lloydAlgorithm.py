import os
import math
input = open(os.path.abspath('../input/rosalind_ba9c.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba9c.txt'), 'w')

parameters = input.readline().strip().split()
k,m = [int(x) for x in parameters]
datapoints = {}
for i,elem in enumerate(input):
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
    clusters = {}
    for c in centers:
        clusters[c] = []
        
    for elem in datapoints:
        allc = {}
        for c in centers:
            allc[c] = euclidean(elem,c)
        keytomin = min(allc, key=allc.get)
        distToCenter[elem] = allc[keytomin]
        clusters[keytomin].append(elem)
        
    return clusters
    
def centerOfGravity(l):
    center = [0] * m
    for elem in l:
        coords = datapoints[elem]
        for index,c in enumerate(coords):
            center[index] += c
    return [x/len(l) for x in center]
        
def lloyd():
    centers = range(len(datapoints), len(datapoints) + k)
    for i,elem in enumerate(centers): datapoints[elem] = datapoints[i]
    clusters = centerDistance(centers)
    while True:
        samecenters = 0
        for c in clusters:
            cluster = clusters[c]
            newCenter = centerOfGravity(cluster)
            if datapoints[c] == newCenter: samecenters += 1
            datapoints[c] = newCenter
        if samecenters == len(clusters): break
        clusters = centerDistance(centers)
    return clusters
        
for cluster in lloyd():
    for elem in datapoints[cluster]:
        print '%.3f' % elem,
    print ''
