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

	def __init__(self, word, subwords, user_answer=''):
		self.word = word
		self.__subwords = subwords
		self.__user_answer = user_answer

	@property
	def get_answer(self):
		return self.__user_answer

	@get_answer.setter
	def get_answer(self, user_answer):
		self.__user_answer = user_answer

	def check_answer(self):
		"""проверку введенного слова в списке допустимых подслов (вернет bool),"""
		cyrillic_lower = [chr(x) for x in range(1072, 1104)]
		if not set(set(self.__user_answer)).issubset(set(cyrillic_lower)):
			print('введите слово кириллицей без пробелов')
			return False
		if len(self.__user_answer) < 3:
			print('слишком короткое слово')
			return False
		# print(f'{self.__subwords}')
		if self.__user_answer in self.__subwords:
			return True

	def count_subwords(self) -> int:
		"""подсчет количества подслов (вернет int)"""
		len_answers = len(self.__subwords)
		return len_answers

	def __repr__(self):
		return f"{self.__class__}: {self.word} {self.__subwords}"


if __name__ == '__main__':
	ex = BasicWord("питон", ["пот", "тип", "топ", "пион", "понт"])
	ex.get_answer = 'пион'
	print(ex.count_subwords())
	print('пион', ex.check_answer())
	print(ex.__dict__)
