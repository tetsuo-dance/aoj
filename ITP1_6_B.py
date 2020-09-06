import itertools
n = int(input())
mark = ['S', 'H', 'C', 'D']
nums = [str(i) for i in range(1, 14)]
cards = []

for i in mark:
    for j in nums:
        cards.append("{0} {1}".format(i, j))


for i in range(1, n+1):
    pair = input()
    cards.remove(pair)


for i in cards:
    print(i)
