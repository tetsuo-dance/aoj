b = input().split()
s = [int(n) for n in b]
W = s[0]
H = s[1]
x = s[2]
y = s[3]
r = s[4]

if x + r <= W and y + r <= H and x - r >= 0 and y - r >= 0:
    print("Yes")
else:
    print("No")
