from pyDatalog import pyDatalog

pyDatalog.create_terms('X,Y,Z,N, associate, can_reach')

# + associate('дерево', 'латы')
# + associate('латы', 'металлические_пластины')
# + associate('латы', 'нагрудник')

# + associate('латы', 'лата')
# + associate('латы', 'конец')
# + associate('латы', 'форма_частей_тела_воина')
# + associate('латы', 'составляющая_часть_доспеха')
# + associate('латы', 'полный_латный_доспех')
# + associate('латы', 'латная_защита_конечностей')
# + associate('латы', 'coat_of_plates')
# + associate('латы', 'усиленное_подкладка')
# + associate('дерево', 'листы')
# + associate('листы', 'такие_название')
# + associate('листы', 'такая_страница')
# + associate('листы', 'быстрое_старт')
# + associate('листы', 'статья')
# + associate('листы', 'руководство')
# + associate('листы', 'википедия')
# + associate('дерево', 'дерево')
# + associate('дерево', 'латы')

# + associate('дерево', 'листы')

# + associate('дерево', 'дерево')
# + associate('дерево', 'высота')
# + associate('дерево', 'дерева')
# + associate('дерево', 'яблоня')
# + associate('дерево', 'плод')
# + associate('дерево', 'миндаль')
# + associate('дерево', 'метры')
# + associate('дерево', 'цветки')
# + associate('дерево', 'высота')
# + associate('высота', 'безопасная_высота')
# + associate('высота', 'высота')
# + associate('высота', 'толковый_словарь_ушакова')
# + associate('высота', 'понятия_техники_безопасности')
# + associate('высота', 'оба_других_измерения')
# + associate('высота', 'строительные_сооружение')
# + associate('высота', 'специальное_снаряжение')
# + associate('высота', 'проведение_работ')
# + associate('высота', 'неограждённый_перила')
# + associate('высота', 'медицинский_допуск')
# + associate('дерево', 'дерева')
# + associate('дерева', 'населённые_пункты')
# + associate('дерева', 'название')
# + associate('дерева', 'дерево')
# + associate('дерево', 'яблоня')
# + associate('яблоня', 'яблоня')
# + associate('яблоня', 'яблоко')
# + associate('яблоня', 'плоды')
# + associate('яблоня', 'дикорастущие_виды')
# + associate('яблоня', 'сорт')
# + associate('яблоня', 'сады')
# + associate('яблоня', 'плод')
# + associate('яблоня', 'яблоня_сиверса')
# + associate('яблоня', 'умеренный_климат')
# + associate('яблоня', 'яблоки')
# + associate('дерево', 'плод')
# + associate('плод', 'плоды')
# + associate('плод', 'латы')
# + associate('плод', 'семена')
# + associate('плод', 'плод')
# + associate('плод', 'созревание')
# + associate('плод', 'завязь')
# + associate('плод', 'участие')
# + associate('плод', 'гинецей')
# + associate('плод', 'ягода')
# + associate('плод', 'часть')
# + associate('дерево', 'миндаль')
# + associate('миндаль', 'миндаль')
# + associate('миндаль', 'горький')
# + associate('миндаль', 'prunus_dulcis_var')
# + associate('миндаль', 'первое_сорта')
# + associate('миндаль', 'кондитерские_изделия')
# + associate('миндаль', 'ядро')
# + associate('миндаль', 'скорлупа')
# + associate('миндаль', 'орехи')
# + associate('миндаль', 'тонкая_бархатистая_оболочка_косточки')
# + associate('миндаль', 'чистый_выход_миндаля')
# + associate('дерево', 'метры')
# + associate('метры', 'такие_название')
# + associate('метры', 'такая_страница')
# + associate('метры', 'быстрое_старт')
# + associate('метры', 'статья')
# + associate('метры', 'руководство')
# + associate('метры', 'википедия')
# + associate('дерево', 'цветки')
# + associate('цветки', 'цветок')
# + associate('цветки', 'тычинка')
# + associate('цветки', 'цветки')
# + associate('цветки', 'венчик')
# + associate('цветки', 'пестики')
# + associate('цветки', 'члены')
# + associate('цветки', 'чашелистики')
# + associate('цветки', 'чашечка')
# + associate('цветки', 'цветоложе')
# + associate('цветки', 'пестик')

+ associate('q', 'w')
+ associate('w', 'e')
+ associate('e', 'r')
+ associate('r', 't')
+ associate('t', 'y')


if __name__ == '__main__':
	import sys
	# import logging
	# from pyDatalog import pyEngine
	# pyEngine.Logging = True
	# logging.basicConfig(level=logging.INFO)
	
	can_reach(X, Y, N) <= associate(X, Y) & (N>0)
	can_reach(X, Y, 1) <= associate(X, Y)

	can_reach(X, Y, N) <= (can_reach(X, Z, N-1) & can_reach(Z, Y, N-1) & (X != Y) & N>0)
	
	print(can_reach('q', Y, 3))







##################

	# associate(X, Y) <= associate(Y, X)
	
	# can_reach(X, Y) <= associate(X, Y)

	# can_reach(X, Y, N) <= (can_reach(X, Z, N-1) & can_reach(Z, Y, N-1) & (X != Y))
	# print(can_reach(sys.argv[1], Y, 3))

######################











	# associate(X, Y, N) <= (len_(associate(X, Y))==N)
	# can_reach(X, Y, N) <= associate(X, Y) & N==N-1
	# can_reach(X, Y, 0) <= (X=='x' & Y=='y')

		# print(len_(associate(X, Y)), X=='дерево')