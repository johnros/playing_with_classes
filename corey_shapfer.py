# Following https://www.youtube.com/watch?v=ZDa-Z5JzLYM

#%% The naive approach
class Employee():
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Corey'
emp_1.last = 'Shapfer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'



#%% Instance variables
class Employee():
    
    def __init__(self, first, last, pay):
        # Setting instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email  = first + '.' + last + '@company.com'

emp_1 = Employee('Corey', 'Shapfer', 50000)
emp_2 = Employee('Test', 'User', 60000)

dir(emp_1)



#%% Methods 
f'{emp_1.first} {emp_1.last}'

class Employee():
    
    def __init__(self, first, last, pay):
        # Setting instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email  = first + '.' + last + '@company.com'
    
    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('Corey', 'Shapfer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_1.fullname()



#%% Class variables
class Employee():
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        # Setting instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email  = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1 
    
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Shapfer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps)




#%% Class/Static methods

class Employee():
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        # Setting instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email  = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1 
    
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    # Unlike a regular method, a class method takes the class as the first argument
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        

emp_1 = Employee('Corey', 'Shapfer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# Run the class method from the class
Employee.set_raise_amount(1.05)
emp_1.raise_amount

# Run the class method from the instance (works, but logicallty wierd)
emp_1.set_raise_amount(1.06)
emp_2.raise_amount




#%% Class method as alternative constructor

class Employee():
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        # Setting instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email  = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1 
    
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    # Unlike a regular method, a class method takes the class as the first argument
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False    
        return True

emp_1 = Employee.from_string('John-Doe-70000')
emp_1.fullname()

import datetime
emp_1.is_workday(datetime.date(2016, 7, 10))


#%% Static methods
# Static methods don't pass anything automatically
# They behave like regular functions, but belong to the class
# They don't have access to the class or instance
# They are used to group methods/functions together that have some logical connection
# They are used to perform operations that have some logical connection with the class


