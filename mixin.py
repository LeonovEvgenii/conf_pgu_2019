from pyDatalog import pyDatalog
import sys

pyDatalog.create_terms('X, Y, Z, N')

class Associate(pyDatalog.Mixin):
    
    def __init__(self, name, bind): 
        super(Associate, self).__init__()
        self.name = name
        self.bind = bind     
    
    def __repr__(self):
        return self.name

q = Associate('q', None)
w = Associate('w', q)
e = Associate('e', w)
# r = Associate('r', e)
# t = Associate('t', r)
# y = Associate('y', t)



Associate.indirect_manager(X,Y, N) <= (Associate.bind[X]==Y) & (Y != None) & (N>0)
Associate.indirect_manager(X,Y, N) <= (Associate.bind[X]==Z) & Associate.indirect_manager(Z,Y, N-1) & (Y != None) & (N>0)

print(Associate.indirect_manager(X,Y, int(sys.argv[1])))


# Employee.indirect_manager(X,Y) <= (Employee.manager[X]==Y) & (Y != None)
# Employee.indirect_manager(X,Y) <= (Employee.manager[X]==Z) & Employee.indirect_manager(Z,Y) & (Y != None)


# print(Employee.indirect_manager(X,Y))
