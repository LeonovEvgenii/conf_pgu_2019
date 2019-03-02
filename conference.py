#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from get_definition import get_definition
from get_keywords import get_keywords

def get_graph(definition = "Дерево", n = 0):	
	if n == 5:
		sys.exit()

	definition_text = get_definition(definition)	
	
	keywords = get_keywords(definition_text)

	i=0
	while i<len(keywords):
		keywords[i] = keywords[i].replace(" ", "_")
		i = i+1

	# print(keywords)

	for definition in keywords:
		n = n+1
		# print(definition)
		get_graph(definition, n)

if __name__ == '__main__':
	get_graph("Дерево", 2)
	#graph = get_graph(definition = "дерево")
	# понятие -> понятие2