import os
import sys
input = open(os.path.abspath('../input/rosalind_ba4f.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba4f.txt'), 'w')

s1 = input.readline().strip()
s2 = input.readline().strip()
s1 = "MEANLY"
s2 = "PENALTY"
n = len(s1)
m = len(s2)
sys.setrecursionlimit(n*m)     
alphabet = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

diagonal = {}
for letter1 in alphabet:
    if letter1 not in diagonal: diagonal[letter1] = {}
    scores = input.readline().split()
    for i,letter2 in enumerate(alphabet):
        diagonal[letter1][letter2] = int(scores[i])
        
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
        path[i][j] = max([path[i-1][j] - 5, path[i][j-1] - 5 , path[i-1][j-1] + diagonal[s1[i-1]][s2[j-1]], 0])
        if path[i][j] == path[i-1][j] - 5: backtrack[i][j] = 'd'
        elif path[i][j] == path[i][j-1] - 5: backtrack[i][j] = 'r'
        elif path[i][j] == path[i-1][j-1] + diagonal[s1[i-1]][s2[j-1]]: backtrack[i][j] = 'm'
        else: backtrack[i][j] = '0'
        
        if path[i][j] >= maxPath:
            maxPath = path[i][j]
            maxLoc = (i,j)

for line in path: print line

def outputLCS1(i,j):
    if backtrack[i][j] == '0': return []
    if i == 0 and j == 0: return []
    if j == 0: return [s1[i-1::-1]]
    if i == 0: return ['-' for i in range(len(s1[i-1::-1]))]
    if backtrack[i][j] == 'd':
        return [s1[i-1]] + outputLCS1(i-1,j)
    elif backtrack[i][j] == 'r':
        return ['-'] + outputLCS1(i,j-1)
    else:
        return [s1[i-1]] + outputLCS1(i-1,j-1)

def outputLCS2(i,j):
    if backtrack[i][j] == '0': return []
    if i == 0 and j == 0: return []
    if i == 0: return [s2[j-1::-1]]
    if j == 0: return ['-' for i in range(len(s2[i-1::-1]))]
    if backtrack[i][j] == 'd': return ['-'] + outputLCS2(i-1,j)
    elif backtrack[i][j] == 'r': return [s2[j-1]] + outputLCS2(i,j-1)
    else:
        return [s2[j-1]] + outputLCS2(i-1,j-1)

output.write(str(path[maxLoc[0]][maxLoc[1]]) + '\n')
output.write(''.join(outputLCS1(maxLoc[0],maxLoc[1]))[::-1] + '\n')
output.write(''.join(outputLCS2(maxLoc[0],maxLoc[1]))[::-1] + '\n')
output.close()
