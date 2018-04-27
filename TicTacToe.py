### Tic Tac Toe
def display_board(B):
	print(f'\n{B[7]}|{B[8]}|{B[9]}\n-----')
	print(f'{B[4]}|{B[5]}|{B[6]}\n-----')
	print(f'{B[1]}|{B[2]}|{B[3]}\n')

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

def welcome():
	user_input = input('\nWould you like to play a game? [Y/N]\n').upper()
	if user_input == 'Y':
		print('\nGreat, Let us Begin.\n')
	elif user_input == 'N':
		print('\nHow unfortunate, Goodbye.\n')
		exit()
	else:
		print('\nInvalid Input\n')
		welcome()

def choose_input():
	Player1 = None
	while Player1 is None:
		Player1 = input('\nPlayer 1, Please select X or O.\n').upper()
		if Player1 == 'X':
			Player2 = 'O'
			break
		elif Player1 == 'O':
			Player2 = 'X'
			break
		else:
			print('\nInvalid Input, Please try again.\n')
			
	print(f'\nPlayer 1 is {Player1}.\nPlayer 2 is {Player2}.\n')
	return (Player1,Player2)

def play_game():
	GB = ['#','1','2','3','4','5','6','7','8','9']
	P1,P2 = choose_input()
	Counter = 1

	def play_input(Player,Num):
		display_board(GB)
		input_pos = None
		input_index = None
		while input_pos not in ('1','2','3','4','5','6','7','8','9'):
			input_pos = input(f'\nPlayer{Num}, Please take your turn. [1-9].\n').upper()

		input_index = int(input_pos)

		if input_pos in GB:
			GB[input_index] = Player
		else:
			print('\nPosition already taken, PLease try again. [1-9]\n')
			play_input(Player,Num)
	
	win = None
	while Counter != 10:
		win = winner(GB,P1,P2)
		if win is not None:
			break
		elif Counter %2 == 0:
			play_input(P1,1)
			Counter += 1
		else:
			play_input(P2,2)
			Counter += 1
	win = winner(GB,P1,P2)
	if win is None:
		print('\nStalemate.\n')
	elif win:
		print('\nPlayer 1 Wins.\n')
	else:
		print('\nPlayer 2 Wins\n')
	
	display_board(GB)
	
def play_again():
	again_input = input('\nWould you like to play again? [Y/N]\n').upper()
	if again_input == 'Y':
		print('\nGreat, Let us Begin.\n')
		play_game()
		play_again()
	elif again_input == 'N':
		print('\nHow unfortunate, Goodbye.\n')
		exit()
	else:
		print('\nInvalid Input, Try again.\n')
		play_again()
welcome()
play_game()
play_again()
