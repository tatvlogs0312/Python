import random

a = random.random()
print(a)

for i in range(2, 5):
    print(random.randint(10, 20))

members = ['John', 'Lisa', 'Jane', 'Mosh', 'Bob']
print(members[random.randint(0, len(members)) - 1])


class Dice:

    # def __init__(self, first, second):
    #     self.first = first
    #     self.second = second

    def roll(self):
        first = random.randint(1, 6)
        last = random.randint(1, 6)
        return (first, last)


dice = Dice()
print(dice.roll())
