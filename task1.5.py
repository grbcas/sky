def learning_english(dict_):
    answer_counter = 0
    for key, value in dict_.items():
        print(f'Задание: {key}')
        answer = input('Введите недостающее слово: ').lower()
        if answer == value:
            print('Ответ верный!')
            answer_counter += 1
        else:
            print(f'Ваш ответ: {answer}')
            print(f'Верный ответ: {value}')
    answer_percent = int(answer_counter/len(dict_)*100)
    return f'Вот и всё! Вы ответили на {answer_counter} ' \
           f'вопросов из {len(dict_)} верно, это {answer_percent} процентов.'


if __name__ == '__main__':
    dict_tasks = {
        "My name ___ Vova": "is",
        "I ___ a coder": "am",
        "I live ___ Moscow": "in"
    }
    print(learning_english(dict_tasks))
