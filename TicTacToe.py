### Tic Tac Toe

def input_check(user_input,scenario):

	if scenario == 'A':
		return user_input in ('Y','N')
	elif scenario == 'B':
		return user_input in ('X','O')
	elif scenario == 'C':
		return user_input in ('1','2','3','4','5','6','7','8','9')
### Surely is better for readability to list the numbers vs return 49 <= ord(user_input) <= 57?
### Tuples look the cleanest whilst also conveying what's going on?

def display_board(B):
	print(f'\n{B[7]}|{B[8]}|{B[9]}\n-----')
	print(f'{B[4]}|{B[5]}|{B[6]}\n-----')
	print(f'{B[1]}|{B[2]}|{B[3]}\n')
### ^^^ Is this consider clean or could it be improved further?

def winner(B,P1,P2):
	if ((B[1] == B[2] == B[3] == P1) or
		(B[4] == B[5] == B[6] == P1) or
		(B[7] == B[8] == B[9] == P1) or
		(B[1] == B[4] == B[7] == P1) or
		(B[2] == B[5] == B[8] == P1) or
		(B[3] == B[6] == B[9] == P1) or
		(B[1] == B[5] == B[9] == P1) or
		(B[3] == B[5] == B[7] == P1)):
		return True
	elif ((B[1] == B[2] == B[3] == P2) or
		(B[4] == B[5] == B[6] == P2) or
		(B[7] == B[8] == B[9] == P2) or
		(B[1] == B[4] == B[7] == P2) or
		(B[2] == B[5] == B[8] == P2) or
		(B[3] == B[6] == B[9] == P2) or
		(B[1] == B[5] == B[9] == P2) or
		(B[3] == B[5] == B[7] == P2)):
		return False
	else:
		return None
### ^^^ Still needs work on my part?

def welcome():
	user_input = input('\nWould you like to play a game? [Y/N]\n').upper()
	if input_check(user_input,'A') is True:
		if user_input in ('Y'):
			print('\nGreat, Let us Begin.\n')
		else:
			print('\nHow unfortunate, Goodbye.\n')
			exit()
	else:
		print('\nInvalid Input\n')
		welcome()

### Is it good practice to theme your program to use recursion OR loops?

def choose_input():
	Player1 = None
	while Player1 is None:
		Player1 = input('\nPlayer 1, Please select X or O.\n').upper()
		if Player1 in ('X'):
			Player2 = 'O'
			break
		elif Player1 in ('O'):
			Player2 = 'X'
			break
		else:
			print('\nInvalid Input, Please try again.\n')

	print(f'\nPlayer 1 is {Player1}.\nPlayer 2 is {Player2}.\n')

	return (Player1,Player2)

### Removed Hash # was a relic from an earlier idea.

def play_game():
	GB = ['#','1','2','3','4','5','6','7','8','9']
	P1,P2 = choose_input()
	Counter = 1

	def play_input(Player,Num):
		display_board(GB)
		input_pos = None
		input_index = None
		while input_check(input_pos,'C') is False:
			input_pos = input(f'\nPlayer{Num}, Please take your turn. [1-9].\n').upper()
			if input_check(input_pos,'C') is False:
				print('\nInvalid Input, Try again.\n')
			else:
				break

		input_index = int(input_pos)

		if input_pos in GB:
			GB[input_index] = Player
		elif GB[input_index] in (P1,P2):
			print('\nPosition already taken, PLease try again. [1-9]\n')
			play_input(Player,Num)

		### Using a while for the input instead of recursion. 

	win = None

	while Counter is not 10:
		win = winner(GB,P1,P2)
		if win in (True,False):
			break
		elif Counter %2 == 0:
			play_input(P1,1)
			Counter += 1
		elif Counter %2 != 0:
			play_input(P2,2)
			Counter += 1
	
	if Counter is 10:
		print('\nStalemate.\n')
	elif winner(GB,P1,P2):
		print('\nPlayer 1 Wins.\n')
	elif not winner(GB,P1,P2):
		print('\nPlayer 2 Wins\n')

	display_board(GB)
				
### Cleaned up the if statements at the end a little.

def play_again():
	again_input = input('\nWould you like to play again? [Y/N]\n').upper()
	if not input_check(again_input,'A'):
		print('\nInvalid Input\n')
		play_again()
	elif again_input in ('Y'):
		print('\nGreat, Let us Begin.\n')
		play_game()
		play_again()
	else:
		print('\nHow unfortunate, Goodbye.\n')
		exit()

welcome()

play_game()

play_again()
