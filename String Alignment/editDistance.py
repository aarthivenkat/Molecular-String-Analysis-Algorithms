import os
import sys
input = open(os.path.abspath('../input/rosalind_ba4g.txt'))

s1 = input.readline().strip()
s2 = input.readline().strip()
n = len(s1)
m = len(s2)
sys.setrecursionlimit(n*m)

path = []
for i in range(n+1):
    path.append([])
    for j in range(m+1):
        path[i].append(0)

for i in range(n+1): path[i][0] = i
for j in range(m+1):
    path[0][j] = j  
       
# Traversal
for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i-1] == s2[j-1]: cost = 0
        else: cost = 1
        path[i][j] = min([path[i-1][j]+1, path[i][j-1]+1, path[i-1][j-1] + cost])

print path[n][m]
