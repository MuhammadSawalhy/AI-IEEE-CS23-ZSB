def get_nums():
    try:
        l = [int(x) for x in input().split()]
        if len(l) < 2:
            print("You should input at least two numbers")
            exit(1)
        return l
    except ValueError:
        print("You should enter valid numbers")
        exit(1)
    except KeyboardInterrupt:
        exit(1)


def get_max_min_sublists(nums):
    nums.sort()
    n = len(nums)
    i, j = 2, n - 2
    while i < n and nums[i] < 0:
        i += 1
    while j > 0 and nums[j - 1] > 0:
        j -= 1
    return nums[j:], nums[:i]


if __name__ == "__main__":
    nums = get_nums()
    max_sublist, min_sublist = get_max_min_sublists(nums)
    print(f"{max_sublist} ({sum(max_sublist)})")
    print(f"{min_sublist} ({sum(min_sublist)})")
