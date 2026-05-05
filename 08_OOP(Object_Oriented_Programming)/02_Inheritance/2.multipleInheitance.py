class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def introduce(self):
        print(f"Hi, My name is {self.first_name} {self.last_name}, Age: {self.age}")


class Employee:
    def __init__(self, position, salary):
        self.position = position
        self.salary = salary

    def work(self):
        print(f"Working as {self.position} and earning {self.salary}")


class Manager(Person, Employee):
    def __init__(self, first_name, last_name, age, position, salary):
        Person.__init__(self, first_name, last_name, age)
        Employee.__init__(self, position, salary)


# Create object
manager = Manager("Zafrin", "Chowdhury", 20, "Manager", 35000)

manager.introduce()
manager.work()