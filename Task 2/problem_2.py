def get_nums():
    try:
        l = [int(x) for x in input().split()]
        return l
    except ValueError:
        print("You should enter valid numbers")
        exit(1)
    except KeyboardInterrupt:
        exit(1)


def count_evens(nums: list[int]):
    return len(list(filter(lambda x: x % 2 == 0, nums)))


if __name__ == "__main__":
    nums = get_nums()
    print(count_evens(nums))

