tmp_str = input().split()
X, Y, A, B = [int(i) for i in tmp_str]
dp = X
count = 0

while True:
    if dp * A <= dp + B and dp * A < Y:
        dp = dp * A
        count += 1
    else:
        count += (Y - 1 - dp) // B
        break

print(count)
