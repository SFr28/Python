import sys


def encoding(text: str) -> None:
    MORSE = {
        ' ': '/',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..'
    }

    code = []
    for char in text:
        if char in MORSE.keys():
            code.append(MORSE[char])
        else:
            raise AssertionError("the arguments are bad")

    for char in code:
        print(char, end=" ")
    print()


def main():
    "Transform an alpha string in morse code"

    try:
        assert len(sys.argv) == 2, "the arguments are bad"

        encoding(sys.argv[1].upper())

    except AssertionError as error:
        print("Assertion error:", error)
    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
