# https://github.com/daniel-kurushin/wiki-get-structure

from rutermextract import TermExtractor

from pymorphy2 import MorphAnalyzer

mo = MorphAnalyzer()

te = TermExtractor()

FILTR = set(['Abbr',
 'Fixd',
 'Geox',
 'Name',
 'Surn',
 'англ',
 'NUMB',
 'википедия',
 'гео',
 'такая статья',
 'такая страница',
 'такие название', 'быстрое старт', 'статья', 'руководство',
 'фам'])

def get_keywords(text = ""):
    terms = te(text)

    i=0

    max_count = terms[0].count
    for term in terms:

        if (i>10):
            return

        i+=1

        if term.count >= max_count / 10:
            yield term.normalized 

    
def filter_keywords(keywords = ["россия", "бердяев", "информатика"], filter = FILTR):
    for keyword in keywords:
        params = []
        
        for a in mo.parse(keyword):
                params += list(a.tag.grammemes)
            
        if not filter & set(params + [keyword]) and not len(keyword) < 3:
            yield keyword.replace('/', '_')
        else:
#            import sys
#            print(keyword, params, file = sys.stderr)
            pass

if __name__ == '__main__':
	print(list(filter_keywords(get_keywords(test))))