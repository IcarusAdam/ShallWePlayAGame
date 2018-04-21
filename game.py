### ShallWePlayAGame?
### Global Variables ### Subject to Change
InputBreak = 1
Player1 = None
Player2 = None
GameBoard = ['#','1','2','3','4','5','6','7','8','9']
AllowedPos = ["#","1","2","3","4","5","6","7","8","9"]
Counter = 0

### User Input ## Welcomes Player and asks them to play a game?
def WelcomeInput():
    YesNo = input("\nGREETINGS\n\nSHALL WE PLAY A GAME? (Y/N)\n\n")
    if YesNo.upper() == "Y":
        print("\nEXCELLENT LET'S BEGIN\n")
    elif YesNo.upper() == "N":
        print("\nGOODBYE\n")
        exit()
    else:
        WelcomeInput()

### Pretty self explainatory, Prints Board. Don't know how to make this bigger or prettier yet.
def DisplayBoard(Board):
    print(f"\n\n{Board[1]}|{Board[2]}|{Board[3]}\n-----\n{Board[4]}|{Board[5]}|{Board[6]}\n------\n{Board[7]}|{Board[8]}|{Board[9]}\n\n".format(Board))

### Resets the board back to Originals
def ResetBoard():
    global InputBreak
    global Player1
    global Player2
    global GameBoard
    global AllowedPos
    global Counter
    InputBreak = 0
    Player1 = None
    Player2 = None
    GameBoard = ['#','1','2','3','4','5','6','7','8','9']
    AllowedPos = ["#","1","2","3","4","5","6","7","8","9"]
    Counter = 0

### User Input ### Player1 Selects either X or O
def PlayerInput():
        global InputBreak
        global Player1
        global Player2
        Player1 = input("PLAYER1 PLEASE PICK X OR 0.\n")
        if Player1.upper() == "X":
            print("\nPLAYER 1 IS X\n")
            Player2='O'
            print("PLAYER 2 IS O\n")
        elif Player1.upper() == "O":
            print("\nPLAYER 1 IS O\n")
            Player2='X'
            print("PLAYER 2 IS X\n")
        else:
            print("\nINVALID INPUT, TRY AGAIN.\n")
            Player1=None
            Player2=None
            InputBreak += 1

### User Input ### Player1 Selects either X or O
def ChooseInput():
    global InputBreak
    global Player1
    global Player2
    
    PlayerInput()
    if InputBreak == 4:
        exit()
    while Player1 == None:
        PlayerInput()
    else:
        pass

### Checks to see if Win/Lose/Stalemate has occured.
def WhoWins():
    if ((GameBoard[1]==GameBoard[2]==GameBoard[3]==Player1) or 
    	(GameBoard[4]==GameBoard[5]==GameBoard[6]==Player1) or 
    	(GameBoard[7]==GameBoard[8]==GameBoard[9]==Player1) or 
    	(GameBoard[1]==GameBoard[4]==GameBoard[6]==Player1) or 
    	(GameBoard[2]==GameBoard[5]==GameBoard[8]==Player1) or 
    	(GameBoard[3]==GameBoard[6]==GameBoard[9]==Player1) or 
    	(GameBoard[1]==GameBoard[5]==GameBoard[9]==Player1) or 
    	(GameBoard[3]==GameBoard[5]==GameBoard[7]==Player1)):
        return 1
    elif ((GameBoard[1]==GameBoard[2]==GameBoard[3]==Player2) or 
    	(GameBoard[4]==GameBoard[5]==GameBoard[6]==Player2) or 
    	(GameBoard[7]==GameBoard[8]==GameBoard[9]==Player2) or 
    	(GameBoard[1]==GameBoard[4]==GameBoard[6]==Player2) or 
    	(GameBoard[2]==GameBoard[5]==GameBoard[8]==Player2) or 
    	(GameBoard[3]==GameBoard[6]==GameBoard[9]==Player2) or 
    	(GameBoard[1]==GameBoard[5]==GameBoard[9]==Player2) or 
    	(GameBoard[3]==GameBoard[5]==GameBoard[7]==Player2)):
        return 2
    elif Counter==9:
        return 3
    else:
        pass

### Take in user input for desired location of marker on their turn, also checks the WhoWins() value
def GameInput(Player,Letter):
    global AllowedPos
    global GameBoard
    global Counter
    DisplayBoard(GameBoard)
    if WhoWins() == None:
        InputPos = input(f"PLAYER{Player}'S TURN, PLEASE SELECT A POSITION[1-9]\n".format())
        if InputPos.upper() in AllowedPos:
            InputIndex=int(InputPos)
            AllowedPos[InputIndex] = Letter.upper()
            GameBoard[InputIndex] = Letter.upper()
            pass
        else:
            print("POSITION ALREADY TAKEN, PLEASE TRY AGAIN.\n")
            GameInput(Player,Letter)
    elif WhoWins()==1:
        print("PLAYER1 WINS!")
        DisplayBoard(GameBoard)
        Counter += 10
    elif WhoWins()==2:
        print("PLAYER2 WINS!")
        DisplayBoard(GameBoard)
        Counter += 10
    elif WhoWins()==3:
        print("STALEMATE!")
        DisplayBoard(GameBoard)

### Runs the GameInput Function whilst inserting Player1/Player2 details into the function, checks if the Counter has reached 10
def PlayGame():
    global Counter
    while Counter < 10:
        if Counter%2!=0:
            GameInput(1,Player1)
            Counter += 1
        elif Counter%2==0:
            GameInput(2,Player2)
            Counter += 1
### Asks the user if they would like to play again.
def PlayAgain():
    PlayInput=input("\nWOULD YOU LIKE TO PLAY A AGAIN?[Y/N]")
    if PlayInput.upper == "Y" or "Yes":
        print("\nEXCELLENT LET'S BEGIN\n")
        ResetBoard()
        ChooseInput()
        PlayGame()
        PlayAgain()
    elif PlayInput.upper == "N" or "No":
        exit()
    else:
        print("\nGOODBYE\n")
        exit()

WelcomeInput()

ChooseInput()

PlayGame()

PlayAgain()
