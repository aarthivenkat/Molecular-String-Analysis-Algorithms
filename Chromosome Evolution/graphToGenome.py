import os
import sys
input = open(os.path.abspath('../input/rosalind_ba6i.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba6i.txt'), 'w')

def cycleToChr(x):
    y = []
    x.insert(0,x[-1])
    x = x[:-1]
    for i in range(0,len(x),2):
        if x[i+1] - x[i] == 1: y.append(x[i+1]/2)
        if x[i+1] - x[i] == -1: y.append(-x[i]/2)
    return y
    
def format(list):
  newList = ["%+d" %elem for elem in list]
  return "(" + ' '.join(newList) + ")"

x = input.readline().strip()
extraneous = ["(", ")", ","]
for e in extraneous:
    x = x.replace(e, "")
x = [int(elem) for elem in x.split(" ")]

cycles = []
currI = 0
while x:
    head = x[0]
    if head%2 == 1: diff = 1
    if head%2 == 0: diff = -1
    for i,elem in enumerate(x):
        if x[i+1] - head == diff:
            currI = i
            break
    cycles.append(x[0:i+2])
    x = x[i+2:]

allCycles = ""
for cycle in cycles:
    allCycles += format(cycleToChr(cycle))
print allCycles
