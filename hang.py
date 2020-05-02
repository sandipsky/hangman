#hangman game in python by sandipsky

import random


def get_word():
	words = ['rat', 'cat', 'bat', 'python', 'monkey', 'tiger', 'dragon', 'linux']
	return random.choice(words)

def playagain():
	ans = input('Do u want to play again? yes or no').lower()
	if ans == "yes":
		play_game()
	else:
		pass

def play_game():
	letter_guessed = []
	word = get_word()
	tries = 5
	guessed = False
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	print("##### Welcome to hangman game #######")
	name = input('Enter your name: ')
	print('Alright lets begin the game '+name)
	print('your word has ', len(word), 'letters')
	print(len(word) * '*')
	while(guessed == False and tries>0):
		print('you have ',tries,'tries')
		guess = input('Please enter one letter or Full word if u can: ').lower()
		#case 1: user inputs one letter
		if len(guess) == 1:
			if guess not in alpha:
				print('You have not entered a letter')
			elif guess in letter_guessed:
				print('You have already entered that letter')
				letter_guessed.append(guess)
			elif guess in word:
				print('welldone letter exists')
				letter_guessed.append(guess)
			elif guess not in word:
				print('sorry that letter doesnt exist')
				letter_guessed.append(guess)
				tries -= 1
		elif len(guess) == len(word):
			if guess == word:
				print('Bravo! You have won the game')
				guessed = True
			else:
				print('sorry your word is not correct')
				tries -= 1
		else:
			print('length of word doesnt match')

		status=''
		if guessed==False:
			for letter in word:
				if letter in letter_guessed:
					status += letter
				else:
					status += '*'
			print(status)

		if status == word:
			print('Bravo! You have won the game')
			guessed = True

		elif tries == 0:
			print('Sorry! You have run out of guesses')


	playagain()
			


play_game()
	