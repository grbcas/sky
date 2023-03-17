class Player:
	def __init__(self, user_name=None):
		"""
		имя пользователя,
		использованные слова пользователя.
		"""
		self.user_name = user_name
		self.__counter_user_answers = 0
		self.__user_answers = set()
		print(self.__user_answers)

	def get_name(self):
		return self.user_name

	@property
	def get_user_answers(self):
		return self.__user_answers

	@get_user_answers.setter
	def get_user_answers(self, user_answers):
		self.__user_answers = user_answers

	def add_answer(self, answer):
		"""добавление слова в использованные слова (ничего не возвращает);"""
		self.__user_answers.add(answer)
		print('self.__user_answers', self.__user_answers)

	def check_answer_repeat(self, answer) -> bool:
		"""проверка использования данного слова до этого (возвращает bool)"""
		if answer in self.__user_answers:
			print('уже используется')
			return False
		return True

	def count_user_answers(self) -> int:
		"""получение количества использованных слов (возвращает int)"""
		self.__counter_user_answers += 1
		return self.__counter_user_answers

	def __repr__(self):
		return f"{self.__class__}: {self.user_name} {self.__user_answers}"


if __name__ == '__main__':
	p = Player()
	user_answer = 'hfkjf'
	p.add_answer(user_answer)
	user_answer = 'hfkавпjf'
	p.add_answer(user_answer)
	user_answer = 'hfkzxcjf'
	p.add_answer(user_answer)
	user_answer = 'hfkzxcвпjf'
	p.add_answer(user_answer)
	print(p.get_user_answers)
