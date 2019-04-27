import os

def ask_question(term, level):
	print(term, level)

	f = open('graph.py', 'a')

	footer = """
Associate.indirect_vertex(X,Y, N) <= (Associate.bind[X]==Y) & (Y != None) & (N>0)
Associate.indirect_vertex(X,Y, N) <= (Associate.bind[X]==Z) & Associate.indirect_vertex(Z,Y, N-1) & (Y != None) & (N>0)

print(Associate.indirect_vertex(X, %s, %s))


""" % (term, level)

# print(Associate.indirect_vertex(%s, Y, %s))
# """ % (term, level, term, level)

	f.write(footer)
	f.close()

	os.system('python3 graph.py')
