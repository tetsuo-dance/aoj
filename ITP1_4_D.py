n = int(input())
num_str = input().split()
nums = [int(i) for i in num_str]
print("{0} {1} {2}".format(min(nums), max(nums), sum(nums)))
