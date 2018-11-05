import os
import sys
input = open(os.path.abspath('../input/rosalind_ba4c.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba4c.txt'), 'w')

s1 = input.readline().strip()
s2 = input.readline().strip()
n = len(s1)
m = len(s2)
sys.setrecursionlimit(n*m)
       
path = []
backtrack = []
for i in range(n+1):
    path.append([])
    backtrack.append([])
    for j in range(m+1):
        path[i].append(0)
        backtrack[i].append('')

# Traversal
for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i-1] == s2[j-1]: path[i][j] = max([path[i-1][j], path[i][j-1], path[i-1][j-1] + 1])
        else: path[i][j] = max([path[i-1][j], path[i][j-1], path[i-1][j-1]])
        if path[i][j] == path[i-1][j]: backtrack[i][j] = 'd'
        elif path[i][j] == path[i][j-1]: backtrack[i][j] = 'r'
        elif path[i][j] == path[i-1][j-1] + 1 and s1[i-1] == s2[j-1]: backtrack[i][j] = 'm'

def outputLCS(i,j):
    if i == 0 or j == 0: return []
    if backtrack[i][j] == 'd': return outputLCS(i-1,j)
    elif backtrack[i][j] == 'r': return outputLCS(i,j-1)
    else:
        return [s1[i-1]] + outputLCS(i-1,j-1)
print ''.join(outputLCS(n,m))[::-1]


