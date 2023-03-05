"""
Напишите функцию `load_random_word()` в файле `utils`, которая:

- получит список слов с внешнего ресурса,
- выберет случайное слово,
- создаст экземпляр класса `BasicWord`,
- вернет этот экземпляр.
"""

import basic_word
import requests
import random

URL = 'https://www.jsonkeeper.com/b/5LLM'


def load_random_word(url):
	with requests.get(url) as get_req:
		word_subwords_json = get_req.json()

	random_word = random.choice(word_subwords_json)
	word = random_word.get('word')
	subwords_list = random_word.get('subwords')

	anagrams = basic_word.BasicWord(word, subwords_list)
	return anagrams


if __name__ == '__main__':
	print(load_random_word(URL))
