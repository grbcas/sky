def greeting():
    print('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать!')
    ready = input('input "ready" to start: ').lower()
    if ready == 'ready':
        return ready
    else:
        print('Кажется, вы не хотите играть. Очень жаль.')
        exit()


def learning_english(dict_tasks: dict) -> str:
    """
    задаем вопросы, считаем ответы и баллы
    возвращаем текст c оценками
    """
    answer_counter = 0
    score = 0
    tasks_quantity = len(dict_tasks)

    for key_question, value_answer in dict_tasks.items():
        print(f'Задание: {key_question}')
        for i_attempt in range(3):
            answer = input('Введите недостающее слово: ').lower()
            if answer == value_answer and i_attempt < 3:
                answer_counter += 1
                match i_attempt:
                    case 0:
                        score += 3
                        print(f'Ответ верный!\nВы получаете {3 - i_attempt} балла!')
                    case 1:
                        score += 2
                        print(f'Ответ верный!\nВы получаете {3 - i_attempt} балла!')
                    case 2:
                        score += 1
                        print(f'Ответ верный!\nВы получаете {3 - i_attempt} балл!')
                break
            elif i_attempt < 2:
                print(f'Осталось попыток: {2-i_attempt}, попробуйте еще раз!')
                i_attempt += 1
            else:
                print(f'Неправильно.\nПравильный ответ: {value_answer}')

    # считаем процент выполненных заданий
    answer_percent = round(100*answer_counter/tasks_quantity, 2)
    output = str(
        f'Вот и всё! '
        f'Вы ответили на {answer_counter} вопросов из {tasks_quantity} верно.\n'
        f'Вы заработали {score} баллов. '
        f'Это {answer_percent} процентов.')
    return output


if __name__ == '__main__':
    # выполняем задание: "Создайте два списка  с вопросами и ответами"
    questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
    answers = ["is", "am", "in"]

    dict_questions_answers = {}
    # for i, val in enumerate(questions):
    #     dict_questions_answers[val] = answers[i]
    for i_question, i_answer in zip(questions, answers):
        dict_questions_answers[i_question] = i_answer
    greeting()
    print(learning_english(dict_questions_answers))
