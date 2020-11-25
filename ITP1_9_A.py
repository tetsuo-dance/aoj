W = input()
count = 0

while True:
    T = input()
    if T == "END_OF_TEXT":
        break
    list_T = T.lower().split()
    count += list_T.count(W)

print(count)
