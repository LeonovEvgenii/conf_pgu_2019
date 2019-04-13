
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
латы = Associate('латы', дерево)
век = Associate('век', латы)
нагрудник = Associate('нагрудник', латы)
лата = Associate('лата', латы)
конец = Associate('конец', латы)
листы = Associate('листы', дерево)
высота = Associate('высота', дерево)
дерева = Associate('дерева', дерево)
название = Associate('название', дерева)
дерево = Associate('дерево', дерева)
яблоня = Associate('яблоня', дерево)
яблоко = Associate('яблоко', яблоня)
плоды = Associate('плоды', яблоня)
вид = Associate('вид', яблоня)
сорт = Associate('сорт', яблоня)
сады = Associate('сады', яблоня)
плод = Associate('плод', яблоня)
плод = Associate('плод', дерево)
плоды = Associate('плоды', плод)
латы = Associate('латы', плод)
созревание = Associate('созревание', плод)
завязь = Associate('завязь', плод)
участие = Associate('участие', плод)
гинецей = Associate('гинецей', плод)
ягода = Associate('ягода', плод)
часть = Associate('часть', плод)
околоплодник = Associate('околоплодник', плод)
миндаль = Associate('миндаль', дерево)
ядро = Associate('ядро', миндаль)
скорлупа = Associate('скорлупа', миндаль)
орехи = Associate('орехи', миндаль)
метры = Associate('метры', дерево)
цветки = Associate('цветки', дерево)
цветок = Associate('цветок', цветки)
тычинка = Associate('тычинка', цветки)
венчик = Associate('венчик', цветки)
пестики = Associate('пестики', цветки)
члены = Associate('члены', цветки)
чашелистики = Associate('чашелистики', цветки)
чашечка = Associate('чашечка', цветки)
цветоложе = Associate('цветоложе', цветки)
пестик = Associate('пестик', цветки)

Associate.indirect_manager(X,Y, N) <= (Associate.bind[X]==Y) & (Y != None) & (N>0)
Associate.indirect_manager(X,Y, N) <= (Associate.bind[X]==Z) & Associate.indirect_manager(Z,Y, N-1) & (Y != None) & (N>0)

print(Associate.indirect_manager(X, дерево, 1))
