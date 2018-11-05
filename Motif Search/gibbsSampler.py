"""
BA2g: Gibbs Sampler Motif Search
"""

import os
import random

input = open(os.path.abspath('../input/rosalind_ba2g.txt'))
vals = input.readlines()
k = int(vals[0].split()[0])
t = int(vals[0].split()[1])
N = int(vals[0].split()[2])
dnaCollection = vals[1:]

def random_distr(d):
    r = random.uniform(0, 1)
    s = 0
    for item, prob in d.items():
        s += prob
        if s >= r:
            return item
    return item

def profileRandomKmer(profile, text):
    probabilities = {}
    for i in range(len(text) - k +1):
        window = text[i:i+k]
        currentP = 1
        for pos,base in enumerate(window):
            currentP *= profile[base][pos]
        probabilities[window] = currentP
    sumP = sum(probabilities.values())
    for key in probabilities:
        probabilities[key] = probabilities[key] / sumP
    return random_distr(probabilities)
    
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
    return totalScore
    
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
for i in range(20):
    motifs = []
    for j in range(t):
        start = random.randint(0,len(dnaCollection[j].strip()) - k)
        motifs.append(dnaCollection[j][start:start+k])
    bestProfile = {}
    bestMotifs = []
    for l in range(N):
        index = random.randint(0,t-1)
        tempMotifs = motifs[:index] + motifs[index+1:]
        prof = buildProfile(tempMotifs, len(tempMotifs))
        kmer = profileRandomKmer(prof,dnaCollection[index].strip())
        motifs[index] = kmer
        currProfile = buildProfile(motifs,len(motifs))
        if score(currProfile) < score(bestProfile):
            bestProfile = currProfile
            bestMotifs = motifs
    if score(bestProfile) < bestScore:
        bestScore = score(bestProfile)
        totalBestMotifs = bestMotifs
print '\n'.join(totalBestMotifs)
