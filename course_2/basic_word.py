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
	# CYRILLIC_LOWER = (chr(x) for x in range(1072, 1104))
	CYRILLIC_LOWER = set('абвгдежзийклмнопрстуфхцчшщъыьэюя')

	def __init__(self, word, subwords, user_answer=''):

		self.__word = word
		self.__subwords = subwords
		self.__user_answer = user_answer

	@classmethod
	def validate_user_answer(cls, user_answer):
		"""
		проверка слова на символы и длину слова
		:param user_answer:
		:return:
		"""
		if not set(user_answer).issubset(cls.CYRILLIC_LOWER):
			raise ValueError('слово должно быть написано кириллицей без пробелов')
		elif len(user_answer) < 3:
			raise ValueError('слишком короткое слово')

	@property
	def answer(self):
		return self.__user_answer

	@answer.setter
	def answer(self, user_answer):
		self.validate_user_answer(user_answer)
		self.__user_answer = user_answer

	@property
	def word(self):
		return self.__word

	def check_answer(self) -> bool:
		"""
		проверка введенного слова в списке допустимых подслов
		:return: bool
		"""
		if self.__user_answer in self.__subwords:
			return True

	def count_subwords(self) -> int:
		"""подсчет количества подслов (вернет int)"""
		return len(self.__subwords)

	def __repr__(self):
		return f"{self.__class__}: {self.__word} {self.__subwords}"
