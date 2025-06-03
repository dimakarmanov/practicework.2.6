class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"\nИмя: {self.name}, возраст: {self.age}")

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Я собака")

class Cat(Animal):
    def speak(self):
        print("Я кошка")

dog = Dog("Макс", 1)
dog.info()
dog.speak()

cat = Cat("Муся", 1)
cat.info()
cat.speak()