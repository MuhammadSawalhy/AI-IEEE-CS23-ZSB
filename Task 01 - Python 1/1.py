nums = list(set([int(x) for x in input().split()]))
nums.sort()

if len(nums) < 2:
    print("You should enter at least 2 distinct numbers")
    exit()

print(nums[-2])
print(nums[1])

