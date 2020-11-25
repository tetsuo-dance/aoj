str = input()

length = len(str)

if str[length - 1] == 's':
    print(str + 'es')
else:
    print(str + 's')
