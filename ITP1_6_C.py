n = int(input())
#floor = [0 for i in range(1, 11)]
my_a = [[0 for i in range(1, 11)], [0 for i in range(1, 11)], [
    0 for i in range(1, 11)]]
my_b = [[0 for i in range(1, 11)], [0 for i in range(1, 11)], [
    0 for i in range(1, 11)]]
my_c = [[0 for i in range(1, 11)], [0 for i in range(1, 11)], [
    0 for i in range(1, 11)]]
my_d = [[0 for i in range(1, 11)], [0 for i in range(1, 11)], [
    0 for i in range(1, 11)]]
bs = [my_a, my_b, my_c, my_d]

for i in range(n):
    num_str = input().split()
    b, f, r, v = [int(i) - 1 for i in num_str]
    bs[b][f][r] = bs[b][f][r] + v + 1

for i in range(len(bs)):
    for j in range(len(bs[0])):
        print(" ", end="")
        tmp_str = [str(i) for i in bs[i][j]]
        print(" ".join(tmp_str))
    if i != len(bs)-1:
        print("####################")
