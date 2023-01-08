# todo: class
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
# tạo biến không lưu vào class như dict
point1.x = 10
print(point1.x)

point1.draw()
point1.move()
