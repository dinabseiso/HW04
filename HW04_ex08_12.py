# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 12 for guidance
# Please do provide function calls that test/demonstrate your function

# import here

import string 

# body here

def shift_letter(letter, shift):
	inAlphabet = 26
	if letter.isupper():
		start = ord('A') # Rank starts at 65
	elif letter.islower():
		start = ord('a') # Rank starts at 97
	else: 
		return letter 
	rankInAlphabet = ord(letter) - start
	shiftedLetter = (rankInAlphabet + shift) % inAlphabet + start 
	return chr(shiftedLetter)



def rotate_word(originalWord, shift):
	inchWorm = ""
	for letter in originalWord:
		inchWorm += shift_letter(letter, shift)
	return inchWorm


# call main() here

def main():

	print rotate_word("cryptography", 13)
	print rotate_word("mother", 7)
	print rotate_word("Niners", 40)
	print rotate_word("wedding", 2)

if __name__ == '__main__':
	main()