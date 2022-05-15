# def function1():
#     print("Subscribe now")
# func2 = function1
# del function1
# func2()
# from pyclbr import Function


# # Function in Function
# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# a = funcret(1)
# print(a)

# def executor(func):
#     func("this is valid")
# executor(print)

# what is Decorator ?
# def dec1(func1):
#     def nowexec():
#         print("Subscribe Now")
#         func1()
#         print("Subscribed")
#     return nowexec

# Iterables, Iterators, Generators

# def gen(n):
#     for i in range(n):
#         yield i

# g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

z = "sarfraz khan"
h = iter(z)
print(h.__next__())
print(h.__next__())
print(h.__next__())
print(h.__next__())
print(h.__next__())
print(h.__next__())
print(h.__next__())
print(h.__next__())
print(h.__next__())
print(h.__next__())