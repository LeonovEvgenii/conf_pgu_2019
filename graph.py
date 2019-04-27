
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

дерево = Associate('дерево', None)
листы = Associate('листы', дерево)
плод = Associate('плод', дерево)
ягода = Associate('ягода', плод)
цветки = Associate('цветки', дерево)
тычинка = Associate('тычинка', цветки)
венчик = Associate('венчик', цветки)
пестик = Associate('пестик', цветки)
цветоножка = Associate('цветоножка', цветки)
лепестки = Associate('лепестки', цветки)
ствол = Associate('ствол', дерево)
побеги = Associate('побеги', дерево)
почки = Associate('почки', побеги)
листы = Associate('листы', побеги)
стебель = Associate('стебель', побеги)
цветки = Associate('цветки', побеги)

Associate.indirect_manager(X,Y, N) <= (Associate.bind[X]==Y) & (Y != None) & (N>0)
Associate.indirect_manager(X,Y, N) <= (Associate.bind[X]==Z) & Associate.indirect_manager(Z,Y, N-1) & (Y != None) & (N>0)

print(Associate.indirect_manager(X, дерево, 1))
