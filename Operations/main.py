# todo: Toán tử số học - arithmetic operations
# / => chia không làm tròn
# // => chia làm tròn
print(10 / 3)
print(10 // 3)

# % => lấy số dư
print(10 % 3)

# ** => mũ
print(10 ** 3)
print(10 ** 2)

# +=, -=, *=, /=
x = 10
x = x + 3
print(x)
x += 3
print(x)

# todo: Đọ ưu tiên của toán tử
# 1.parenthesis(nhóm ()) => (2+3) * 2
# 2.Exponentiation(mũ) => 2**3
# 3.Multiplication(nhân) or Division(chia) => 2*3 or 2/3
# 4.Addition(cộng) or subtraction(trừ) => 2+3 or 2-3
x = 10 + 3 * 2 ** 2
print(x)

# todo: Toán tử logic - logical operators
has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
    print("And")

if has_high_income or has_good_credit:
    print("Or")

# todo: Toán tử so sánh - comparison operators
# 1. > lớn hơn
# 2. < nhỏ hơn
# 3. == bằng
# 4. != không =

age = 18
if age >= 18:
    print("Trưởng thành")
else:
    print("Vị thành niên")


