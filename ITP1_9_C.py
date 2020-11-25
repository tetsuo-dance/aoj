n = int(input())
taro_score = 0
hanako_score = 0

for i in range(n):
    taro_card, hanako_card = input().split()
    if taro_card < hanako_card:
        hanako_score += 3
    elif taro_card > hanako_card:
        taro_score += 3
    else:
        hanako_score += 1
        taro_score += 1

print("{0} {1}".format(taro_score, hanako_score))
