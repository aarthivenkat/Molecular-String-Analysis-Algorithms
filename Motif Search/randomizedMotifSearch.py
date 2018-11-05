"""
BA2f: Randomized Motif Search
"""

import os
import random

input = open(os.path.abspath('../input/rosalind_ba2f.txt'))
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

bestScore = float("inf")
totalBestMotifs = []
for i in range(1000):
    motifs = []
    for i in range(t):
        start = random.randint(0,len(dnaCollection[i].strip()) - k)
        motifs.append(dnaCollection[i][start:start+k])
    bestProfile = {}
    bestMotifs = []
    while(True):
        prof = buildProfile(motifs, t)
        motifs = []
        for i in range(t):
            motifs.append(mostProbableKmer(prof, dnaCollection[i].strip()))

        currProfile = buildProfile(motifs,len(motifs))
        if score(currProfile) < score(bestProfile):
            bestProfile = buildProfile(motifs,len(motifs))
            bestMotifs = motifs
        else:
            if score(bestProfile) < bestScore:
                bestScore = score(bestProfile)
                totalBestMotifs = bestMotifs
            break
print '\n'.join(totalBestMotifs)
