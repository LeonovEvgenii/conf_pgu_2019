# https://github.com/daniel-kurushin/wiki-get-structure

from get_wiki_definition import get_wiki_definition

def get_definition(definition = "Дерево"):
    try:
        rez = open("database/%s.dat" % definition).read()
    except FileNotFoundError:
        rez = get_wiki_definition(definition)
        open("database/%s.dat" % definition, 'w').write(rez)
    return rez

if __name__ == '__main__':
    print(get_definition())