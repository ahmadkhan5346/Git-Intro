# class Employee:
#     no_of_leaves = 8

#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole

#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves

#     @classmethod
#     def from_dash(cls, string):
#         return cls(*string.split("-"))

#     @staticmethod
#     def printgood(string):
#         print("This is good " + string)

# harry = Employee("Harry", 255, "Instructor")
# rohan = Employee("Rohan", 455, "Student")
# karan = Employee.from_dash("Karan-480-Student")

# Employee.printgood("Harry")

class student:
    def __init__(self, name, percentage): # parameter to constructor
        self.name = name
        self.percentage = percentage  # Instance variable
    
    def show (self):   # Instance method
        print("Name is:", self.name, "and Percentage is:", self.percentage)

#  OBJECT CLASS
std=student("ahmad", 80)
std.show()