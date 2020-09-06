# math.powは扱える桁数に上限があるから不可
#import math
#A, R, N = input().split()
##ans = int(A) * int(math.pow(int(R), int(N) - 1))
#ans = int(A) * (int(R) ** (int(N) - 1))
# if ans > 1000000000:
#    print('large')
# else:
#    print(ans)
#
val = input().split()
A, R, N = [int(i) for i in val]

if N > 31:
    if R == 1:
        print(A)
    else:
        print('large')
else:
    ans = A * (R ** (N - 1))
    if ans > 10 ** 9:
        print('large')
    else:
        print(ans)
