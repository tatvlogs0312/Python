# todo: Chuỗi - strings
s = '''
Hello

My name is Tuấn
I'm 20 years old
'''
print(s)

course = 'Python For Beginners'
# len(s) => lấy độ dài của s
print("Độ dài chuỗi : " + str(len(course)))
# s[x] => lấy giá trị ở vị trí x <=> index
print("Giá trị ở index thứ 3 : " + course[3])
# s[-x] => lấy giá trị ở vị trí len(s) - x
print("Giá trị ở index thứ -3 : " + course[-3])
# s[x:y] => lấy giá trị từ index x đến index y
print("Giá trị từ 0 => 3 : " + course[0:3])
print("Giá trị từ đầu đến 3 : " + course[:3])
print("Giá trị từ 3 trở đi : " + course[3:])
print("Giá trị từ đầu đến cuối : " + course[:])
print("Giá trị từ 3 đến -3 : " + course[3:-3])
print("Giá trị từ -3 đến 3 : " + course[-3:3])

# todo: Formatted strings
first = 'Trần'
last = 'Tuấn'
msg1 = first + ' [' + last + '] is developer'
msg2 = f'{first} [{last}] is developer'
print(msg1)
print(msg2)

# todo: String method
# upper() => in hoa chuỗi
print("In hoa : " + course.upper())
# lower() => in thường chuỗi
print("In thường : " + course.lower())
# find(x) => tìm index của x
print("Vị trí của chữ F : " + str(course.find("F")))
# replace(x,y) => thay đổi x thành y
print(course.replace("For", "4"))
# in => kiểm tra phần tử có trong chuỗi không => true or false
print('Python' in course)
