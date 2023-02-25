
def choose_difficulty_level() -> dict:
    """выбираем задания по уровню сложности"""
    words_easy = {
        "family": "семья",
        "hand": "рука",
        "people": "люди",
        "evening": "вечер",
        "minute": "минута",
    }
    words_medium = {
        "believe": "верить",
        "feel": "чувствовать",
        "make": "делать",
        "open": "открывать",
        "think": "думать",
    }
    words_hard = {
        "rural": "деревенский",
        "fortune": "удача",
        "exercise": "упражнение",
        "suggest": "предлагать",
        "except": "кроме",
    }
    difficulty_level = {}
    difficulty_levels = {'легкий': words_easy, 'средний': words_medium, 'сложный': words_hard}
    level_input = input('Выберите уровень сложности.\nЛегкий, средний, сложный. ').lower()
    if level_input in difficulty_levels:
        difficulty_level = difficulty_levels.get(level_input)
    else:
        print("Задан несуществующий уровень. Выход")
        exit()
    print(f'Выбран уровень сложности, мы предложим {len(difficulty_level)} слов, подберите перевод.')
    return difficulty_level


def get_answers(words_dict: dict) -> dict:
    """получаем ответы пользователя, выдаем словарь с ответами"""
    answers = {}
    for key, val in words_dict.items():
        print(f'{key}, {len(val)} букв,  начинается на {val[0]}...')
        answer = input('Ответ: ').lower()
        print(key, answer)
        if val == answer:
            print(f'Верно, {key} — это {val}.')
            answers[key] = True
        else:
            print(f'Неверно, {key} — это {val}.')
            answers[key] = False
    return answers


def score_result(answer_dict: dict):
    """считаем правильные и неправильные ответы, печатаем рейтинг"""
    levels = {
        0: "Нулевой",
        1: "Так себе",
        2: "Можно лучше",
        3: "Норм",
        4: "Хорошо",
        5: "Отлично",
    }
    mistakes = []
    print('Правильно отвечены слова: ')
    for key, val in answer_dict.items():
        if val:
            print(key)
        else:
            mistakes.append(key)

    print('Неправильно отвечены слова:')
    [print(x) for x in mistakes]
    user_rang = len(answer_dict) - len(mistakes)
    print(f'Ваш ранг:\n{levels.get(user_rang)}')


if __name__ == '__main__':
    words = choose_difficulty_level()
    result = get_answers(words)
    score_result(result)
