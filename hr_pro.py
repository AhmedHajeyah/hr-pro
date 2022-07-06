from datetime import datetime


class Employee:
   #Employee class here
    def __init__ (self, name, age,salary,employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year
    def get_working_years(self):
        return datetime.now().year - self.employment_year

employee1 = Employee("Ahmad", 30, 5000, 2015)
employee2 = Employee("Omar", 25, 6000, 2016)


class Manager(Employee):
    #Manager class here
    def __init__(self, name, age, salary, employment_year, bonus_percentage):
        super().__init__(name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage
    def get_bonus(self):
        return self.bonus_percentage * self.salary
    def get_working_years(self):
        return datetime.now().year - self.employment_year    

manager1 = Manager("Barrak", 35, 7000, 2017, 0.1)
manager2 = Manager("Mohammed", 40, 8000, 2018, 0.2)


        
def main():
	# main code here
    def __str__(self):
        return "Name: {}, Age: {}, Salary: {}, Employment year: {}, Bonus: {}".format(self.name, self.age, self.salary, self.employment_year, self.get_bonus())
    print(employee1.name)
    print(employee1.age)
    print(employee1.salary)
    print(employee1.employment_year)
    print(employee1.get_working_years())
    print(manager1.name)
    print(manager1.age)
    print(manager1.salary)
    print(manager1.employment_year)
    print(manager1.get_bonus())
    print(manager1.get_working_years())
    

    
if __name__ == '__main__':
	main()
