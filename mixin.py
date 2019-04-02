from pyDatalog import pyDatalog 

pyDatalog.create_terms('X, Y, Z')

class Associate(pyDatalog.Mixin):
    
    def __init__(self, left, right): 
        super(Associate, self).__init__()
        self.left = left
        self.right = right     
    
    def __repr__(self):
        return self.left+' -> '+self.right

q_w = Associate('q', 'w')
w_e = Associate('w', 'e')
e_r = Associate('e', 'r')
r_t = Associate('r', 't')
t_y = Associate('t', 'y')


Associate.indirect_manager(X,Y) <= (Associate.left[X]==Y) & (Y != None)
# Associate.indirect_manager(X,Y) <= (Associate.left[X]==Z) & Associate.indirect_manager(Z,Y) & (Y != None)

print(Associate.indirect_manager(X,Y))


# Employee.indirect_manager(X,Y) <= (Employee.manager[X]==Y) & (Y != None)
# Employee.indirect_manager(X,Y) <= (Employee.manager[X]==Z) & Employee.indirect_manager(Z,Y) & (Y != None)


# print(Employee.indirect_manager(X,Y))



























# print(Associate.left[X] == 'q')
