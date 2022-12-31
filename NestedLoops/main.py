for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

# c1
for x in range(5):
    if x == 0 or x == 2:
        print("xxxxx")
    else:
        print("xx")

# c2
numbers = [5, 2, 5, 2, 2]
for item in numbers:
    print('X' * item)

# c3
for x in numbers:
    out = ''
    for y in range(x):
        out += 'X'
    print(out)
