nums = [int(x) for x in input().split()]

symmetric = True

n = len(nums)
for i in range(n // 2):
    symmetric = symmetric and nums[i] == nums[-i - 1]

if symmetric:
    print("YES")
else:
    print("NO")
