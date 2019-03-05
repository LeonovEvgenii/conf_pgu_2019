# -*- coding: utf-8 -*-
from rutermextract import TermExtractor

def get_keywords(text = ""):
	term_extractor = TermExtractor()
	return [ _.normalized for _ in term_extractor(text) if len(_.normalized) > 3 ][0:10]

if __name__ == '__main__':
	get_keywords("несогласованное использование табуляции и пробелов в отступах")