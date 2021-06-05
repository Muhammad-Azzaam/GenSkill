import re
import random


def create_word_list(fin):
	fname = open(fin)
	words = []
	for line in fname:
		line = line.strip()
		for word in line.split():
			if len(word)>=6 and word.isalpha() and word.islower():
				words.append(word)	

	fname.close()
	#print(words)
	return random.choice(words)





def print_masked_word(word):
	print("\nThe given word is:    ", end=" ")
	if len(word)>=9:
		i = 3
	else:
		i = 2
	initial_indices = []
	while i>0:
		j = random.randint(0,len(word)-1)
		if j not in initial_indices:
			initial_indices.append(j)
			i-=1
		
	for k in range(len(word)):
		if k in initial_indices:
			print(word[k], end = " ")
		else:
			print("_", end=" ")
	print("(",len(word), " LETTERS )\n\n")
	return initial_indices




def print_remaining_letters(word,found_letters,initial_indices):
	for i in range(len(word)):
		if i in initial_indices:
			print(word[i], end=" ")
		elif word[i] in found_letters:
			print(word[i], end=" ")
		else:
			print("_", end=" ")
	print("\n")





#def main():
fin = input("Enter the name of the file: ")
word = create_word_list(fin)

print("\n")
heading = "WELCOME TO THE GAME OF HANGMAN"
print(heading.center(80,"*"),end="\n\n")
	
rules = """RULES:
1) The aim of the game is to guess the masked word.
2) You will have 5 chances within which you have to guess the word.
3) The 5 chances include either: (i)guessing the word, or (ii)guessing a letter.
"""
print(rules)





#PRINT A FEW LETTERS OF THE WORD(FUNCTION)
initial_indices = print_masked_word(word)
	




letters = []
for char in word:
	if char not in letters:
		letters.append(char)



if len(word)>=9:
	tries = 6
else:
	tries = 5

text = """What would you like to do?
1) Guess the Word
2) Guess a Letter

Enter an option(1/2): """



found_letters = []
for i in initial_indices:
	if word.count(word[i])==1:
		found_letters.append(word[i])



while tries!=0:
	
	print("YOU HAVE ", tries, " CHANCES REMAINING!", end="      ") 
	print_remaining_letters(word,found_letters,initial_indices)
	option = input(text)
	if option=="1":
		answer = input("\nEnter the word: ")
		if answer==word:
			print("YOUR GUESS IS CORRECT!!! THE WORD WAS", word)
			quit()
		else:
			print("Sorry, your guess was INCORRECT!\n")			
			tries-=1

	elif option=="2":
		answer = input("\nEnter a letter: ")
		if answer in letters and answer not in found_letters:
			print(answer, " is a CORRECT guess.", end="   ")
			found_letters.append(answer)
			print_remaining_letters(word,found_letters,initial_indices)
			if len(found_letters)==len(letters):
				print("\n\nYOU'VE FOUND ALL THE LETTERS OF THE WORD!!! THE WORD WAS ", word)
				quit()			

		else:
			print(answer, "is an INCORRECT guess.\n")

		tries-=1

	else:
		print("INVALID OPTION CHOSEN! PLEASE ENTER A VALID OPTION AGAIN(1/2)\n")

	print("-"*80, end="\n\n")

			

print("All your tries have been exhausted! You were unable to guess the word. The word was", word)

	
					
