import os
import sys
input = open(os.path.abspath('../input/rosalind_ba6b.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba6b.txt'), 'w')

x = input.readline().strip()
x = [int(elem) for elem in x[1:len(x)-1].split()]
input.close()

y = [0]
y.extend(x)
y.append(len(x)+1)
totalBreakpoints = 0
for i in range(len(y) - 1):
  if y[i] - y[i+1] != -1: totalBreakpoints += 1

print totalBreakpoints
