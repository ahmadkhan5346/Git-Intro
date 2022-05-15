class Employee:
    no_of_leaves = 8
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    def ahmad(self):
        return f"Name is {self.name} Salary is {self.salary} role is {self.role}"
    
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        # param = string.split("-")
        # return cls(param[0], param[1], param[2])
        return cls(*string.split("-"))

staticmethod
def printgood(string):
    print("This is good" + string)


harry = Employee("Harry", 300, "Instructor")
rohan = Employee("Rohan", 400, "Student")
karan = Employee.from_dash("karan-480-student")

# print(karan.salary)
# print(harry.salary, rohan.role)
# harry.change_leaves(34)
# print(harry.no_of_leaves)

Employee.printgood("Harry")