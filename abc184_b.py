tmp_str = input().split()
N, X = [int(i) for i in tmp_str]
S = input()

for i in range(N):
    if S[i] == "o":
        X += 1
    else:
        if X != 0:
            X -= 1

print(X)
