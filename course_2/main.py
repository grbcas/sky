import players
import utils

# URL = 'https://www.jsonkeeper.com/b/5LLM'
# получаем заданное слово
task_word = utils.load_random_word()

answers_quantity = task_word.count_subwords()

player = input('Введите имя: ')
players.Player.name = player

print(f'Привет, {player}!\n'
	f'Составьте {answers_quantity} слов из слова "{task_word.word.upper()}"\n'
	'Слова должны быть не короче 3 букв\n'
	'Чтобы закончить игру, угадайте все слова или напишите "stop"\n'
	'Поехали, ваше первое слово?')

play = players.Player()

right_answers = 0

while True:
	"""Запускайте цикл, пока количество угаданных слов не сравняется с количеством слов, которые можно составить."""
	user_input = input('\nВведите слово: ').lower()

	if user_input in ['стоп', 'stop']:
		break

	try:
		task_word.answer = user_input
	except Exception as e:
		print(f'"{user_input}" - {e}')
		continue

	if not play.check_answer_repeat(user_input):
		print("Слово уже было использовано!")
	elif task_word.check_answer():
		right_answers += 1
		print('верно')
		play.count_user_answers()
	else:
		print('неверно')
	# добавление слова в использованные слова
	play.add_answer(user_input)

	print(f'Задано слово "{task_word.word}" - верно ответов: {right_answers}, всего слов: {answers_quantity}')
	if right_answers == answers_quantity:
		break

print(f'Программа: Игра завершена, вы угадали {right_answers} слов! '
	  f'Kоличество использованных слов {play.count_user_answers()}')
