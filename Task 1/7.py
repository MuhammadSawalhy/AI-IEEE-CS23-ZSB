nums = [int(x) for x in input().split()]
k = int(input())

n = len(nums)
k %= n
rotated = nums[-k:] + nums[:n-k]

print(rotated)

