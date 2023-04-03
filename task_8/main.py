from json import load
from random import shuffle


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


def main():
	questions = []
	# получаем список вопросов из файла
	with open('questions.json', 'r') as f:
		data = load(f)
		for i in data:
			questions.append(Questions(i['q'], i['d'], i['a']))
	shuffle(questions)

	# получаем и обрабатываем ответы
	for i_question in questions:
		print(i_question.build_question())
		i_question.user_answer = input('Ответ: ')
		if i_question.is_correct():
			# подсчитываем points per question
			i_question.get_points()
			# помечаем ответ как верный
			i_question.if_answer = True
			print(i_question.build_positive_feedback())
		else:
			print(i_question.build_negative_feedback())

	print('Вот и всё!')
	print(f'Отвечено {sum([x.if_answer for x in questions])} вопроса из {len(questions)}')
	print(f'Набрано баллов: {sum([x.points_per_question for x in questions])}')


if __name__ == '__main__':
	main()
