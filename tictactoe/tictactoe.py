
# Final Collaborative Project (CS-043)
# tictactoe.py

# Programmed By:
# Ali Siddiqui
# Owen Lin


# REQUIREMENTS OF THE PROGRAM:
# In this game, we have 2 players.
# When the game begins, player 1 will choose if they want X or O.
# Then, the game will request for the names of the two players.
# The game will randomly choose who goes first (player 1 or player 2).

# The entire objective of the game is to get THREE of your letters a consecutive row.
# A player can win when they have three of their letters in a straight line.
# For victory, your 3 letters can be horizontal, vertical, or even diagonal.
# The game will run until someone wins, or when there is a tie.

# Ties occur when there is no winner, since both players were
# not able to get 3 of their letters in a row, and when all of
# the squares of the board have been occupied with letters.

# When it is your turn (the game will inform you), you must try to block the other
# player from winning, or you must place your letter in a position that
# will lead yourself into victory.

# When asked, in order to place your letter into the board, you must place a number (1-9),
# corresponding to the square you wish to place your letter.

# Here is an easy overview, of each number, and its corresponding square.
#            			(Numbers 1-9)
#             TicTacToe Board
#    (TL) - 7 | (TM) - 8 | (TR) - 9
#    ------------------------------
#    (ML) - 4 | (MC) - 5 | (MR) - 6
#    ------------------------------
#    (BL) - 1 | (BM) - 2 | (BR) - 3

# Here's what it means:
# ENTER 1 for Bottom Left (BL)
# ENTER 2 for Bottom Middle (BM)
# ENTER 3 for Bottom Right (BR)

# ENTER 4 for Middle Left (ML)
# ENTER 5 for Middle Center (MC)
# ENTER 6 for Middle Right (MR)

# ENTER 7 for Top Left (TL)
# ENTER 8 for Top Middle (TM)
# ENTER 9 for Top Right (TR)



# If you enter a number (for the position on the board),
# and if the position has already been filled,
# the game will ask you for a valid number, in order to insert your letter into that square.


# Recap of Rules:
# You must enter in a valid number from 1-9, otherwise your piece will not be placed.
# You cannot place a piece in a square that has already been taken by another piece.
# You must try to win, by placing your 3 of your letters in a straight row
# (either horizontally, vertically, or diagonally)


# Remember the Grid Format:
# Top Row - 7 8 9
# Middle Row - 4 5 6
# Bottom Row - 1 2 3


# Player 1 chooses either X or O to use in the game.
# Enter in the names of the two people playing.
# A random player will be chosen to go first.
# To put your piece in, enter a number from 1-9.

# The game will end once a player gets 3 of their pieces in a row.
# Those 3 pieces can be horizontal, vertical, or diagonal to make up the 3 in a row.
# If the grid is filled and no player has gotten 3 in a row,
# the game ends as a tie.
# If you want to play again, simply enter “yes” when asked, and the game will restart




# The Design of the Program:

# The TicTacToe two-player game has 4 classes total.
# The classes are referred to as; class Player, class Game, class TicTacToe,
# and class RunGame. Since we have 4 classes, we have 4 objects.

# The objects are created when the program first runs. T
# he objects are; user, game, run, and screen.
# Classes are known as “cookie cutters” for objects.
# So our 4 classes form our four objects.
# Since we have objects, we can implement object-oriented programming.
# Object oriented programming has the potential to make complex source codes easier
# in more complex projects.

# We created our 4 classes based on the similarities between the user-defined functions.
# For example, functions inside of the class Player; all have something to do with the user.
# It includes a function to ask names of both players, and asks the players if they
# want to restart.
# The next class is class Game, which includes all user-defined functions related
# to the actual TicTacToe game.

# This is where player 1 chooses if they want to be X or O, and this is where the
# source code assigns player 2’s letter (based on Player 1’s response).
# Player 2 becomes X, if player 1 chooses O. Player 2 becomes O, if player 1 chooses X.
# Class Game also includes the directions() user-defined function.
# When this function is called (when the user asks for it) it gives the user
# a great-detailed explanation of the game.

# It includes how the game functions, how to insert your letter into
# the TicTacToe board, and the main objectives of the TicTacToe game.
# This function is useful for all players
# Also, within the class Game, we have the whoGoesFirst1() functions that will
# randomly decide which player (1 or 2) will go first when the game runs.

# The next class is, class TicTacToe. This is where many of the functions related to
# TicTacToe are located.
# In this class, we have the drawBoard() user-defined function,
# which creates the board for the game.
# This is the same board the players see when the game is running,
# and is the most important part of the game (since it shows where the letters are in the board).

