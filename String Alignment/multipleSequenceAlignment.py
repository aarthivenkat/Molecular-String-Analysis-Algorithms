import os
import sys
input = open(os.path.abspath('../input/rosalind_ba5e.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba5e.txt'), 'w')

s1 = input.readline().strip()
s2 = input.readline().strip()
s3 = input.readline().strip()
n = len(s1)
m = len(s2)
o = len(s3)
sys.setrecursionlimit(n*m*o)     
       
path = []
backtrack = []
for i in range(n+1):
    path.append([])
    backtrack.append([])
    for j in range(m+1):
        path[i].append([])
        backtrack[i].append([])
        for k in range(o+1):
            path[i][j].append(0)
            backtrack[i][j].append('')

for i in range(n+1):
    backtrack[i][0][0] = 'i'
for j in range(m+1):
    backtrack[0][j][0] = 'j'
for k in range(o+1):
    backtrack[0][0][k] = 'k'

# Traversal
for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(1,o+1):
            if s1[i-1] == s2[j-1] == s3[k-1]: isMatch = 1
            else: isMatch = 0
            path[i][j][k] = max( path[i-1][j][k],
                                 path[i][j-1][k],
                                 path[i][j][k-1],
                                 path[i-1][j-1][k],
                                 path[i-1][j][k-1],
                                 path[i][j-1][k-1],
                                 path[i-1][j-1][k-1] + isMatch)

            if path[i][j][k] == path[i-1][j][k]: backtrack[i][j][k] = 'i'
            elif path[i][j][k] == path[i][j-1][k]: backtrack[i][j][k] = 'j'
            elif path[i][j][k] == path[i][j][k-1]: backtrack[i][j][k] = 'k'
            elif path[i][j][k] == path[i-1][j-1][k]: backtrack[i][j][k] = 'i,j'
            elif path[i][j][k] == path[i-1][j][k-1]: backtrack[i][j][k] = 'i,k'
            elif path[i][j][k] == path[i][j-1][k-1]: backtrack[i][j][k] = 'j,k'
            else: backtrack[i][j][k] = 'i,j,k'
            
s = []; t = []; u = []
i = n; j = m; k = o

while True:
        if backtrack[i][j][k] == 'i,j,k':   
            s = [s1[i-1]] + s
            t = [s2[j-1]] + t
            u = [s3[k-1]] + u
            i -= 1; j -= 1; k -= 1
        elif backtrack[i][j][k] == 'j,k':   
            s = ['-'] + s
            t = [s2[j-1]] + t
            u = [s3[k-1]] + u
            j -= 1; k -= 1
        elif backtrack[i][j][k] == 'i,k': 
            s = [s1[i-1]] + s
            t = ['-'] + t
            u = [s3[k-1]] + u
            i -= 1; k -= 1
        elif backtrack[i][j][k] == 'i,j':
            s = [s1[i-1]] + s
            t = [s2[j-1]] + t
            u = ['-'] + u
            i -= 1; j -= 1
        elif backtrack[i][j][k] == 'k':
            s = ['-'] + s
            t = ['-'] + t
            u = [s3[k-1]] + u
            k -= 1
        elif backtrack[i][j][k] == 'j':
            s = ['-'] + s
            t = [s2[j-1]] + t
            u = ['-'] + u
            j -= 1
        elif backtrack[i][j][k] == 'i':
            s = [s1[i-1]] + s
            t = ['-'] + t
            u = ['-'] + u
            i -= 1
        """
        FIX
        """
        if i == 0 or j == 0 or k == 0
            if i != 0:
                s = [s1[i-1]] + s
                i -= 1
            if j != 0:
                t = [s2[j-1]] + t
                j -= 1
            if k != 0:
                u = [s3[k-1]] + u
                k -= 1
            break
        
output.write(str(path[n][m][o]) + '\n')
output.write(''.join(s) + '\n')
output.write(''.join(t) + '\n')
output.write(''.join(u) + '\n')
output.close()
