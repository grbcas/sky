from functions import check_fitness, get_student_by_pk

pk = int(input('Введите номер студента: '))
# pk = 1
dict_name = get_student_by_pk(pk).keys()

name = ''.join([x for x in dict_name])
print(name)
skills = ', '.join(*get_student_by_pk(pk).values())
print(f'Знает {skills}')
title = input(f'Выберите специальность для оценки студента {name} ').capitalize()
# title = 'Backend'
result = check_fitness(pk, title)
print('Пригодность', result['fit_percent'])
print('Студент знает', *result['has'])
print('Студент не знает', result["lacks"])
