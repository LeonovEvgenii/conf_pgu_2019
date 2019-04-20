import pymorphy2
from rutermextract import TermExtractor
from pprint import pprint


def parse_question(question = 'Где изучают историю и не изучают музыку'):

	# term_extractor = TermExtractor()

	# rte = [ _.normalized for _ in term_extractor(question) ]

	# print(rte)

	morph = pymorphy2.MorphAnalyzer()

	# pm = [ morph.parse(_) for _ in rte ]

	pms = []

	for x in question.split(' '):
		pms.append(morph.parse(x))

	for pm in pms:
		if 'NOUN' in pm[0].tag:
			print(pm[0].normalized.word)

	# pprint(pm[0][0][0])

	# print(pm[0][0])

	# return pm[0][0][0]

if __name__ == '__main__':
	parse_question();

