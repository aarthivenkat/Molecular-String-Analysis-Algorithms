import os
import sys
"""
input = open(os.path.abspath('../input/rosalind_ba4h.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba4h.txt'), 'w')

s2 = input.readline().strip()
s1 = input.readline().strip()
"""
s2 = "PENALTY"
s1 = "MEANLY"
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
maxPath = 0
maxLoc = (0,0)
for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i-1] == s2[j-1]: path[i][j] = max([path[i-1][j] - 1, path[i][j-1] - 1, path[i-1][j-1] + 1])
        else: path[i][j] = max([path[i-1][j] - 1, path[i][j-1] - 1, path[i-1][j-1] - 1])

        if path[i][j] == path[i-1][j] - 1: backtrack[i][j] = 'd'
        elif path[i][j] == path[i][j-1] - 1: backtrack[i][j] = 'r'
        else: backtrack[i][j] = 'm'
        
        if path[i][j] >= maxPath and i == n:
            maxPath = path[i][j]
            maxLoc = (i,j)

i = maxLoc[0]
j = maxLoc[1]
s = []
t = []

for line in path: print line
for line in backtrack: print line
while True:
        if backtrack[i][j] == 'm':   
            s = [s2[j-1]] + s
            t = [s1[i-1]] + t
            i -= 1
            j -= 1
        elif backtrack[i][j] == 'r': 
            s = [s2[j-1]] + s
            t = ["-"] + t
            j -= 1
        else:
            s = ["-"] + s
            t = [s1[i-1]] + t
            i -= 1
        if i == 0: break
print s, t
"""
output.write(str(maxPath) + '\n')
output.write(''.join(s) + '\n')
output.write(''.join(t) + '\n')
output.close()
"""
