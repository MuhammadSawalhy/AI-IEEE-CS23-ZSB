def sort(nums):
    nums.sort()


def get_2_occurences(nums: list[int], value):
    nums.sort()
    j = nums.index(value)
    k = len(nums) - 1 - nums[::-1].index(value)
    if j == k:
        raise ValueError("one occurence of the value")

    return j, k


if __name__ == "__main__":
    try:
        nums = [int(x) for x in input().split()]
        sort(nums)
        value = int(input())
    except ValueError:
        print("Oops! you should input valid numbers")
        exit(1)
    except KeyboardInterrupt:
        exit(1)

    try:
        j, k = get_2_occurences(nums, value)
        print(f"{j} {k}")
    except ValueError:
        print("Oops! we can't find two occurences of the value: " + str(value))
        exit(1)
