#Create an abstract class Employee that contains, Encapsulated attributes _name and
# _salary and an abstract method calculate_bonus(). Create a Manager subclass and
# a Developer subclass.Calculate the bonus for manager and developer.
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calc_bonus(self):
            pass
    def __init__(self, name, salary):
        self._name = name
        self.__salary = salary
    def get_salary(self):
        return self.__salary

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name,salary)
    def calc_bonus(self):
        bonus = int(self.get_salary() * (20/100))
        return bonus

class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def calc_bonus(self):
        bonus = int(self.get_salary() * (10/100))
        return bonus

manager = Manager("John", 20000)
employee = Developer("Kumar", 10000)
print(f"Bonus for the Manager {manager._name} is {manager.calc_bonus()}")
print(f"Bonus for the Employee {employee._name} is {employee.calc_bonus()}")
