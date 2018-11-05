import os
input = open(os.path.abspath('../input/rosalind_ba6e.txt'))

def getKmers(text, k):
    kmers = {}
    for i in range(len(text) - k +1):
        window = text[i:i+k]
        if window not in kmers: kmers[window] = []
        kmers[window].append(str(i))
    return kmers

k, text1, text2 = input.readlines()
firstK = getKmers(text1.strip(),int(k.strip()))
secondK = getKmers(text2.strip(), int(k.strip()))
complement = {'A':'T','G':'C','C':'G','T':'A'}

for kmer in firstK:
    if kmer in secondK:
        pos1 = firstK[kmer]
        pos2 = secondK[kmer]
        for posx in pos1:
            for posy in pos2:
                print "(%s, %s)" %(posx,posy)

    rcKmer = ''.join([complement[s] for s in kmer[::-1]])

    if rcKmer in secondK:
        pos1 = firstK[kmer]
        pos2 = secondK[rcKmer]
        for posx in pos1:
            for posy in pos2:
                print "(%s, %s)" %(posx,posy)
