import sys
from ft_filter import ft_filter


def checkString(S):
    """
    Check if the string is conform
    """
    conform = [word for word in S if word.isalnum() or word == " "]
    assert len(conform) == len(S), "the arguments are bad"


def wordLength(S, N):
    "Compares the word's N to a given N"

    checkString(S)

    if (len(S) > N):
        return True
    else:
        return False


def main():

    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        words = sys.argv[1].split()
        N = int(sys.argv[2])
        long_words = ft_filter(lambda S: wordLength(S, N), words)
        print(long_words)

    except AssertionError as error:
        print("Assertion error:", error)
    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
