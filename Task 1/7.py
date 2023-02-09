nums = [int(x) for x in input().split()]
k = int(input())

k %= len(nums)
rotated = nums[-k:] + nums[:-k]

print(rotated)

