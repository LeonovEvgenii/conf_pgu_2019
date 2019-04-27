#!/usr/bin/python3
# -*- coding: utf-8 -*-

from get_definition import get_definition
from get_keywords import get_keywords, filter_keywords
from write_to_file import write_to_file
from stop_words import is_stop_word
from pymorphy import parse_question
from pprint import pprint
from ask_question import ask_question
from converter import converter
from print_dot import print_dot
import sys


def get_graph(definition = "Дерево", n = 2):
	if n > 0:
		definition = definition.lower()

		definition_text = get_definition(definition)
		
		pairs = []

		for keyword in filter_keywords(get_keywords(definition_text)):
			if keyword.find(' ') == -1:
				if keyword != definition and not is_stop_word(keyword):
					yield [definition, keyword]
					for x in get_graph(keyword, n - 1):
						yield x
			
if __name__ == '__main__':

	prototype_objects = []

	# получение с википедии
	# for x in get_graph("дерево", 2):
	# 	prototype_objects.append(x)
	
	# конвертер из файла
	prototype_objects = converter('graph_for_article.dot')

	# print(prototype_objects)

	# print_dot(prototype_objects)

	# write_to_file(prototype_objects, 'школа')
	write_to_file(prototype_objects, 'дерево')

	# term = parse_question('Из чего состоит побеги')
	# term = parse_question('Из чего состоит лепестки')
	# term = parse_question('Где изучают историю и не изучают музыку')

	# ask_question(term, 5)
	ask_question(sys.argv[1], sys.argv[2])
	# ask_question('история')