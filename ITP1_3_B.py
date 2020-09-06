
x = []
while True:
    val = int(input())
    if val == 0:
        break
    x.append(val)

for i in range(len(x)):
    print("Case {0}: {1}".format(i + 1, x[i]))
