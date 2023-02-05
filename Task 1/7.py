nums = [int(x) for x in input().split()]
k = int(input())

n = len(nums)
rotated = [0] * n
for i in range(n):
    rotated[i] = nums[i - k]

print(rotated)