# It also has the makeMove() user-defined function,which will place the user’s letter
# onto the board, at their desired place.
# Within the class TicTacToe, we have the isWinner() user-defined function,
# which will constantly check after each player’s turn, to see if they have achieved
# a three in a row.
# We also have the isSpaceFree() user-defined function, which will check if the
# place the player wants to place their letter has already been taken.
# If the space is free, then the game will allow the letter to be placed there.

# Finally, within the class TicTacToe, we have the isBoardFull() user-defined
# function, which will check after each player’s turn, to see if the game is
# considered “over” if the players cannot add more letters onto the board.

# In our last class within the source code, we have the class RunGame.
# This class mainly has user-defined functions to get the player’s move,
# and checks if the inserted string is a number that represents the position
# on the board.

# These user-defined functions are getPlayer1Move() and getPlayer2Move().
# After this, we created objects for each class,
# in order to use their user-defined functions.
# We create an object called user for class Player.
# An object called game for class Game.
# An object called run for class RunGame. And an object called screen for class TicTacToe.
# Then we use object-oriented programming
# when we call these functions inside of these classes,
# and the game runs successfully without bugs.




import random
import time

class Player:
    def inputPlayerName1(playerName1):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        print()
        time.sleep(0.2)
        print('ENTER Player 1 name here: ', end = '')
        playerName1 = input()
        if playerName1 == '':
            print('ENTER Player 1 name here: ', end='')
            playerName1 = input()
        return playerName1

    def inputPlayerName2(playerName2):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        print()
        time.sleep(0.2)
        print('ENTER Player 2 name here: ', end = '')
        playerName2 = input()
        if playerName2 == '':
            time.sleep(0.2)
            print('ENTER Player 2 name here: ', end='')
            playerName2 = input()
        print()
        return playerName2

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print()
        print('GAME OVER')
        print('ENTER yes, to restart the game (yes or no): ', end = '')
        return input().lower().startswith('y')


class Game:
    def directions(self):
        print()
        print()
        time.sleep(0.3)
        print('TicTacToe Directions: ')
        print()
        print ('\tIn this game, we have 2 players.')
        print()
        time.sleep(1)
        print('\tHere is how we play TicTacToe.')
        print()
        time.sleep(1)
        print('\tWhen the game begins, player 1 will choose if they want X or O.')
        print()
        time.sleep(1)
        print('\tThen, the game will request for the names of the two players.')
        print()
        time.sleep(1)
        print('\tThe game will randomly choose who goes first (player 1 or player 2)')
        print()
        print()
        time.sleep(3)
        print('\tThe entire objective of the game is to get THREE of your letters a consecutive row.')
        print()
        time.sleep(1)
        print('\tA player can win when they have three of their letters in a straight line')
        print()
        time.sleep(1)
        print('\tFor victory, your 3 letters can be horizontal, vertical, or even diagonal.')
        print()
        time.sleep(1)
        print('\tThe game will run until someone wins, or when there is a tie.')
        print()
        time.sleep(1)
        print('\tTies occur when there is no winner, since both players were not able to get 3 of their letters in a row...')
        print()
        time.sleep(1)
        print('\tand when all of the squares of the board have been occupied with letters. ')
        print()
        print()
        time.sleep(4)
        print('\tWhen it is your turn (the game will inform you), you must try to block the other player from winning...')
        print()
        time.sleep(1)
        print('\tor you must place your letter in a position that will lead yourself into victory')
        print()
        time.sleep(1)
        print('\tWhen asked, in order to place your letter into the board...')
        print()
        time.sleep(1)
        print('\tyou must place a number (1-9), corresponding to the square you wish to place your letter')
        print()
        print()
        time.sleep(4)
        print('''Here is an easy overview, of each number, and its corresponding square.
                    (Numbers 1-9)
                        
                   TicTacToe Board
            (TL) - 7 | (TM) - 8 | (TR) - 9
            ------------------------------
            (ML) - 4 | (MC) - 5 | (MR) - 6
            ------------------------------
            (BL) - 1 | (BM) - 2 | (BR) - 3
            
            ''')
        time.sleep(4)
        print("Here's what it means: ")
        time.sleep(1.5)
        print('''
        ENTER 1 for Bottom Left (BL)
        ENTER 2 for Bottom Middle (BM)
        ENTER 3 for Bottom Right (BR)
        ENTER 4 for Middle Left (ML)
        ENTER 5 for Middle Center (MC)
        ENTER 6 for Middle Right (MR)
        ENTER 7 for Top Left (TL)
        ENTER 8 for Top Middle (TM)
        ENTER 9 for Top Right (TR)
        ''')
        print()
        print()
        time.sleep(4)
        print('\tIf you enter a number (for the position on the board)')
        print()
        time.sleep(1)
        print('\tand if the position has already been filled,')
        print()
        time.sleep(1)
        print('\tthe game will ask you for a valid number, in order to insert your letter into that square.')
        print()
        print()
        print()
        time.sleep(2)
        print('Press ENTER to continue: ', end = '')
        input()
        time.sleep(0.4)

    def inputPlayerLetter(letter):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print()
            time.sleep(0.2)
            print('Player 1: Choose X or O?')
            print('ENTER here: ', end = '')
            letter = input().upper()

        # the first element in the tuple is the player1's letter, the second is player2's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst1(turn):
        # Randomly choose the player who goes first.
        if turn == 0:
            turn = playerName1
            return turn

    def whoGoesFirst2(turn):
        if turn == 1:
            turn = playerName2
            return turn

