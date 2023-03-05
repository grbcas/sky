import basic_word, players
import utils
URL = 'https://www.jsonkeeper.com/b/5LLM'

task_word = utils.load_random_word(URL)
print(task_word.word)

while True:
	user_input = input('введите слово: ').lower()
	if user_input in ['стоп', 'stop']:
		print(f'Программа: Игра завершена, вы угадали {8} слов!')
		exit()

	if task_word.check_anagrams(user_input):
		print('yess')
	else:
		print('NNNNOOO')
