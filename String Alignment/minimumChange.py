import os
input = open(os.path.abspath('../input/rosalind_ba4a.txt'))
if not os.path.exists('../output/'): os.mkdir('../output/')
output = open(os.path.abspath('../output/rosalind_ba4a.txt'), 'w')

money = int(input.readline().strip())
coins = [int(item) for item in input.readline().split(',')]
input.close()

minimumCoins = []
minimumCoins.append(0.0)
for m in range(1,money+1):
    minimumCoins.append(float('Inf'))
    for i,coin in enumerate(coins):
        if m >= coin:
            if minimumCoins[m-coin] + 1 < minimumCoins[m]:
                minimumCoins[m] = minimumCoins[m-coin] + 1
output.write(str(int(minimumCoins[money])))
output.close()
