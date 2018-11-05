"""
BA1d: Iterate through string in k-length windows, whenever we hit the window
matches the pattern, we add the starting position to list. return list.

Input: short pattern \n full line
Output: Space-delimited list of start positions
"""

import os
input = open(os.path.abspath('../input/rosalind_ba1d.txt'))

"""
Return positions of pattern in text
"""
def patternPosition(text,pattern):
    startPos= []
    for i in range(len(text) - len(pattern) +1):
        if text[i:i+len(pattern)] == pattern:
            startPos.append(str(i))
    return ' '.join(startPos)

patt,line = input.readlines()
print patternPosition(line.strip(),patt.strip())
