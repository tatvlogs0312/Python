# todo: Inheritance

class Mammal:
    def walk(self):
        print("walk")


# pass => dùng để bỏ qua
class Lion(Mammal):
    pass


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("be_annoying")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.be_annoying()

mammal = Mammal()
mammal.walk()
