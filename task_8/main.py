from json import load
from random import shuffle
from utils import *


def main():
	questions = []
	# получаем список вопросов из файла
	with open('questions.json', 'r', encoding='utf-8') as f:
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

	print('\nВот и всё!')
	print(f'Отвечено {sum([x.if_answer for x in questions])} вопроса из {len(questions)}')
	print(f'Набрано баллов: {sum([x.points_per_question for x in questions])}')


if __name__ == '__main__':
	main()
