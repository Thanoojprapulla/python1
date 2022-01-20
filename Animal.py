class Animal(object):
    def __int__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating %s" % (self.name, food))


class Dog(Animal):
    def fetch(self, thing):
        print("%s goes after the" % (self.name, thing))


class Cat(Animal):
    def swatstring(self):
        print("%s shred the string %s" % self.name)


d = Dog("Roger")
d = Cat("Fluffy")
d.fetch("paper")
d.eat("dog food")
d.swatstring("")
obj = Animal("")
obj.print_Animal()