keys = [1, 2, 3, 4, 5]
values = ['one', 'two', 'three']

def make_dict(keys, values):

	"""
	Arguments must be iterable and indexable.
	Function returns a dictionary with keys
	from first argument elements, and values
	from second elements argument.
	If length of the second argument less
	than lenght of the first argument,
	difference will fills with None values.
	"""

	dictionary = dict()
	for i in range(len(keys)):
		if i > len(values) - 1:
			dictionary.update({keys[i] : None})
		else:
			dictionary.update({ keys[i] : values[i]})

	return dictionary

if __name__ == "__main__":
	print(make_dict(keys, values))
