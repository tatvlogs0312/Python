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
lists.append(5)
lists.append(6)
lists.append(7)
print(f"List sau khi thêm phần tử : {lists}")

# 2: insert(x,y) => thêm giá trị y vào vị trí x
lists.insert(0, 0)
print(f"List sau khi thêm phần tử 0 : {lists}")

# 3: remove(x) => xóa x ra khỏi list
lists.remove(2)
print(f"List sau khi xóa phần tử 2 : {lists}")

# 4: list[x] => lấy giá trị ở index x
print(f"Giá trị của list ở index 0 : {lists[0]}")
print(f"Giá trị của list ở index 2 : {lists[2]}")

# 5: list.index(x) => lấy index của x trong list
print(f"Vị trí của phần tử 1 trong list : {lists.index(1)}")
print(f"Vị trí của phần tử 5 trong list : {lists.index(5)}")

# 6: lists.count(x) => đếm số lượng x có trong list
print(f"Số lượng phần tử 2 có trong list : {lists.count(2)}")
print(f"Số lượng phần tử 5 có trong list : {lists.count(5)}")

# 7: list.pop() => xóa phần tử cuối cùng, list.pop(x) => xóa phần tử ở vị trí x
lists.pop()
print(f"List sau khi xóa phần tử cuối cùng : {lists}")

lists.pop(3)
print(f"List sau khi xóa phần tử ở vị trí 3 : {lists}")

# 8: list.clear() => xóa tất cả giá trị của list
lists.clear()
print(f"List sau khi clear : {lists}")

lists2 = [1, 4, 2, 3, 7, 5, 6]
# 9: list.sort() => sắp xếp list tăng dần
lists2.sort()
print(f"List sau khi sắp xếp tăng dần : {lists2}")

# 10: list.reverse() => sắp xếp list giảm dần
lists2.reverse()
print(f"List sau khi sắp xếp giảm dần : {lists2}")

# 11: copy() => copy toàn bộ phần tử từ list này sang list khác
lists3 = lists2.copy()
lists3.append(8)
print(f"List sau khi được copy : {lists3}")
