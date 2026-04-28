import sys

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


def main():
    "Transform an alpha string in morse code"

    if (len(sys.argv) != 2):
        print("AssertionError: the arguments are bad")
        sys.exit()

    string = sys.argv[1].upper()
    code = []
    for char in string:
        if char in MORSE.keys():
            code.append(MORSE[char])
        else:
            print("AssertionError: the arguments are bad")
            sys.exit()

    for char in code:
        print(char, end=" ")
    print()


if __name__ == "__main__":
    main()
