def greeting():
    print('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать!')
    ready = input('input "ready" to start: ').lower()
    if ready == 'ready':
        return ready
    else:
        print('Кажется, вы не хотите играть. Очень жаль.')
        return exit()


def learning_english(dict_tasks: dict):
    # Создаем счетчики ответов и баллов
    answer_counter = 0
    # score = 0
    tasks_quantity = len(dict_tasks)

    for key_question, value_answer in dict_tasks.items():
        print(f'Задание: {key_question}')
        for i_tryies in range(3):
            answer = input('Введите недостающее слово: ').lower()
            if answer == value_answer and i_tryies < 3:
                print('Ответ верный!\nВы получаете 10 баллов!')
                answer_counter += 1
                # score += 10
                break
            elif i_tryies < 2:
                print(f'Осталось попыток: {2-i_tryies}, попробуйте еще раз!')
                i_tryies += 1
            else:
                print(f'Неправильно.\nПравильный ответ: {value_answer}')

    # считаем процент выполненных заданий
    answer_percent = round(100*answer_counter/tasks_quantity, 2)

    print(f'Вот и всё! '
          f'Вы ответили на {answer_counter} вопросов из {tasks_quantity} верно.\n'
          # f'Вы заработали {score} баллов. '
          f'Это {answer_percent} процентов.')


if __name__ == '__main__':
    # выполняем задание: "Создайте два списка  с вопросами и ответами"
    questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
    answers = ["is", "am", "in"]

    dict_questions_answers = {}

    for i, val in enumerate(questions):
        dict_questions_answers[val] = answers[i]

    greeting()
    learning_english(dict_questions_answers)
