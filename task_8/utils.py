class Questions:
	def __init__(self, text, difficulty, answer):
		self.text = text
		self.difficulty = difficulty
		self.answer = answer
		self.if_answer = False
		self.user_answer = None
		self.points_per_question = 0

	def get_points(self):
		"""Возвращает int, количество баллов.
		Баллы
		"""
		self.points_per_question = int(self.difficulty) * 10
		return self.points_per_question

	def is_correct(self):
		"""Возвращает True, если ответ пользователя совпадает
		с верным ответов иначе False.
		"""
		if self.user_answer == self.answer:
			return True
		return False

	def build_question(self):
		"""Возвращает вопрос в понятном пользователю виде, например:
		Вопрос: What do people often call American flag?
		Сложность 4/5
		"""
		return f'Вопрос: {self.text} \nСложность: {self.difficulty}'

	def build_positive_feedback(self):
		"""Возвращает :
		Ответ верный, получено __ баллов
		"""
		return f'Ответ верный, получено {self.points_per_question} баллов'

	def build_negative_feedback(self):
		"""Возвращает :
		Ответ неверный, верный ответ __
		"""
		return f'Ответ неверный, верный ответ {self.answer}'