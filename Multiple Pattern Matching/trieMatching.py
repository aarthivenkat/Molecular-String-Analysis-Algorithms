import os
import sys
from collections import Counter

"""
Instructions noted we can start anywhere in the DNA sequence
"""
START = 0

inputDNA = open("DNA.txt",'r')
inputQUERIES = open("queries.txt",'r')
output = open("matching_queries.txt", 'w')

inputDNA.readline()
text = ""

for line in inputDNA:
    text += line.strip()
text = text[START:]+text[:START]+'\n'
patterns = [line.strip() for line in inputQUERIES.readlines()]

trie = {}
keywordlist = []
endnodelist = []
def trieConstruction():
    idx = 0
    root = 0
    for pattern in patterns:
        node = root
        if node not in trie: trie[node] = []
        for char in pattern:               
            symbol = char
            symbolIsEdge = False
            for edge,adj in trie[node]:
                if symbol == edge:
                    symbolIsEdge = True
                    node = adj
                    break
            if not symbolIsEdge:
                idx += 1
                trie[idx] = []
                trie[node].append((symbol, idx))
                node = idx
        keywordlist.append(node)
    return
    
def prefixTrieMatching(text):
    symbol = text[0]
    idx = 0
    v = 0
    pattern = ""
    while True:
        if not trie[v]:
            endnodelist.append(v)
            return (idx - len(pattern))
        symbolIsEdge = False
        for edge,adj in trie[v]:
            if symbol == edge:
                symbolIsEdge = True
                idx += 1
                symbol = text[idx]
                pattern += symbol
                v = adj
                break
        if not symbolIsEdge:
            return -1

def trieMatching(string):
    j = 0
    while string:
        pos = prefixTrieMatching(string)
        #if pos != -1:
            #output.write(str(j) + " ")
        string = string[1:]
        j += 1

trieConstruction()
trieMatching(text)

keywordcount = dict(Counter(endnodelist))
for key,val in keywordcount.iteritems():
    output.write(patterns[keywordlist.index(key)] + " " + str(val) + "\n")

output.close()
