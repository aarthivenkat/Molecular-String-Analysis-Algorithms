"""
BA2e: Greedy Pseudocount Motif Search
For each kmer in the first string, this algorithm iteratively creates a profile matrix,
and searches for the most-probable kmer in the next string until all strings are searched.
It outputs the kmer from the first string that minimizes the score of the end profile matrix.
"""

import os
input = open(os.path.abspath('../input/rosalind_ba2e.txt'))
vals = input.readlines()
k = int(vals[0].split()[0])
t = int(vals[0].split()[1])
dnaCollection = vals[1:]

def mostProbableKmer(profile, text):
    bestP = 0
    mostProbable = ""
    for i in range(len(text) - k +1):
        window = text[i:i+k]
        currentP = 1
        for pos,base in enumerate(window):
            currentP *= profile[base][pos]
        if currentP > bestP:
            bestP = currentP
            mostProbable = window
    if mostProbable == "": return text[0:k]
    return mostProbable
    
def score(p):
    if p == {}: return float("inf")
    totalScore = 0
    for i in range(k):
        score = []
        score.append(p['A'][i] * t)
        score.append(p['C'][i] * t)
        score.append(p['G'][i] * t)
        score.append(p['T'][i] * t)
        score.remove(max(score))

        totalScore += sum(score)
    return round(totalScore,5)
    
def kmersInFirstString(text):
    kmers = []
    for i in range(len(text) - k +1):
        kmers.append(text.strip()[i:i+k])
    return kmers   
    
def buildProfile(motifs, size):
    profile = {}
    bases = ['A','C','G','T']
    for i in range(k):
        posProfile = {}
        for motif in motifs:
            if motif[i] in posProfile: posProfile[motif[i]] += 1
            else: posProfile[motif[i]] = 2
        for base in bases:
            if base not in posProfile: posProfile[base] = 1
            if base not in profile: profile[base] = [float(posProfile[base]) / (size+4)]
            else: profile[base].append(float(posProfile[base]) / (size+4))
            
    return profile

bestProfile = {}
bestMotifs = []
for motif in kmersInFirstString(dnaCollection[0].strip()):
    motifs = [motif]
    for i in range (1,t):
        prof = buildProfile(motifs, len(motifs))
        motifs.append(mostProbableKmer(prof,dnaCollection[i].strip()))
    if score(buildProfile(motifs,len(motifs))) < score(bestProfile):
        bestProfile = buildProfile(motifs,len(motifs))
        bestMotifs = motifs
    
print '\n'.join(bestMotifs)
