import basic_word
import requests
import random

# URL = 'https://www.jsonkeeper.com/b/5LLM'
URL = 'https://api.npoint.io/463f7575c7f973ca6761'


def load_random_word(url=URL):
	"""
	функция:
	- получит список слов с внешнего ресурса,
	- выберет случайное слово,
	- создаст экземпляр класса `BasicWord`,
	- вернет этот экземпляр.
	"""
	with requests.get(url) as get_req:
		word_subwords_json = get_req.json()

	random_word = random.choice(word_subwords_json)
	word = random_word.get('word')
	subwords_list = random_word.get('subwords')

	return basic_word.BasicWord(word, subwords_list)