class TicTacToe:
    def drawBoard(self, board):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    def makeMove(self, board, letter, move):
        board[move] = letter

    def __getitem__(self, items):
        print(type(items), items)

    def isWinner(self, bo, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal

    def isSpaceFree(self, board, move):
        # Return true if the passed move is free on the passed board.
        return board[move] == ' '

    def isBoardFull(self, board):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if screen.isSpaceFree(board, i):
                return False
        return True


class RunGame:
    def getPlayer1Move(self, board):
        # Let the player1 type in his move.
        move1 = ' '
        while move1 not in '1 2 3 4 5 6 7 8 9'.split() or not screen.isSpaceFree(board, int(move1)):
            print()
            print('' + playerName1 + ', what is your move? (1-9)')
            print('ENTER here: ', end = '')
            move1 = input()
        return int(move1)

    def getPlayer2Move(self, board):
        # Let the player2 type in his move.
        move2 = ' '
        while move2 not in '1 2 3 4 5 6 7 8 9'.split() or not screen.isSpaceFree(board, int(move2)):
            print()
            print('' + playerName2 + ', what is your next move? (1-9)')
            print('ENTER here: ', end = '')
            move2 = input()
        return int(move2)

    def __getitem__(self, items):
        print(type(items), items)


# This is where the Game begins:

print()
print('Welcome to Tic Tac Toe!')
print()
time.sleep(0.2)

print("Press ENTER to continue: ", end = "")
input()
print()

user = Player()
game = Game()
run = RunGame()
screen = TicTacToe()

print("ENTER yes, if you want to see the instructions: ", end = "")
if input().lower().startswith('y'):
    game.directions()


playerLetter1, playerLetter2 = game.inputPlayerLetter()

playerName1 = user.inputPlayerName1()
playerName2 = user.inputPlayerName2()

while True:
    # Reset the board
    theBoard = [' '] * 10


    turn = random.randint(0,1)
    if turn == 0:
        turn = playerName1
    else:
        turn = playerName2


    print()
    print('' + turn + ' will go first')

    gameIsPlaying = True

    while gameIsPlaying:
        if turn == playerName1:
            time.sleep(0.2)
            # Player1's turn.
            print()
            screen.drawBoard(theBoard)
            move = run.getPlayer1Move(theBoard)
            screen.makeMove(theBoard, playerLetter1, move)

            if screen.isBoardFull(theBoard):
                if screen.isWinner(theBoard, playerLetter1) == False and screen.isWinner(theBoard, playerLetter2) == False:
                    screen.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
            if screen.isWinner(theBoard, playerLetter1):
                screen.drawBoard(theBoard)
                print('' + playerName1 + ' has won the game!')
                gameIsPlaying = False
            elif screen.isWinner(theBoard, playerLetter2):
                screen.drawBoard(theBoard)
                print('' + playerName2 + ' has won the game!')
                gameIsPlaying = False
            elif screen.isBoardFull(theBoard):
                    screen.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
            else:
                turn = playerName2

        else:
            # Player2's turn.
            print()
            time.sleep(0.2)
            screen.drawBoard(theBoard)
            move = run.getPlayer2Move(theBoard)
            screen.makeMove(theBoard, playerLetter2, move)

    # why does this first line not work?
            if screen.isBoardFull(theBoard):
                if screen.isWinner(theBoard, playerLetter1) == False and screen.isWinner(theBoard, playerLetter2) == False:
                    screen.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
            if screen.isWinner(theBoard, playerLetter1):
                screen.drawBoard(theBoard)
                print('' + playerName1 + ' has won the game!')
                gameIsPlaying = False
            elif screen.isWinner(theBoard, playerLetter2):
                screen.drawBoard(theBoard)
                print('' + playerName2 + ' has won the game!')
                gameIsPlaying = False
            elif screen.isBoardFull(theBoard):
                    screen.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
            else:
                turn = playerName1

    if not user.playAgain():
        break
