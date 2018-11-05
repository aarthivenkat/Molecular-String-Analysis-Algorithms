import os
import sys
input = open(os.path.abspath('../input/rosalind_ba6a.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba6a.txt'), 'w')

def format(list):
  newList = ["%+d" %elem for elem in list]
  return "(" + ' '.join(newList) + ")\n"

x = input.readline().strip()
x = [int(elem) for elem in x[1:len(x)-1].split()]
input.close()

for k in range(1, len(x) + 1):
  pos = [abs(elem) for elem in x].index(k) + 1
  if pos - (k-1) == 1 and x[k-1:pos][0] > 0: continue

  x[k-1:pos] = [-elem for elem in x[k-1:pos][::-1]]
  output.write(format(x))
  if x[k-1] < 0:
    x[k-1] = -x[k-1]
    output.write(format(x))

output.close()
