import os
import sys
input = open(os.path.abspath('../input/rosalind_ba5b.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba5b.txt'), 'w')

s1 = input.readline().strip()
s2 = input.readline().strip()
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

lowPath = []
midPath = []
upPath = []
lowBt = []
midBt = []
upBt = []

for i in range(n+1):
    lowPath.append([])
    midPath.append([])
    upPath.append([])
    lowBt.append([])
    midBt.append([])
    upBt.append([])
    for j in range(m+1):
        lowPath[i].append(0)
        midPath[i].append(0)
        upPath[i].append(0)
        lowBt[i].append('')
        midBt[i].append('')
        upBt[i].append('')

for i in range(n+1):
    lowPath[i][0] = -10 - i
    midPath[i][0] = -10 - i
    upPath[i][0] = float('-inf')
for j in range(m+1):
    lowPath[0][j] = float('-inf')
    midPath[0][j] = -10 - j
    upPath[0][j] = -10 - j
    
lowPath[0][0] = 0; midPath[0][0] = 0; upPath[0][0] = 0

# Traversal
for i in range(1,n+1):
    for j in range(1,m+1):
        lowPath[i][j] = max(lowPath[i-1][j] - 1, midPath[i-1][j] - 11)
        if lowPath[i][j] == lowPath[i-1][j] - 1: lowBt[i][j] = 'l'
        else: lowBt[i][j] = 'm'
        
        upPath[i][j] = max(upPath[i][j-1] - 1, midPath[i][j-1] - 11)
        if upPath[i][j] == upPath[i][j-1] - 1: upBt[i][j] = 'u'
        else: upBt[i][j] = 'm'
        
        midPath[i][j] = max(lowPath[i][j], upPath[i][j], midPath[i-1][j-1] + diagonal[s1[i-1]][s2[j-1]])
        if midPath[i][j] == lowPath[i][j]: midBt[i][j] = 'l'
        elif midPath[i][j] == upPath[i][j]: midBt[i][j] = 'u'
        else: midBt[i][j] = 'm'     
i = n
j = m
s = []
t = []

currBt = midBt
start = currBt[i][j]
if currBt == midBt and start == 'l':
    currBt = lowBt
elif currBt == midBt and start == 'u':
    currBt = upBt
while True:
    if currBt == midBt:
        if currBt[i][j] == 'm':
            s = [s1[i-1]] + s
            t = [s2[j-1]] + t
            i -= 1
            j -= 1
        elif currBt[i][j] == 'l':
            currBt = lowBt
        elif currBt[i][j] == 'u':
            currBt = upBt
        
    elif currBt == lowBt:
        s = [s1[i-1]] + s 
        t = ['-'] + t 
        i -= 1
        if currBt[i+1][j] == 'm':
            currBt = midBt
    
    elif currBt == upBt:
        s = ['-'] + s 
        t = [s2[j-1]] + t 
        j -= 1
        if currBt[i][j+1] == 'm':
            currBt = midBt   
            
    if i == 0 and j == 0: break
        
output.write(str(midPath[n][m]) + '\n')
output.write(''.join(s) + '\n')
output.write(''.join(t) + '\n')
output.close()
