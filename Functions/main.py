# todo: function

# function không tham số
def greet_user():
    print("hi there")


greet_user()


# function có tham số
def sum(a, b):
    return a + b


# c1: truyền theo thứ tự
a = 5
b = 4
print(sum(b=4, a=5))


def calc(c, d, e):
    return c + d + e


# c2 truyền theo tên biến
print(calc(d=2, c=3, e=1))
