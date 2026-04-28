import sys
from ft_filter import ft_filter


def wordLength(word, length):
    "Compares the word's length to a given length"

    if (len(word) > length):
        return True
    else:
        return False


def main():
    if (len(sys.argv) != 3):
        print("AssertionError: the arguments are bad")
        sys.exit()

    words = sys.argv[1].split()
    # help(wordLength)

    try:
        length = int(sys.argv[2])
        long_words = ft_filter(lambda seq: wordLength(seq, length), words)
        print(long_words)
    except (ValueError, TypeError):
        print("AssertionError: second argument is not an integer")
        sys.exit()


if __name__ == "__main__":
    main()
