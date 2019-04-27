def print_dot(prototype_objects):

	f = open('graph_for_article.dot', 'w')
	head = """digraph g {
	"""
	f.write(head)
	body = ""

	for x in prototype_objects:
		body += '"'+x[0]+'" -> "'+x[1]+'"\n';

	body += "\n}"

	f.write(body)
	f.close()