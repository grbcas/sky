import pathlib
import json


def load_students() -> json:
	"""Загружает список студентов из файла"""
	path = pathlib.Path('students.json')
	try:
		with open(path, "r") as f:
			return json.load(f)
	except FileNotFoundError:
		print(f'No such file or directory: {path}')
		exit()


def load_professions() -> json:
	"""Загружает список профессий из файла"""
	path = pathlib.Path('professions.json')
	try:
		with open(path, "r") as f:
			return json.load(f)
	except FileNotFoundError:
		print(f'No such file or directory: {path}')
		exit()


def get_student_by_pk(pk) -> dict:
	"""Получает словарь с данными студента по его pk """
	students = load_students()
	pk_student = {x['full_name']: x['skills'] for x in students if x['pk'] == pk}
	if pk_student:
		return pk_student
	print("У нас нет такого студента")
	exit()


def get_profession_by_title(title) -> dict:
	"""Получает словарь с инфо о профе по названию"""
	profession_skills = load_professions()
	title_skills = {title: x['skills'] for x in profession_skills if x['title'] == title}
	if title_skills:
		return title_skills
	print('У нас нет такой специальности')
	exit()


def check_fitness(student, profession):
	"""возвращает словарь типа student:skills и fit_percent"""
	student_has = get_student_by_pk(student).keys()

	professions = (get_profession_by_title(profession).get(profession))

	lacks = list(set(professions) - set(student_has))
	fit_percent = round(100 - len(lacks) / len(professions) * 100) # ?????????
	return {"has": student_has, "lacks": lacks, "fit_percent": fit_percent}


if __name__ == '__main__':
	# pk = input('Введите номер студента: ')
	pk = 3
	result = get_student_by_pk(pk).keys()
	print(*result)
	result = get_profession_by_title('Frontend')
	print(result)
	result = check_fitness(pk, 'Backend')
	print(*result['has'], result['lacks'], result['fit_percent'])
