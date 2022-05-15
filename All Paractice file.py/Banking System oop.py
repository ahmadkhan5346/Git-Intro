# #Banking System using 0OP

# #Parent Class : User
# #Holds detials about an user
# #Has a function to show user details

# #Child Class : Bank
# #Stores details about the account balance
# #Stores details about the amount
# #Allows for deposits, withdraw, view_balance

# #Parent Class
# class User():
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def show_details(self):
#         print("Personal Details")
#         print("")
#         print("Name", self.name)
#         print("Age", self.age)
#         print("Gender", self.gender)

# # Child Class
# class Bank(User):
#     def __init__(self, name, age, gender):
#         super().__init__(name, age, gender)
#         self.ballance = 0

#     def deposit(self,amount):
#         self.amount = amount
#         self.ballance = self.ballance + self.amount
#         print("Account ballance has been updated : $", self.ballance)

#     def withdraw(self,amount):
#         self.amount = amount
#         if (self.amount > self.ballance):
#             print("Insufficient Funds| Ballance Available : $", self.ballance)
#         else:
#             self.ballance = self.ballance-self.amount
#             print("Account ballance has been activated : $", self.ballance)
#     def view_ballance(self):
#         self.show_details()
#         print("account ballance : $", self.ballance)

# ahmad = Bank('Ahmad', 20, 'Male')
# ahmad.deposit(10000)
# ahmad.view_ballance()
# ahmad.withdraw(1001)
# ahmad.view_ballance()

#use bank account for user


class bank_accont():
    def __init__(self):
        self.amount = 0
    def deposit(self,Amount):
        self.amount+=Amount
        print("Amont Successfully Deposited")
    def withdraw(self,Amount):
        if (self.amount-Amount>=500):
            self.amount-=Amount
            print("Amount Successfully Withdrawn")
        else:
            print("Insufficient Ballance.\nYou have to keep atleast Rs.500 in Your Account")
    def display(self):
        print("Your Bank Ballance is:", self.amount)

a = bank_accont()
for i in range(0,50):
    print("1.Deposit 2.Withdraw 3.Display 4.Exit")
    p = int(input("Enter Your Choice:"))
    if (p==1):
        Amount=float(input("Enter Amount to be Deposit:"))
        a.deposit(Amount)
    elif (p==2):
        Amount=float(input("Enter Amount to be Withdrawn:"))
        a.withdraw(Amount)
    elif (p==3):
        a.display()
    elif (p==4):
        exit()
    else:
        print("You have Entered a Wrong Value")






