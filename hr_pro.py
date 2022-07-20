from datetime import datetime


class Employee:
   #Employee class here
    def __init__ (self, name, age,salary,employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year
    def get_working_years(self):
        working_years = datetime.now().year - int(self.employment_year)
        return working_years

#employee1 = Employee("Ahmad", 30, 5000, 2015)
#employee2 = Employee("Omar", 25, 6000, 2016)
employee_list = []
employee_list.append(Employee("Ahmad", 30, 5000, 2015))
employee_list.append(Employee("Omar", 25, 6000, 2016))


class Manager(Employee):
    #Manager class here
    def __init__(self, name, age, salary, employment_year, bonus):
        super().__init__(name, age, salary, employment_year)
        self.bonus_percentage = bonus
    def get_bonus(self):
        bonus= self.bonus_percentage * self.salary
        return bonus
    def get_working_years(self):
        working_years= datetime.now().year - int(self.employment_year)
        return working_years
        

#manager1 = Manager("Barrak", 35, 7000, 2017, 0.1)
#manager2 = Manager("Mohammed", 40, 8000, 2018, 0.2)
managers_list = []
managers_list.append(Manager("Mohammed", 40, 8000, 2018, 0.2))
managers_list.append(Manager("Barrak", 35, 7000, 2017, 0.1))


def main():
    # main code here
    user_choice = 0
    print("Welcome to HR Pro 2022")
    while user_choice != 5:
        print("Options:")
        print("1. Show Employees")
        print("2. Show Managers")
        print("3. Add An Employee")
        print("4. Add A Manager")
        print("5. Exit")

        user_choice = int(input("What would you like to do?"))
        if user_choice == 1:
            print("Employees")
            for i in range(len(employee_list)):
                print(
                    f"Name: {employee_list[i].name}, Age: {employee_list[i].age}, Salary: {employee_list[i].salary},Working Years: {employee_list[i].get_working_years()}")
        elif user_choice == 2:
            print("Managers")
            for i in range(len(managers_list)):
                print(
                    f"Name: {managers_list[i].name}, Age: {managers_list[i].age}, Salary: {managers_list[i].salary},Working Years: {managers_list[i].get_working_years()}, Bonus: {managers_list[i].get_bonus()}")
        elif user_choice == 3:
            name = input("Name:")
            age = int(input("Age:"))
            salary = int(input("Salary:"))
            employment_year = input("Employement year:")
            employee_list.append(Employee(name, age, salary, employment_year))
            print("Employee added succesfully")
        elif user_choice == 4:
            name = input("Name:")
            age = int(input("Age:"))
            salary = int(input("Salary:"))
            employment_year = input("Employement year:")
            bonus_persentage = input("Bonus Percentage:")
            managers_list.append(Manager(name, age, salary, employment_year, bonus_persentage))
            print("Manager added succesfully")


if __name__ == '__main__':
    main()