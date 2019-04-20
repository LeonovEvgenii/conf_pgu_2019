import os

def write_to_file(prototype_objects, main_word):
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

	f.write("%s = Associate('%s', None)\n" % (main_word, main_word))

	for i in prototype_objects:
		# print(i)
		f.write("%s = Associate('%s', %s)\n" % (i[1], i[1], i[0]))

	f.close()

