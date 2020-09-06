num_str = input().split()
N, M, Q = [int(n) for n in num_str]
status = []
for i in range(M):
    status.append([0] * N)
score = 0
score_list = [0] * M

for i in range(Q):
    row = input().split()
    row_i = [int(n) for n in row]

    if len(row_i) == 2:
        n = row_i[1]
        for j in range(M):
           # print("status is " + str(status[j][n-1]))
            if status[j][n-1] != 0:
             #       score = score + N - sum(status[j])
               # print("score is " + str(score))
               # print("score_list[j] is  " + str(score_list[j]))
               # print("N is " + str(N))
                score = score + N - score_list[j]
        print(score)
        score = 0
    else:
        n = row_i[1]
        m = row_i[2]
        status[m - 1][n - 1] = 1
        score_list[m-1] += 1
