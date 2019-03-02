# -*- coding: utf-8 -*-

def get_keywords(text = ""):
	from rutermextract import TermExtractor
	term_extractor = TermExtractor()
	text_local = text
	myList = []
	for term in term_extractor(text_local):
		myList.append(term.normalized)
		#print(term.normalized, term.count)
	#print(myList)
	return myList

if __name__ == '__main__':
	get_keywords("несогласованное использование табуляции и пробелов в отступах")