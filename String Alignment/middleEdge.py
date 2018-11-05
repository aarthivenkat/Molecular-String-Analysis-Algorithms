import os
import sys
input = open(os.path.abspath('../input/rosalind_ba5c.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba5c.txt'), 'w')

s1 = input.readline().strip()
s2 = input.readline().strip()
n = len(s1)
m = len(s2)
middle = (m+1)/2.0
#print n,m
if middle.is_integer():
    sourceMiddle = int(middle-1)
    sinkMiddle = int(middle-1)
else:
    sourceMiddle = int(middle-0.5)
    sinkMiddle = int(middle-0.5)
    
sys.setrecursionlimit(n*m)     

alphabet = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

diagonal = {}
for letter1 in alphabet:
    if letter1 not in diagonal: diagonal[letter1] = {}
    scores = input.readline().split()
    for i,letter2 in enumerate(alphabet):
        diagonal[letter1][letter2] = int(scores[i])
   
# Initializing column in linear space
col1 = []
col2 = []
for i in range(n+1):
    col1.append(-5 * i)
    col2.append(0)

# Traversal from source
for i in range(1, sourceMiddle + 2):
    for j in range(0, n+1):
        if j == 0:
            col2[j] = col1[j] - 5
        else:
            col2[j] = max(col1[j-1] + diagonal[s1[j-1]][s2[i-1]], col1[j] - 5, col2[j-1] - 5)
    col1 = col2
    col2 = [0 for i in range(n+1)]
  
midColFromSource = col1[1:]

col1 = []
col2 = []
for i in range(n+1):
    col1.append(-5 * i)
    col2.append(0)

# Traversal from sink
bt = ['' for i in range(n+1)]
for i in range(1, sinkMiddle + 2):
    for j in range(0, n+1):
        if j == 0: col2[j] = col1[j] - 5
        else:
            col2[j] = max(col1[j-1] + diagonal[s1[::-1][j-1]][s2[::-1][i-1]], col1[j] - 5, col2[j-1] - 5)
            temp = s2[::-1][i-1]
        if col2[j] == col1[j-1] + diagonal[s1[::-1][j-1]][s2[::-1][i-1]]: bt[j] = 'm'
        elif col2[j] == col1[j] - 5: bt[j] = 'r'
        else: bt[j] = 'd'
    col1 = col2
    col2 = [0 for i in range(n+1)]

midColFromSink = col1[::-1][:-1]

length = [sum(x) for x in zip(midColFromSource, midColFromSink)]
maxPos = -1
maxElem = 0
for i,elem in enumerate(length):
    if elem > maxElem:
        maxElem = elem
        maxPos = i
        
print "(%d,%d)" % (maxPos, sourceMiddle),
if bt[maxPos] == 'r': print "(%d,%d)" %(maxPos, sourceMiddle + 1)
elif bt[maxPos] == 'm': print "(%d,%d)" %(maxPos+1, sourceMiddle + 1)
else: print "(%d,%d)" %(maxPos, sourceMiddle)
