import os
import sys
input = open(os.path.abspath('../input/rosalind_ba6h.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba6h.txt'), 'w')

def format(list):
  newList = ["%d" %elem for elem in list]
  return "(" + ' '.join(newList) + ")\n"

def chrToCycle(list):
    y = []
    for elem in list:
        if elem > 0:
            y.extend([(2*elem) - 1, (2*elem)])
        else:
            y.extend([(-2*elem), (-2*elem) - 1])
    return y

x = input.readline().strip()  
x = ''.join(x.split("(")).split(")")[:-1]
edges = []
for chr in x:
    blocks = [int(elem) for elem in chr.split()]
    nodes = [str(elem) for elem in chrToCycle(blocks)]
    nodes.append(nodes[0])

    for i in range(1, len(nodes) -1, 2):
      edges.append("(" + nodes[i] + ", " + nodes[i+1] + ")")

print ', '.join(edges)
      
      
