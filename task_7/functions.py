import pathlib
import json

PATH_students = pathlib.Path('students.json')
PATH_professions = pathlib.Path('professions.json')

def load_students() -> json:
	"""Загружает список студентов из файла"""
	try:
		with open(PATH_students, "r") as f:
			return json.load(f)
	except FileNotFoundError:
		print(f'No such file or directory: {PATH_students}')
		exit()


def load_professions() -> json:
	"""Загружает список профессий из файла"""
	try:
		with open(PATH_professions, "r") as f:
			return json.load(f)
	except FileNotFoundError:
		print(f'No such file or directory: {PATH_professions}')
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


def check_fitness(student_skills: list, profession: list) -> dict:
	"""возвращает словарь типа student:skills и fit_percent"""
	has = set(student_skills) - (set(student_skills) - set(profession))
	lacks = set(profession) - set(student_skills)
	fit_percent = round(100 - len(lacks) / len(profession) * 100)
	return {"has": has, "lacks": lacks, "fit_percent": fit_percent}


if __name__ == '__main__':
	result = check_fitness(['Python', 'Go', 'Linux'], ["Python", "Linux", "Docker", "SQL", "Flask"])
	print(*result['has'], *result['lacks'], result['fit_percent'])
