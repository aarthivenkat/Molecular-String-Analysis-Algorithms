"""
BA1k: Create frequency array.
Create list of all possible combinations of a kmer.
Iterate through k-windows of string and incremement frequency of each kmer.
The kmers that do not show in string have 0 frequency. 
Sort the dictionary by string (lexicographically), print frequencies in order.

Input: line \n pattern
Output: frequencies of each possible kmer in lexicographical order.
"""

import os
input = open(os.path.abspath('../input/rosalind_ba1k.txt'))

"""
Return list of all combinations of length interval string.
E.g. interval = 1 return [A,C,G,T]
"""
def allCombinations(interval):
    kmers = [""]
    for c in range(interval):
        currKmers = []
        for item in kmers:
            currKmers.append(item+'A')
            currKmers.append(item+'C')
            currKmers.append(item+'G')
            currKmers.append(item+'T')
        kmers = currKmers
    return kmers

"""
Create frequency array by iterating through string and counting appearances.
Then fill in gaps using allCombinations list.
"""
def freqArray(text,interval,kmers):        
    freqArray = {}
    for i in range(len(text) - interval +1):
        curr = text[i:i+interval]
        if curr in freqArray: freqArray[curr] += 1
        else: freqArray[curr] = 1

    for elem in kmers:
        if elem not in freqArray: freqArray[elem] = 0

    sorted_freq = [str(item[1]) for item in sorted(freqArray.iteritems())]
    print ' '.join(sorted_freq)

line,patt = input.readlines()
kmers = allCombinations(int(patt.strip()))
freqArray(line.strip(),int(patt.strip()), kmers)
input.close()
