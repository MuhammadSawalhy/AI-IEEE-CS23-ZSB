nums = [int(x) for x in input().split()]
target = int(input())

indices = dict()

for i, v in enumerate(nums):
    if (target - v) in indices:
        print(f"{indices[target - v]}, {i}")
        exit()
    if v not in indices:
        indices[v] = i

