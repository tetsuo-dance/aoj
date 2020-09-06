# while True:
#    s = input().split()
#    a = int(s[0])
#    op = s[1]
#    b = int(s[2])
#    if op == "+":
#        print(a + b)
#    elif op == "-":
#        print(a - b)
#    elif op == "/":
#        print(a // b)
#    elif op == "*":
#        print(a * b)
#    else:
#        break
#

while True:
    s = input()
    s = s.replace('/', '//')
    if "?" in s:
        break
    else:
        print(eval(s))
