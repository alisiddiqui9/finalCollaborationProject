
# Final Collaborative Project (CS-043)
# tictactoe.py



# Created by:
#   Ali Siddiqui
#   Owen Lin




# Requirements:



# Design:



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

        return playerName1

    def inputPlayerName2(playerName2):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        print()
        time.sleep(0.2)
        print('ENTER Player 2 name here: ', end = '')
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

    def whoGoesFirs12(turn):
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


    def getBoardCopy(self, board):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard

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




print()
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10

    user = Player()
    game = Game()
    run = RunGame()
    screen = TicTacToe()
    playerLetter1, playerLetter2 = game.inputPlayerLetter()

    playerName1 = user.inputPlayerName1()
    playerName2 = user.inputPlayerName2()


    turn = random.randint(0,1)
    if turn == 0:
        turn = playerName1
    else:
        turn = playerName2



    print('' + turn + ' will go first')

    time.sleep(0.5)
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == playerName1:
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
            time.sleep(0.5)
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
