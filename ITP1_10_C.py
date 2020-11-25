import math

while True:
    n = int(input())
    if n == 0:
        break
    score = input().split()
    score_int = [int(i) for i in score]
    m = sum(score_int) / n
    tmp_bunsan = 0

    for i in range(n):
        tmp_bunsan += (score_int[i] - m) ** 2
    bunsan = tmp_bunsan / n
    hensa = math.sqrt(bunsan)
    print(hensa)
