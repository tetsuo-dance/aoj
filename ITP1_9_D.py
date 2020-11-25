my_str = input()
q = int(input())

for i in range(q):
    row = input().split()

    if row[0] == "print":
        print(my_str[int(row[1]):int(row[2]) + 1])
    elif row[0] == "reverse":
        my_str_list = list(my_str)
        my_str_list[int(row[1]):int(
            row[2]) + 1] = ''.join(list(reversed(my_str[int(row[1]):int(row[2]) + 1])))
        my_str = "".join(my_str_list)
    else:
        # my_str = my_str.replace(
        #    my_str[int(row[1]):int(row[2]) + 1], row[3])
        my_str_list = list(my_str)
        my_str_list[int(row[1]):int(row[2]) + 1] = row[3]
        my_str = "".join(my_str_list)
