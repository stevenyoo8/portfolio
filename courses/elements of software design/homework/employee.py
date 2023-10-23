#  File: Employee.py
#  Student Name: Jongho Yoo
#  Student UT EID: jy23294

#  Description: Display employee descriptions


# general employee info: name, id, and salary
class Employee:
    # initializer
    def __init__(self, **kwargs):
        self._name = kwargs.get("name", None) # get variable of the 'name' keyword if supplied. If not, default to 'None'
        self._id = kwargs.get("id", None)
        self._salary = kwargs.get("salary", None)

    # allows the 'salary' variable to be retrieved (getter)
    @property
    def salary(self):
        return self._salary

    # set the salary
    @salary.setter
    def salary(self, salary):
        self._salary = salary

    # 'name' variable getter
    @property
    def name(self):
        return self._name
    
    # 'id' variable getter
    @property
    def id(self):
        return self._id

    
    # print results
    def __str__(self):
        print("Employee")
        return str(self._name) + ", " + str(self._id) + ", " + str(self._salary)
    


# add benefits to employees and calculate adjusted salary
class Permanent_Employee(Employee): # derived class of 'Employees' base class
    # initializer
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # initialize using 'Employees' (base) class initializer
        self._benefits = kwargs.get("benefits", None)

    # calculate salary based on benefits employee has
    def cal_salary(self):
        pass
        if self._benefits == ["health_insurance"]:
            return self._salary * 0.9
        elif self._benefits == ["retirement"]:
            return self._salary * 0.8
        elif self._benefits == ["retirement", "health_insurance"]:
            return self._salary * 0.7
        else:
            return self._salary

    # 'benefits' variable getter
    @property
    def benefits(self):
        return self._benefits

    # 'benefits' setter
    @benefits.setter
    def benefits(self, benefits):
        self._benefits = benefits

    # print results
    def __str__(self):
        print("Permanent_Employee")
        return str(self._name) + ", " + str(self._id) + ", " + str(self._salary) + ", " + str(self._benefits)



# Derived from Employee class. Managers additionaly have a bonus
class Manager(Employee):
    # initializer
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._bonus = kwargs.get("bonus", None)

    # calculate salary with bonus
    def cal_salary(self):
        return self._salary + self._bonus

    # 'bonus' getter
    @property
    def bonus(self):
        return self._bonus

    # print results
    def __str__(self):
        print("Manager")
        return str(self._name) + ", " + str(self._id) + ", " + str(self._salary) + ", " + str(self._bonus)



# Derived from Employee class. Temporary employees work on an hourly rate. Add the 'hours' variable
class Temporary_Employee(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._hours = kwargs.get("hours", None)

    # calculate salary based on hours worked
    def cal_salary(self):
        return self._salary * self._hours

    # print results
    def __str__(self):
        print("Temporary_Employee")
        return str(self._name) + ", " + str(self._id) + ", " + str(self._salary) +  ", " + str(self._hours)



# Derived from Temporary Employee class. Consultants additionally have trips. Add 'trips' variable
class Consultant(Temporary_Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._trips = kwargs.get("travel", None)

    # calculate salary based on hours worked and trips taken
    def cal_salary(self):
        return (self._salary * self._hours) + (self._trips * 1000)

    # print results
    def __str__(self):
        print("Consultant")
        return str(self._name) + ", " + str(self._id) + ", " + str(self._salary) + ", " + str(self._hours) + ", " + str(self._trips)
        


# Derived from 'Consultant' and 'Manager' classes. No new variables to be added.
class Consultant_Manager(Consultant, Manager):
    def __init__(self,  **kwargs):
        super().__init__(**kwargs) # refers to both base classes ('Consultant' and 'Manager') as defined in the class' arguments

    # calculate salary based on hours worked, trips taken, and bonus
    def cal_salary(self):
        return (self._salary * self._hours) + (self._trips * 1000) + (self._bonus)

    # print bonus
    def __str__(self):
        print("Consultant_Manager")
        return str(self._name) + ", " + str(self._id) + ", " + str(self._salary) + ", " + str(self._hours) + ", " + str(self._trips) + ", " + "Consultant_Manager\n" +  str(self._name) + ", " + str(self._id) + ", " + str(self._salary) + ", " + str(self._bonus)



''' ##### DRIVER CODE ##### '''

def main():

    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary())

    print("Sam's Salary is:", sam.cal_salary())

    print("John's Salary is:", john.cal_salary())

    print("Charlotte's Salary is:", charlotte.cal_salary())

    print("Matt's Salary is:",  matt.cal_salary())


if __name__ == "__main__":
    main()
