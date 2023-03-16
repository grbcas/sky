from random import random


def shuffle_word(word) -> str:
	"""перемешивает буквы"""
	lst_to_shuffle = list(word.rstrip())
	r = sorted(lst_to_shuffle, key=lambda x: random())
	s_word = ''.join(r)
	return s_word


def main():
	name = input('Введите ваше имя: ')
	# выбирает первое слово из списка, перемешивает буквы и предлагает пользователю его отгадать
	with open('words.txt', 'r', encoding="utf-8") as f_in:
		words = f_in.readlines()
	score = 0
	for word in words:
		print('Угадайте слово: ', shuffle_word(word))
		user_word = input('> ').lower()
		if user_word == word.rstrip():
			score += 10
			print(f'Верно! Вы получаете 10 очков.')
		else:
			print(f'Неверно! Верный ответ – {word.rstrip()}.')

	# записываем результат пользователя
	with open('history.txt', 'a', encoding="utf-8") as f_out:
		print(name, str(score))
		f_out.write(name + ' ' + str(score) + '\n')

	# вывести статистику из прошлых игр, с учетом этой игры
	with open('history.txt', 'r', encoding="utf-8") as f:
		games = 0
		record = 0
		for line in f:
			games += 1
			result = line.rstrip().split()
			if len(result) > 1:
				record += int(result[1])

		print('\nВсего игр сыграно: ', games)
		print('Максимальный рекорд: ', record)


main()
