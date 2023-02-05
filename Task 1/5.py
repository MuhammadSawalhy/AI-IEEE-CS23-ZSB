strings = input().split()

first_half = []
second_half = []

for s in strings:
    first_half.append(s[:(len(s) + 1)//2]) # round up in case of odd length
    second_half.append(s[(len(s) + 1)//2:])
print(first_half)
print(second_half)
