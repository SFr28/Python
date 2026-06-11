import sys


def count_characters(string: str) -> str:
    """Parameters:
        string (str): the string to be described

    Returns:
        a description of the string (number of characters, \
upper and lower cases, digit, punctuation marks and spaces)"""

    upper = 0
    lower = 0
    punc = 0
    digit = 0
    space = 0

    for letter in string:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
        elif letter.isnumeric():
            digit += 1
        elif letter.isspace():
            space += 1
        else:
            punc += 1

    result = f"""The text contains {upper + lower + punc + digit + space} \
characters:
{upper} upper letters
{lower} lower letters
{punc} punctuation marks
{space} spaces
{digit} digits """

    return result


def main():
    string = ""

    try:
        if len(sys.argv) > 2:
            assert len(sys.argv) == 2, "more than one argument is provided"
        elif len(sys.argv) == 1:
            print("What is the text to count?", flush=True)
            while string == "":
                string = sys.stdin.readline()
        else:
            string = sys.argv[1]
        # help(count_characters)
        result = count_characters(string)
        print(result)

    except AssertionError as error:
        print("Assertion error:", error)


if __name__ == "__main__":
    main()
