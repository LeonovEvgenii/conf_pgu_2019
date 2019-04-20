import re
from write_to_file import write_to_file

def converter(file_name):

	f = open(file_name, 'r')

	prototype_objects = []

	for x in f:
		# rez = re.findall('\"([\w\s-]+)+\" -> \"([\w\s-]+)+\"', x)
		rez = x.split('"')[1:4:2]
		if not rez or re.match('\d', rez[1]):
			continue

		temp = []

		for x in rez:
			x = x.replace(' ', '_')
			x = x.replace('-', '_')
			temp.append(x)

		rez = temp

		prototype_objects.append(rez)
		# print(rez)

	return prototype_objects

if __name__ == '__main__':
	converter('школа.dot')