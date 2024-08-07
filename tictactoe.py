# Date: 2023.07.12
# Author : Changmin Yi with ChatGPT

import random

class GameBoard:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def print_board(self):
        print('+-----+')
        print('|' + self.board[0] + '|' + self.board[1] + '|' + self.board[2] + '|')
        print('|-+-+-|')
        print('|' + self.board[3] + '|' + self.board[4] + '|' + self.board[5] + '|')
        print('|-+-+-|')
        print('|' + self.board[6] + '|' + self.board[7] + '|' + self.board[8] + '|')
        print('+-----+')

    def is_winner(self, player):
        # TODO 1 - return True if current_player win
        #
        return False

    def is_board_full(self):
        # TODO 2 - return True if board is full
        #
        return False

    def get_free_positions(self):
        return [i for i, cell in enumerate(self.board) if cell == ' ']

    def make_move(self, position):
        self.board[position] = self.current_player

    def player_move(self):
        while True:
            move = input("Where place X? (1-9): ")
            if move.isdigit():
                move = int(move) - 1
                if 0 <= move <= 8 and self.board[move] == ' ':
                    return move
            print("Invalid location, select again.")

    def computer_move(self):
        free_positions = self.get_free_positions()
        move = random.choice(free_positions)
        print("Computer done -> ", move + 1)
        return move

    def play_game(self):
        while True:
            self.print_board()

            if self.current_player == 'X':
                position = self.player_move()
            else:
                position = self.computer_move()

            self.make_move(position)

            if self.is_winner(self.current_player):
                self.print_board()
                if self.current_player == 'X':
                    print("You Win!")
                else:
                    print("You Lose!")
                break
            elif self.is_board_full():
                self.print_board()
                print("Draw!")
                break

            self.current_player = 'O' if self.current_player == 'X' else 'X'
