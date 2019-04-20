import os

def ask_question(term):
	f = open('graph.py', 'a')

	footer = """
Associate.indirect_manager(X,Y, N) <= (Associate.bind[X]==Y) & (Y != None) & (N>0)
Associate.indirect_manager(X,Y, N) <= (Associate.bind[X]==Z) & Associate.indirect_manager(Z,Y, N-1) & (Y != None) & (N>0)

print(Associate.indirect_manager(X, %s, 1))
print(Associate.indirect_manager(%s, Y, 1))
""" % (term, term)

	f.write(footer)
	f.close()

	os.system('python3 graph.py')
