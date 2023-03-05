class BasicWord:
	"""
	**Поля:**
- исходное слово,
- набор допустимых подслов.
	**Методы:**
- проверку введенного слова в списке допустимых подслов (вернет bool),
- подсчет количества подслов (вернет int).
- метод  `__repr__`
"""

	def __init__(self, word, subwords):
		self.word = word
		self.subwords = subwords
		# self.user_anagram = user_anagram

	def check_anagrams(self, user_anagram):
		print(user_anagram)
		if user_anagram in self.subwords:
			return True
		else:
			return False

	def count_user_subwords(self):
		pass
