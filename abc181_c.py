import math
N = int(input())
points = []
ans = "No"
flag = False

for i in range(N):
    tmp_str = input().split()
    x, y = [int(i) for i in tmp_str]
    points.append((x, y))

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][1]
            x3 = points[k][0]
            y3 = points[k][1]
            x2 -= x1
            x3 -= x1
            y2 -= y1
            y3 -= y1
            if x2 * y3 == x3 * y2:
                ans = "Yes"
                flag = True
                break
        if flag:
            break
    if flag:
        break

print(ans)
