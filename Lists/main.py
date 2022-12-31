# todo: list

name = ['Thay Dat', 'Tuan', 'Nga', 'Dat', 'Hieu']
print(name)
print(name[2])
print(name[-3])
print(name[1:3])

# Tìm max
numbers = [0, 3, 2, 6, 4, 7, 1]

# c1
print(f"C1 - Max of numbers = {max(numbers)}")

# c2
max = numbers[0]
for x in numbers:
    if x >= max:
        max = x

print(f"C2 - Max of numbers = {max}")

# todo: các phương thức của list
lists = []

# 1: append(x) => thêm x vào cuối list
lists.append(1)
print(lists)
lists.append(2)
print(lists)
lists.append(3)
lists.append(4)
print(f"List sau khi thêm phần tử : {lists}")

# 2: remove(x) => xóa x ra khỏi list
lists.remove(2)
print(f"List sau khi xóa phần tử : {lists}")

# 3: list[x] => lấy giá trị ở index x
print(f"Giá trị của list ở index 0 : {lists[0]}")
print(f"Giá trị của list ở index 2 : {lists[2]}")
