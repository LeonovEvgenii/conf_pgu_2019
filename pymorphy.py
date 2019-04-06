import pymorphy2
from rutermextract import TermExtractor
from pprint import pprint


input_str = 'Что такое дерево'

term_extractor = TermExtractor()

rte = [ _.normalized for _ in term_extractor(input_str) ]


morph = pymorphy2.MorphAnalyzer()

pm = [ morph.parse(_) for _ in rte ]

pprint(pm[0])

