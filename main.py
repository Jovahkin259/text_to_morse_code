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


def convert_to_morse_code(string_to_convert: str) -> list:
    morse_code = [" " if letter == " " else MORSE_CODE_DICT[letter] for letter in string_to_convert.upper()]
    return morse_code


def convert_morse_code_to_string(morse_code_to_convert: list):
    decoded_string = ""

    for code in morse_code_to_convert:
        if code == " ":
            decoded_string += " "
        decoded_string += ''.join(letter for letter in MORSE_CODE_DICT if MORSE_CODE_DICT[letter] == code)
    return decoded_string


if __name__ == "__main__":
    not_done = True
    while not_done:
        message = input("Enter your text to be converted, or 0 to exit: ")

        if message == "0":
            not_done = False
            break

        coded_message = convert_to_morse_code(message)
        print(f"Here is your coded message: {coded_message}")
