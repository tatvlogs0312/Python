numbers = [1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]

# c1:
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)

# c2:
for number in numbers:
    if numbers.count(number) > 1:
        index = numbers.index(number)
        numbers.pop(index)

print(numbers)
