# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod
#     def hello():
#         print("Hello")

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "your avg score is :", sum / 3)


# s1 = Student("Vatsal", [90, 98, 99])
# s1.get_avg()

# s1.hello()


# class Account:
#     def __init__(self, balance, account_num):
#         self.balance = balance
#         self.account_num = account_num

#     def debit(self, amount):
#         self.balance -= amount
#         print("Amount debited", amount)

#     def credit(self, amount):
#         self.balance += amount
#         print("Amount credited", amount)


# class complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     def showNumber(self):
#         print(self.real, "i +", self.imag, "j")

#     def __add__(self, num2):
#         new_real = num1.real + num2.real
#         new_imag = num1.imag + num2.imag
#         return complex(new_real, new_imag)

#     def __sub__(self, num2):
#         new_real = num1.real - num2.real
#         new_imag = num1.imag - num2.imag
#         return complex(new_real, new_imag)


# num1 = complex(3, 4)
# num2 = complex(5, 6)
# num1.showNumber()

# num3 = num1 + num2
# num3.showNumber()


# class circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius**2

#     def perimeter(self):
#         return (22 / 7) * 2 * self.radius


# c = circle(4)

# print(c.area())
# print(c.perimeter())


# class Employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary

#     def showDetails(self):
#         print("Role:", self.role)
#         print("Department:", self.department)
#         print("Salary:", self.Salary)
        
        
#     class Engineer:
#         def __init__(self,name,age):
#             self.name = name
#             self.age = age
#             super().__init__("Engineer","IT",50000)


# class Order:
#     def __init__(self, item,price):
        


#  import pandas as pd

# def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
#     merged = employee.merge(department, left_on = 'departmentId',right_on = 'id',how = 'left')
#     highest_salary = merged.loc[merged.groupby('departmentId')['salary'].transform('max') == merged['salary']]
#     result = highest_salary[['name_x','salary','name_y']].rename(columns = {
#         'name_y': 'Department',
#         'name_x' : 'Employee',
#         'salary' : 'Salary'
#     })
#     return result[['Department','Employee','Salary']]

#     result = pd.merge(employee, department, on ='departmentId', how = 'left' )
#     return pd.DataFrame(result)       




from dbm.ndbm import library


Class library:

def __init__(self,books):
    self.books = books

def check_book(self,book):
    if book in self.books:
        return True
    else:
        return False