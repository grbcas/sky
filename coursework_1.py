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


# get input
def get_input() -> str:
    input_word = input('word_to_encode: ').upper()
    return input_word


# check if input can be encoded with Morse code
def check_input(str_to_encode) -> str:
    if not set(str_to_encode) - set(MORSE_CODE_DICT):
        return str_to_encode
    else:
        print('incorrect symbols: ', *(set(word_to_encode) - set(MORSE_CODE_DICT)))


# encoding str into Morse code
def morse_encode(str_to_encode: str) -> list:
    morse_encoded_symbols = []
    for symbol in str_to_encode:
        morse_encoded_symbols.append(MORSE_CODE_DICT.get(symbol))
    return morse_encoded_symbols


if __name__ == '__main__':
    try:
        while True:
            word_to_encode = get_input()
            if check_input(word_to_encode):
                morse_code = morse_encode(word_to_encode)
                print(*morse_code, sep=' ')
            else:
                continue
    except KeyboardInterrupt:
        print('Terminated with KeyboardInterrupt')
