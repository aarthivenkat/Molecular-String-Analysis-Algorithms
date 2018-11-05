import os
import sys
input = open(os.path.abspath('../input/rosalind_ba6g.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba6g.txt'), 'w')

def format(list):
  newList = ["%+d" %elem for elem in list]
  return "(" + ' '.join(newList) + ")\n"

#x = input.readline().strip()
x = "(8 7 9 10 12 11 8)"
x = [int(elem) for elem in x[1:len(x)-1].split()]
input.close()

y = []
for i in range(0,len(x)-1,2):
    if x[i+1] - x[i] == 1: y.append((i+2)/2)
    if x[i+1] - x[i] == -1: y.append(-((i+2)/2))

print format(y)
output.write(format(y))
output.close()
