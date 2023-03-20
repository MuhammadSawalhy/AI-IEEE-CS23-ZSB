def median(values, start, end):
    """
    Parameters
    ----------
    values : list[float]
        original list of numbers to read values from

    start : int
        start index of numbers to consider (inclusive)

    end : int
        end index of numbers (non-inclusive)

    Returns
    -------
    float
        the median of numbers in `values` list in the range [start, end)
    """

    n = end - start
    i = start + n // 2

    if n % 2 == 0:
        j = i - 1
        return (values[i] + values[j]) / 2

    return values[i]


def five_number_summary(values):
    """
    Parameters
    ----------
    values : list[float]
        list of number to calculate their 5 number summary

    Returns
    -------
    (float, float, float, float, float)
        minimum, Q1, Q2, Q3, and maximum
    """

    values = sorted(values)

    n = len(values)
    Q1 = median(values, 0, n // 2)
    Q2 = median(values, 0, n)
    Q3 = median(values, (n + 1) // 2, n)

    return (values[0], Q1, Q2, Q3, values[-1])


def variance(values):
    """
    Parameters
    ----------
    values : list[float]
        list of nubmers to calculate their variance

    Returns
    -------
    float
        variance of values
    """

    n = len(values)
    mean = sum(values) / n
    numerator = sum((x - mean) ** 2 for x in values)
    return numerator / n


def std_deviation(values):
    """
    Parameters
    ----------
    values : list[float]
        list of nubmers to calculate their standard deviation

    Returns
    -------
    float
        standard deviation of values
    """

    return pow(variance(values), 0.5)


if __name__ == "__main__":
    values = list(map(int, input().split()))
    min, Q1, Q2, Q3, max = five_number_summary(values)

    print(f"min: {min}")
    print(f"Q1: {Q1}")
    print(f"Q2: {Q2}")
    print(f"Q3: {Q3}")
    print(f"max: {max}")
    print(f"range: {max - min}")
    print(f"IQR: {Q3 - Q1}")
    print(f"Variance: {variance(values):.3f}")
    print(f"Standard deviation: {std_deviation(values):.3f}")
