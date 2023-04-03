from functions import check_fitness, get_student_by_pk, get_profession_by_title


def main():
	pk = int(input('Введите номер студента: '))
	student = get_student_by_pk(pk)

	# Выводим информации о студенте
	# student_name = ''.join([x for x in student.keys()])
	student_name = next(iter(student))
	print(student_name)
	# student_skills = [x for x in student.values()][0]
	student_skills = list(student.values())[0]
	print(f'Знает: {", ".join(student_skills)}')

	# Пользовательский ввод специальности для оценки студента
	title = input(f'Выберите специальность для оценки студента {student_name}: ').capitalize()
	# Загружаем информацию о навыках указанной профессии
	profession = (get_profession_by_title(title).get(title))

	# Загружаем информацию о том, что знает/не знает студент и степенью его пригодности
	result = check_fitness(student_skills, profession)
	print('Пригодность:', result['fit_percent'])
	print('Студент знает:', ', '.join(result['has']))
	print('Студент не знает:', ', '.join(result['lacks']))


if __name__ == '__main__':
	main()
