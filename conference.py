#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, random, os
from get_definition import get_definition
from get_keywords import get_keywords, filter_keywords
from write_to_file import write_to_file
from stop_words import is_stop_word


def get_graph(definition = "Дерево", n = 2):
	if n > 0:
		definition = definition.lower()

		definition_text = get_definition(definition)
		
		pairs = []

		for keyword in filter_keywords(get_keywords(definition_text)):
			if keyword != definition and not is_stop_word(keyword):
				yield [definition, keyword]
				for x in get_graph(keyword, n - 1):
					yield x
			
if __name__ == '__main__':

	prototype_objects = []

	for x in get_graph("дерево", 2):
		prototype_objects.append(x)
		
	write_to_file(prototype_objects)