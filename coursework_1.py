import random


MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def morse_encode(str_to_encode: str) -> list:
    """encode str into Morse code list"""
    morse_encoded_symbols = []
    for symbol in str_to_encode.upper():
        morse_encoded_symbols.append(MORSE_CODE_DICT.get(symbol))
    return morse_encoded_symbols


def make_random_tasks(tasks_list: list) -> dict:
    """make dict task:answer in random order"""
    input('Сегодня мы потренируемся расшифровывать морзянку.\n'
          'Нажмите Enter и начнем')
    # создаём список индексов в случайном порядке в диапазоне от 0..len(tasks_list)
    random_indexes = random.sample(range(0, len(tasks_list)), len(tasks_list))
    random_tasks_list = [x for y, x in sorted(zip(random_indexes, tasks_list))]
    random_answer_list = list(map(morse_encode, random_tasks_list))
    random_tasks_dict = {}
    for i_task, i_answer in zip(random_tasks_list, random_answer_list):
        random_tasks_dict[i_task] = i_answer
    return random_tasks_dict


def get_input() -> str:
    """get input str"""
    input_word = input(f'Введите слово: ')
    return input_word


def check(task: str, user_answer: str) -> bool:
    """check user input"""
    if user_answer == task:
        print(f'Верно, {task}!')
        return True
    else:
        print(f'Неверно, {task}!')
        return False


def print_statistics(answers_list: list):
    """print_statistics"""
    print(f'Всего задачек: {len(answers_list)}\n'
          f'Отвечено верно: {answers_list.count(True)}\n'
          f'Отвечено неверно:{answers_list.count(False)}')


if __name__ == '__main__':
    tasks = ['code', 'bit', 'list', 'soul', 'next']
    answers = []
    try:
        random_tasks = make_random_tasks(tasks)
        for i_index, random_task in enumerate(random_tasks):
            print(f'Слово {i_index + 1}: {" ".join(random_tasks.get(random_task))}')
            user_input = get_input().lower()
            answers.append(check(random_task, user_input))
        print_statistics(answers)
    except KeyboardInterrupt:
        print('\nTerminated with KeyboardInterrupt')
