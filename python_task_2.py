objects = [1, 2, 1, 2, 3, True, False, "true", '1', True]
ans = 0
s = set()
print("set: ", s)
for obj in objects:
    s.add(id(obj))

print(s)
