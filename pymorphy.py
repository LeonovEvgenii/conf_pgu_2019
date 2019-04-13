import pymorphy2
from rutermextract import TermExtractor
from pprint import pprint


def parse_question(question = 'Из чего состоит дерево'):

	term_extractor = TermExtractor()

	rte = [ _.normalized for _ in term_extractor(question) ]

	# print(rte)

	morph = pymorphy2.MorphAnalyzer()

	pm = [ morph.parse(_) for _ in rte ]

	# pprint(pm[0][0][0])

	return pm[0][0][0]

