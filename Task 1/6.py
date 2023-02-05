people = []
people.extend(input().split(","))
people.extend(input().split(","))

d = dict()

for p in people:
    name, age = p.split(":")
    d[name] = int(age)

print(d)
