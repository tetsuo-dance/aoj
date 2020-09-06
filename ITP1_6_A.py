n = int(input())
num_str = input().split()
nums = [int(i) for i in num_str]
s = reversed(nums)
nums_str = [str(i) for i in s]
print(" ".join(nums_str))


