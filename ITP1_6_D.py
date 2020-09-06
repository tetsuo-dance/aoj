num_str = input().split()
n, m = [int(i) for i in num_str]
count = 0

Mat = []
Vec = []

for i in range(n):
    row = input().split()
    row_i = [int(i) for i in row]
    Mat.append(row_i)

for i in range(m):
    Vec.append(int(input()))

for i in range(n):
    tmp_list = [x * y for (x, y) in zip(Mat[i], Vec)]
    print(sum(tmp_list))
