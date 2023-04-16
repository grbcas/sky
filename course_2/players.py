class Player:
	def __init__(self, user_name=None):
		"""
		имя пользователя,
		использованные слова пользователя.
		"""
		self.user_name = user_name
		self.__user_answers = set()

	def name(self):
		return self.user_name

	@property
	def user_answers(self):
		return self.__user_answers

	@user_answers.setter
	def user_answers(self, user_answers):
		self.__user_answers = user_answers

	def add_answer(self, answer) -> None:
		"""добавление слова в использованные слова (ничего не возвращает);"""
		self.__user_answers.add(answer)

	def check_answer_repeat(self, answer) -> bool:
		"""проверка использования данного слова до этого (возвращает bool)"""
		if answer in self.__user_answers:
			return False
		return True

	def count_user_answers(self) -> int:
		"""получение количества использованных слов (возвращает int)"""
		return len(self.__user_answers)

	def __repr__(self):
		return f"{self.__class__}: {self.user_name} {self.__user_answers}"
