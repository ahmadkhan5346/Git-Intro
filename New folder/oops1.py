# class student:
#     pass
# sarfraz = student()
# ahmad = student()
# sarfraz.name = 'sarfraz'
# sarfraz.std = 'software'
# sarfraz.id_no = 101
# ahmad.subject = ['variable', 'string', 'oops'] 

# print(sarfraz.name, sarfraz.id_no, ahmad.subject)
# print(student.__dict__)

#Self & __init__() in python

class Employee:
    no_of_leaves = 8
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def ahmad(self):
        return f"Name is {self.name}. salary is {self.salary} and role is {self.role}"

harry = Employee('Harry',255,'Instructor')
rohan = Employee('rohan', 455, 'student')
print(harry.salary)

