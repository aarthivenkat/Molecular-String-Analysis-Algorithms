import os
import sys
input = open(os.path.abspath('../input/rosalind_ba6j.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba6j.txt'), 'w')

x = input.readline().strip()
y = input.readline().strip().split(", ")

currEdges = ["(%s, %s)" %(y[0], y[1]), "(%s, %s)" %(y[1], y[0]), "(%s, %s)" %(y[2], y[3]), "(%s, %s)" %(y[3],y[2])]
y1 = "(%s, %s)" %(y[0], y[2])
y2 = "(%s, %s)" %(y[1], y[3])
count = 0
for edge in currEdges:
    if edge in x:
        count += 1
    if count == 1: x = x.replace(edge, y1)
    if count == 2: x = x.replace(edge, y2)
print x
