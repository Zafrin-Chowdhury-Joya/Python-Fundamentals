class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def display(self):
        return f"{self.brand} {self.model} {self.year}"
#Child Class
class Car(Vehicle):
    def __init__(self,brand,model,year,seating_capacity):
        super().__init__(brand, model, year)
        self.seating_capacity = seating_capacity
    def display(self):
        return f"Car Information : {self.brand} {self.model} {self.year} {self.seating_capacity}"
#Object Creation
car1 = Car("BMW","Mercedes",1999,5)
print(car1.display())
car2 = Car("BMW","Mar",2000,5)
print(car2.display())