def measure_center(values):
    if not values:
        return 0, 0, 0
    values = sorted(values)
    n = len(values)

    mean = sum(values) / n

    if n % 2:
        median = values[n//2]
    else:
        median = (values[n//2] + values[n//2 - 1]) / 2

    frequency = {}
    for v in values:
        if v not in frequency:
            frequency[v] = 0
        frequency[v] += 1

    max_frequency = 0
    mode = -1
    for v, fr in frequency.items():
        if fr > max_frequency:
            max_frequency = fr
            mode = v

    assert mode != -1
    return mean, median, mode


if __name__ == "__main__":
    try:
        values = [float(x) for x in input().split()]
        mean, median, mode = measure_center(values)
        print(f"mean: {mean:.3f}")
        print(f"median: {median}")
        print(f"mode: {mode}")
    except ValueError:
        print("You should input valid numbers")
    except KeyboardInterrupt:
        pass
