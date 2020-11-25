N = int(input())
tmp_str = input().split()
A = [int(i) for i in tmp_str]
now = 0
max_ans = 0
moved = 0
max_move = 0

for i in range(N):
    moved += A[i]
    if max_move < moved:
        max_move = moved
    if max_ans < now + max_move:
        max_ans = now + max_move
    now = now + moved
print(max_ans)
