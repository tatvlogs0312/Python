# todo: print() => in ra màn hình
print("Hello world")

# todo: Biến - variable
# Giá trị của các biến giống được lấy ở biến khai cuối cùng
age = 20
age = 30
isLive = True
print(age)
print(isLive)

# todo: input() => cho phép người dùng nhập chuỗi từ bàn phím
name = input("Nhập tên của bạn : ")
print("Tên : " + name)

print("Nhập địa chỉ của bạn : ")
address = input()
print("Địa chỉ : " + address)

print(name + " đang ở " + address)

# todo: Ép kiểu
# Vì input() chỉ cho nhận kiểu dữ liệu string => tính toán số học phải ép kiểu
# Các loại ép kiểu : int() => số nguyên, float() => số thực, bool() => kiểu true-false, str() => kiểu chuỗi
a = input("Nhập a : ")
b = input("Nhập b : ")
aInt = int(a)
print(2002 + aInt)

print("a + 1 = " + str(aInt + 1))

sum = float(a) + float(b)
print("a + b = " + str(sum))
