val = input().split()
s = [int(n) for n in val]
a = s[0]
b = s[1]
print("{0} {1} {2:.05f}".format(a // b, a % b, a/b))
