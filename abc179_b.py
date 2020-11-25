N = int(input())
count = 0
ans = "No"

for i in range(N):
  d1, d2 = input().split()
  if d1 == d2:
      count = count + 1
  else:
      count = 0
  if count == 3:
      ans = "Yes"

print(ans)

