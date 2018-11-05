import os
input = open(os.path.abspath('../input/rosalind_ba4b.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba4b.txt'), 'w')

n,m = [int(item) for item in input.readline().split()]
down = []
right = []
path = []

# Getting input
for i,row in enumerate(input):
    matrixRow = row.split()
    if matrixRow == ['-']: break
    down.append([int(item) for item in matrixRow])

for j,row in enumerate(input):
    right.append([int(item) for item in row.split()])

# Creating path matrix
for i in range(n+1):
    path.append([])
    for j in range(m+1):
        path[i].append(0)

# Traversal
for i in range(1, n+1):
    path[i][0] = path[i-1][0] + down[i-1][0]
for j in range(1, m+1):
    path[0][j] = path[0][j-1] + right[0][j-1]
for i in range(1,n+1):
    for j in range(1,m+1):
        path[i][j] = max([path[i-1][j] + down[i-1][j], path[i][j-1] + right[i][j-1]])
print path[n][m]
