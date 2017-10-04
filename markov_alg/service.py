import random
import re


class MarkovChain(object):

	regex = re.compile("([\n\r])|(\S+)")

	def __init__(self, string):
		self.input_text = string
		self.table = {}
		self.generate_table()

	def words_generator(self):
		for word in re.finditer(self.regex, self.input_text):
			yield word

	def generate_table(self):
		t1, t2 = "", ""
		new_line = "\n\r"
		self.table = {}

		for i in self.words_generator():
			i = i.group(0)

			if i in new_line:
				t1, t2 = "", ""
				continue
			key = (t1, t2)

			if key in self.table:
				self.table[key].append(i)
			else:
				self.table[key] = [i]
			t1, t2 = t2, i
		return True

	def generate_text(self, length):
		result = []
		t1, t2 = "", ""
		counter = 0
		while True:
			counter += 1
			if counter >= length and any((result[-1].endswith(end) for end in ".?!")):
				break

			key = (t1, t2)
			if key not in self.table:
				t1, t2 = "", ""
				result.append("\n")
				continue

			variants = self.table[(t1, t2)]
			next_word = variants[random.randint(0, len(variants) - 1)]
			result.append(next_word)
			t1, t2 = t2, next_word

		return " ".join(result)
