import sys

def main():
	string = ""

	if len(sys.argv) > 2:
		print ("AssertionError: more than one argument is provided")
		sys.exit()
	elif len(sys.argv) == 1:
		while string == "":
			string = input("Please, provide this programm with one string: \n")
	else:
		string = sys.argv[1]
	
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

	result = f"""The text contains {upper + lower + punc + digit + space} characters:
{upper} upper letters
{lower} lower letters
{punc} punctuation marks
{space} spaces
{digit} digits """

	print(result)


if __name__ == "__main__":
	main()