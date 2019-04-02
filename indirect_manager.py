from pyDatalog import pyDatalog 

pyDatalog.create_terms('X, Y, Z')

class Employee(pyDatalog.Mixin):

     def __init__(self, name, manager, salary): 
        super(Employee, self).__init__()
        self.name = name
        self.manager = manager     
        self.salary = salary       

     def __repr__(self):
        return self.name

John = Employee('John', None, 6800)
Mary = Employee('Mary', John, 6300)
Sam = Employee('Sam', Mary, 5900)

Employee.indirect_manager(X,Y) <= (Employee.manager[X]==Y) & (Y != None)
Employee.indirect_manager(X,Y) <= (Employee.manager[X]==Z) & Employee.indirect_manager(Z,Y) & (Y != None)


print(Employee.indirect_manager(X,Y))