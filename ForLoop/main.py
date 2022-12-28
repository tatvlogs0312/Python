# todo: for in python
for item in 'Python':
    print(item)

for item in ['Python', 'Java', 'C#', 'C++']:
    print(item)

for item in [1, 2, 3, 4]:
    print(item)

# range() => danh sách số nguyên từ x => y
for item in range(5, 10):
    print(item)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price

print("total : " + str(total))
print(f"total : {total}")
