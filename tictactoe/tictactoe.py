
# Final Collaborative Project (CS-043)
# tictactoe.py



# Created by:
#   Ali Siddiqui
#   Owen Lin


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
