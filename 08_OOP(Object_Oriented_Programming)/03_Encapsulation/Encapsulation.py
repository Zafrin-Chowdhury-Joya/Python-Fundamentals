class Bank:
    def __init__(self):
        self.__max_salary = 10000
    def get_salary(self):
        print("Salary =", self.__max_salary)
    def setMaxSalary(self, max_salary):
        self.__max_salary = max_salary
bank = Bank()
bank.get_salary()
bank.setMaxSalary(20000)
bank.get_salary()

