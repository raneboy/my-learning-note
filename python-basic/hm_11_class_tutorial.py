class Cat:

    def __init__(self, name):
        print("New cat is here")
        self.name = name

    def eat(self):
        print("%s is eating" % self.name)

    @staticmethod
    def drink():
        print("The cat is drinking")


if __name__ == "__main__":
    cat1 = Cat("Tom")
    cat1.drink()

