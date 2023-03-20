dict1 = {
    "A": [20, 30, 100, 49],
    "B": [00, 199, 201, 29],
    "C": [40, 90, 69, 18]
}

key = None
max_range = -1

for k, l in dict1.items():
    mn, mx = min(*l), max(*l)
    if mx - mn > max_range:
        max_range = mx - mn
        key = k

print(key)
