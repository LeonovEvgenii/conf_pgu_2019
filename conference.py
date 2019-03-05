#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from get_definition import get_definition
from get_keywords import get_keywords

def get_graph(definition = "Дерево", n = 2):	
	if n > 0:
		definition_text = get_definition(definition)	
		
		keywords = get_keywords(definition_text)

		keywords = [ k.replace(' ', '_') for k in keywords ]

		for keyword in keywords:
			# print("associate['%s'] = '%s'" % (definition, keyword))
			# print("+(associate['%s'] == '%s')" % (definition, keyword))
			# print("+ associate('%s', '%s')" % (definition, keyword))

			print("+ associate('%s', '%s'), %s" % (definition, keyword, n))

			get_graph(keyword, n - 1)

if __name__ == '__main__':
	get_graph("дерево", 2)
	