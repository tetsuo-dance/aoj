s = input()
p = input()
s = s + s[0:len(p) - 1]

if p in s:
    print('Yes')
else:
    print('No')
