#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, random, os
from get_definition import get_definition
from get_keywords import get_keywords

def write_to_file(prototype_objects):
	f = open('graph.py', 'w')

	head = ("""
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

""")

	f.write(head)

	f.write("дерево = Associate('дерево', None)\n")

	for i in prototype_objects:
		# print(i)
		f.write("%s = Associate('%s', %s)\n" % (i[1], i[1], i[0]))

	footer = """
Associate.indirect_manager(X,Y, N) <= (Associate.bind[X]==Y) & (Y != None) & (N>0)
Associate.indirect_manager(X,Y, N) <= (Associate.bind[X]==Z) & Associate.indirect_manager(Z,Y, N-1) & (Y != None) & (N>0)

print(Associate.indirect_manager(X, Y, 1))
"""

	f.write(footer)

	f.close()

	os.system('python3 graph.py')



def get_graph(definition = "Дерево", n = 2):	
	if n > 0:
		definition_text = get_definition(definition)	
		
		keywords = get_keywords(definition_text)

		keywords = [ k.replace(' ', '_') for k in keywords ]

		pairs = []

		for keyword in keywords:
			yield [definition, keyword]
			for x in get_graph(keyword, n - 1):
				yield x
			


if __name__ == '__main__':

	prototype_objects = []

	for x in get_graph("дерево", 2):
		prototype_objects.append(x)
		
	write_to_file(prototype_objects)