import os
import sys
input = open(os.path.abspath('../input/rosalind_ba6f.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba6f.txt'), 'w')

def format(list):
  newList = ["%d" %elem for elem in list]
  return "(" + ' '.join(newList) + ")\n"

x = input.readline().strip()
x = [int(elem) for elem in x[1:len(x)-1].split()]
input.close()
y = []
for elem in x:
    if elem > 0:
        y.extend([(2*elem) - 1, (2*elem)])
    else:
        y.extend([(-2*elem), (-2*elem) - 1])
        
output.write(format(y))
