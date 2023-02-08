def greeting():
    print('Привет! Предлагаю проверить свои знания английского!\n'
          'Расскажи, как тебя зовут!')
    user_name = input('Введите имя: ')
    print(f'Привет, {user_name}, начинаем тренировку!')
    return user_name


def learning_english(dict_tasks: dict, username: str):
    # Создаем счетчики ответов и баллов
    answer_counter = 0
    score = 0
    tasks_quantity = len(dict_tasks)

    for key, value in dict_tasks.items():
        print(f'Задание: {key}')
        answer = input('Введите недостающее слово: ').lower()
        if answer == value:
            print('Ответ верный!\nВы получаете 10 баллов!')
            answer_counter += 1
            score += 10
        else:
            print(f'Неправильно.\nПравильный ответ: {value}')

    # считаем процент выполненных заданий
    answer_percent = '{:.2%}'.format(answer_counter/tasks_quantity)

    print(f'Вот и всё, {username}! '
          f'Вы ответили на {answer_counter} вопросов из {tasks_quantity} верно.\n'
          f'Вы заработали {score} баллов. '
          f'Это {answer_percent}.')


if __name__ == '__main__':
    dict_test_tasks = {
        "My name ___ Vova": "is",
        "I ___ a coder": "am",
        "I live ___ Moscow": "in"
    }

    name = greeting()
    learning_english(dict_test_tasks, name)

