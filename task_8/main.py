from json import load
from random import shuffle
from utils import *

PATH = 'questions.json'


def read_data(file_name):
	"""
	Чтение данных из JSON файла
	Args:
	file_name: имя файла
	Returns:	декодировнные данные
	"""
	with open(file_name, mode='r', encoding='utf-8') as file:
		data = load(file)
	return data


def main():
	data = read_data(PATH)

	# Создайте список экземпляров класса Question
	questions = []
	for i in data:
		questions.append(Questions(i['q'], i['d'], i['a']))
	# формируем список вопросов в случайном порядке
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

	print('\nВот и всё!')
	print(f'Отвечено {sum([x.if_answer for x in questions])} вопроса из {len(questions)}')
	print(f'Набрано баллов: {sum([x.points_per_question for x in questions])}')


if __name__ == '__main__':
	main()
