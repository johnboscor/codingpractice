
class Test:
    def printf(self):
        print("Hello, how are you?")

test1 = Test()
test1.printf()

class Boat:
    def __init__(self,
                 x,
                 y):
        self.color = x;
        self.price = y;

    def colors(self):
        print(f"Color of boat is {self.color}")

    def prices(self):
            print(f"Price of boat is ${self.price}")


myboat = Boat("Red",1000)
myboat.colors()
myboat.prices()

myboat = Boat("Yellow",15340)
myboat.colors()
myboat.prices()