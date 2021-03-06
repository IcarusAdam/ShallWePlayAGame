def input_check(user_input,scenario):
	if scenario == 'A':
		if user_input in ('Y','N'):
			return Truea
		else:
			return False
	elif scenario == 'B':
		if user_input in ('X','O'):
			return True
		else:
			return False
	elif scenario == 'C':
		if user_input in ('1','2','3','4','5','6','7','8','9'):
			return True
		else:
			return False

def display_board(B):
	print(f'\n{B[7]}|{B[8]}|{B[9]}\n-----')
	print(f'{B[4]}|{B[5]}|{B[6]}\n-----')
	print(f'{B[1]}|{B[2]}|{B[3]}\n')

def winner(B,P1,P2):
	if ((B[1] == B[2] == B[3] == P1) or
		(B[4] == B[5] == B[6] == P1) or
		(B[7] == B[8] == B[9] == P1) or
		(B[1] == B[4] == B[6] == P1) or
		(B[2] == B[5] == G[8] == P1) or
		(B[3] == B[6] == B[9] == P1) or
		(B[1] == B[5] == B[9] == P1) or
		(B[3] == B[5] == B[7] == P1)):
		return True
	elif ((B[1] == B[2] == B[3] == P2) or
		(B[4] == B[5] == B[6] == P2) or
		(B[7] == B[8] == B[9] == P2) or
		(B[1] == B[4] == B[6] == P2) or
		(B[2] == B[5] == G[8] == P2) or
		(B[3] == B[6] == B[9] == P2) or
		(B[1] == B[5] == B[9] == P2) or
		(B[3] == B[5] == B[7] == P2)):
		return False
	else:
		return None

def welcome():
	user_input = input('\nWould you like to play a game? [Y/N]\n')
	user_input = user_input.upper()
	if input_check(user_input,'A') == True:
		if user_input in ('Y'):
			print('\nGreat, Let us Begin.\n')
		else:
			print('\nHow unfortunate, Goodbye.\n')
			exit()
	else:
		print('\nInvalid Input\n')
		welcome()

def choose_input():
	Player1 = None
	Player2 = None
	while Player1 == None:
		Player1 = input('\nPlayer 1, Please select X or O.\n')
		Player1 = Player1.upper()
		if input_check(Player1,'B') == True:
			if Player1 in ('X'):
				Player2 = 'O'
				pass
			elif Player1 in ('O'):
				Player2 = 'X'
				pass
			else:
				print('\nError, Please try again.\n')
				choose_input()
		elif input_check(Player1,'B'):
			print('\nInvalid Input\n')
			choose_input()

	print(f'\nPlayer 1 is {Player1}.\nPlayer 2 is {Player2}.\n')

	return ('#',Player1,Player2)

def play_game():
	GB = ['#','1','2','3','4','5','6','7','8','9']
	Hash,P1,P2 = choose_input()
	Counter = 1

	def play_input(Player,Num):
		input_pos = input(f'\nPlayer{Num}, Please take your turn. [1-9].\n')
		input_pos = input_pos.upper()
		if input_check(input_pos,'C') == True:
			pass
		else:
			print('\nInvalid Input\n')
			input_pos = None
			play_input(Player,Num)

		input_index = int(input_pos)
		if input_pos in GB:
			GB[input_index] = Player
		elif GB[input_index] == P1 or P2:
			print('\nPosition already taken, PLease try again. [1-9]\n')
			input_pos = None
			input_index = None
			play_input(Player,Num)

	display_board(GB)

	while Counter != 10:
		if winner(GB,P1,P2) != None:
			Counter = 10
		elif Counter %2 == 0:
			display_board(GB)
			play_input(P1,1)
			Counter += 1
		elif Counter %2 != 0:
			display_board(GB)
			play_input(P2,2)
			Counter += 1
	
	if Counter == 9:
		print('\nStalemate.\n')
		display_board(GB)
	elif winner(GB,P1,P2) == True:
		print('\nPlayer 1 Wins.\n')
		display_board(GB)
	elif winner(GB,P1,P2) == False:
		print('\nPlayer 2 Wins\n')
		display_board(GB)	

def play_again():
	again_input = input('\nWould you like to play again? [Y/N]\n')
	again_input = again_input.upper()
	if input_check(again_input,'A') == True:
		pass
	else:
		print('\nInvalid Input\n')
		play_again()
	if again_input in ('Y'):
		print('\nGreat, Let us Begin.\n')
		play_game()
		play_again()
	else:
		print('\nHow unfortunate, Goodbye.\n')
		exit()

welcome()

play_game()

play_again()
