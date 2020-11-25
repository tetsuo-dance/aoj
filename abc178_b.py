str = input().split()
a,b,c,d = [int(i) for i in str]

ans_list = [a * c, a * d, b * c, b * d]

print(max(ans_list))