from main import convert_morse_code_to_string, convert_to_morse_code


def test_convert_morse_code_to_string():
    assert convert_morse_code_to_string(
        ['.---', '---', '...', '....', ' ', '.-', '...', '-', '.-..', '.']) == "Josh Astle".upper()


def test_convert_string_to_morse_code():
    assert convert_to_morse_code("Josh Astle") == ['.---', '---', '...', '....', ' ', '.-', '...', '-',
                                                   '.-..', '.']
