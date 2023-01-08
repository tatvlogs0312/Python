# todo: exception

try:
    age = int(input("Age : "))
    income = 20000
    rick = income / age
    print(age)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Age cannot be 0")


try:
    a = int(input("Nhập a : "))
    print(a)
except Exception:
    print('ERROR')
