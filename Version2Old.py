### Global Variables ### Subject to Change
GameBoard = ['#','1','2','3','4','5','6','7','8','9']
Players = None
Yes = ["YES","Y"]
No = ["NO","N"]

### User Input ## Welcomes Player and asks them to play a game?
def welcome_input():
    Yes_No = input("\nGREETINGS\nSHALL WE PLAY A GAME? (Y/N)\n")
    if Yes_No.upper() in Yes:
        print("\nEXCELLENT LET'S BEGIN\n")
    elif Yes_No.upper() in No:
        print("\nGOODBYE\n")
        exit()
    else:
        welcome_input()

def check_input(user_input):
    valid_input = ['1','2','3','4','5','6','7','8','9',"X","O","Y","N","YES","NO"]
    if user_input in valid_input:
        return True
    if user_input not in valid_input:
        return False

### Pretty self explainatory, Prints Board. Don't know how to make this bigger or prettier yet.
def display_board(B):
    ### B represents the board list
    print(f"\n{B[1]}|{B[2]}|{B[3]}\n-----")
    print(f"{B[4]}|{B[5]}|{B[6]}\n-----")
    print(f"{B[7]}|{B[8]}|{B[9]}\n")

### User Input ### Player1 Selects either X or O
def player_input():
    global Players
    Play1 = None
    Play2 = None
    Play1 = input("\nPLAYER1 PLEASE PICK X OR 0.\n")
    if Play1.upper() == "X":
        print("\nPLAYER 1 IS X\n")
        Play2 = 'O'
        print("\nPLAYER 2 IS O\n")
    elif Play1.upper() == "O":
        print("\nPLAYER 1 IS O\n")
        Play2 = 'X'
        print("\nPLAYER 2 IS X\n")
    else:
        print("\nINVALID INPUT, TRY AGAIN.\n")
        Play1 = None
        Play2 = None
    Players = list(["#",Play1,Play2])

### User Input ### Player1 Selects either X or O
def choose_input():
    player_input()
    input_break = 1
    if input_break == 4:
        exit()
    if Players[1 or 2] == None:
        player_input()
        input_break += 1

def who_wins(GB,P1,P2):
    ### Checks to see if Win/Lose/Stalemate has occured. (GameBoard,Player1,Player2)
    if ((GB[1] == GB[2] == GB[3] == P1) or 
        (GB[4] == GB[5] == GB[6] == P1) or 
        (GB[7] == GB[8] == GB[9] == P1) or 
        (GB[1] == GB[4] == GB[6] == P1) or 
        (GB[2] == GB[5] == GB[8] == P1) or 
        (GB[3] == GB[6] == GB[9] == P1) or 
        (GB[1] == GB[5] == GB[9] == P1) or 
        (GB[3] == GB[5] == GB[7] == P1)):
        return True
    elif ((GB[1] == GB[2] == GB[3] == P2) or 
        (GB[4] == GB[5] == GB[6] == P2) or 
        (GB[7] == GB[8] == GB[9] == P2) or 
        (GB[1] == GB[4] == GB[6] == P2) or 
        (GB[2] == GB[5] == GB[8] == P2) or 
        (GB[3] == GB[6] == GB[9] == P2) or 
        (GB[1] == GB[5] == GB[9] == P2) or 
        (GB[3] == GB[5] == GB[7] == P2)):
        return False
    else:
        return None

### Take in user input for desired location of marker on their turn, also checks the WhoWins() value
def game_input(Player,P):
    global GameBoard
    
    display_board(GameBoard)
    
    if who_wins(GameBoard,Players[1],Players[2]) == None:
        InputPos = input(f"\nPLAYER{Player}'S TURN, PLEASE SELECT A POSITION[1-9]\n")
        if check_input(InputPos) == True:
            pass
        elif check_input(InputPos) == False:
            print("\nINVALID INPUT, TRY AGAIN.\n")
            game_input(Player,P)

        InputIndex=int(InputPos)
        if InputPos.upper() in GameBoard:
            GameBoard[InputIndex] = P.upper()
            pass
        elif GameBoard[InputIndex] == Players[1] or Players[2]:
            print("\nPOSITION ALREADY TAKEN, PLEASE TRY AGAIN.\n")
            game_input(Player,P)

def play_game():
    Counter = 1
    P1Wins = "\nPlayer 1 Wins!\n"
    P2Wins = "\nPlayer 2 Wins!\n"
    Stale = "\nStalemate!\n"

    while Counter != 10:
        if (who_wins(GameBoard,Players[1],Players[2]) != None):
            Counter = 10
        elif Counter %2 == 0:
        	game_input(1,Players[1])
        	Counter += 1
        elif Counter %2 != 0:
            game_input(2,Players[2])
            Counter += 1
    
    if Counter == 9:
        print(Stale)
        display_board(GameBoard)
    elif (who_wins(GameBoard,Players[1],Players[2]) == True):
        print(P1Wins)
        display_board(GameBoard)
        print(P1Wins)
    elif (who_wins(GameBoard,Players[1],Players[2]) == False):
        print(P2Wins)
        display_board(GameBoard)
        print(P2Wins)

### Asks the user if they would like to play again.
def play_again():
    global GameBoard
    PlayInput=input("\nWOULD YOU LIKE TO PLAY A AGAIN?[Y/N]\n")
    PlayInput=PlayInput.upper()
    if PlayInput in Yes:
        print("\nEXCELLENT LET'S BEGIN\n")
        GameBoard = ['#','1','2','3','4','5','6','7','8','9']
        choose_input()
        play_game()
        play_again()
    elif PlayInput in No:
        print("\nGOODBYE\n")
        exit()
    else:
    	play_again()

welcome_input()

choose_input()

play_game()

play_again()
