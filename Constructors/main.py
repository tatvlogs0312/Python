# todo: constructor
class Point:

    # constructor trong python
    # self giống this trong java => dùng để tham chiếu đến biến của class
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.x)
point.x = 15
print(point.x)


#
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("hello " + self.name)


tuan = Person("tuấn")
print(tuan.name)
tuan.talk()
