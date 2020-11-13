import random
import os
import sys
import time

class Parameters:# Static parameters class
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    white = '\033[0m'
    bold = '\033[1m'
    reset = '\u001b[0m'
    underline = '\033[4m'
    abc = {0:"A",1:"B",2:"C"}
    abc_to_digit = {"A": 0, "B":1, "C":2}
    abc_list = ["A","B","C"]

class Global: # Global calass with global functions
    loading_time = 0.01
    a_i_time_sleep = 2

    end_count = 0

    def clear_screen(self):
        os.system("cls || clear")
    
    def check_input(self,text):
        while True:
            user_input = input(text)
            if user_input.lower() == "quit":
                quit()
            break
        return user_input
    
    def print_board(self,board):
        print("   1   2   3")
        for i in range(len(board)):
            if i < 2:
                print(Parameters.abc[i] + "  " + board[i][0].symbol + " | " + board[i][1].symbol + " | " + board[i][2].symbol + "\n  ---+---+---")
            else:
                print(Parameters.abc[i] + "  " + board[i][0].symbol + " | " + board[i][1].symbol + " | " + board[i][2].symbol + "\n")

    def loading_game(self):
        procent = 0
        print("Loading...")
        while procent <= 100:
            sys.stdout.write(u"\u001b[1000D" + str(procent) + "%")
            sys.stdout.flush()
            time.sleep(self.loading_time)
            procent += 1
        print("\nCompleted")
        time.sleep(1)
        os.system("cls || clear")
    
    def change_color(self,text,color):
        return color + text + Parameters.reset

class Inteligence(Global): # Parent inteligence class for Human and AI
    symbol = "."
    name = ""

    def finish(self,winner,tie,board):# Method is calling when someone win or medked tie
        self.clear_screen()
        self.print_board(board)
        if winner:
            print(self.name + " is s Winner!")
        elif tie:
            print("Tie")
        Global.end_count = 0

    def get_file_path(self,file_name):# Method which get file path
        file_dir = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(file_dir, file_name)
        return my_file
    
    def mark(self, board , row, col):# Mark a game board
        if board[row][col] == Inteligence:
            board[row][col] = self
            Global.end_count += 1
        return board
    
    def check_finish(self,board,enemy):# Check the type game-end
        winner = self.has_won(board,enemy)
        tie = False
        if Global.end_count == 9:
            tie = True
        return winner,tie
            
    def has_won(self,board,player):# Сheck for possible winnings
        check_list1 = []
        check_list2 = []
        board_len = len(board)
        for i in range(board_len):
            for j in range(board_len):
                check_list1.append(board[i][j])
                check_list2.append(board[j][i])
            if (Inteligence not in check_list1 and player not in check_list1) or (Inteligence not in check_list2 and player not in check_list2):
                return True
            check_list1,check_list2 = [],[]
        for i in range(board_len):
            for j in range(board_len):
                if i == j:
                    check_list1.append(board[i][j])
        if Inteligence not in check_list1 and player not in check_list1:
            return True
        check_list1 = []
        count = 2
        for i in range(board_len):
            check_list1.append(board[i][count])
            count -= 1
        if Inteligence not in check_list1 and player not in check_list1:
            return True
        return False


class Human(Inteligence): # Human class
    def __init__(self, name):
        self.name = name
        pass
    def get_move(self):# Get human move
        col = None
        row = None
        while col == None or row == None or col > 3:
            while True:
                row = input("Player " + self.name + " choose row (A-C): " ).upper()
                if row not in Parameters.abc_list:
                    continue
                break
            while True:
                try:
                    col = int(input("Player " + self.name + " choose column (1-3): "))
                    if col > 3:
                        continue
                    else:
                        break
                except ValueError:
                    print("Please write a digit!")
        return Parameters.abc_to_digit[row], col-1

    def move(self, enemy, board):# Human move
        self.clear_screen()
        self.print_board(board)
        row,col = self.get_move()
        board = self.mark(board,row,col)
        winner,tie = self.check_finish(board,enemy)
        return board,winner,tie

class Artificial_Intelligence(Inteligence): # AI class

    lines_file_name = ""

    def __init__(self):
        self.name = "Compukter"
        self.lines_file_name = self.get_file_path("Phrases.txt")

    def check_two_cell(self, board, player):# Return True and coordinates of sell if the player has marked two out of three cells in the same row
        check_list1,check_list2 = [],[]
        board_len = len(board)
        for i in range(board_len):
            for j in range(board_len):
                check_list1.append(board[i][j])
                check,col,row = self.enemy_looking_two_cell(board,player,check_list1,"first_simple",i)
                if check:
                    return check,row,col
                check_list2.append(board[j][i])
                check,row,col = self.enemy_looking_two_cell(board,player,check_list2,"first_simple",i)
                if check:
                    return check,row,col
            check_list1,check_list2 = [],[]
        for i in range(board_len):
            for j in range(board_len):
                if i == j:
                    check_list1.append(board[i][j])
                    check,row,col = self.enemy_looking_two_cell(board,player,check_list1,"second_simple")
                    if check:
                        return check,row,col
        check_list1 = []
        count = 3
        for i in range(board_len):
            count -= 1
            check_list1.append(board[i][count])
            check,row,col = self.enemy_looking_two_cell(board,player,check_list1,"third_simple")
            if check:
                return check,row,col
        return False,0,0

    def enemy_looking_two_cell(self, board, player, check_list, mode, col = None):# Help method for "check_two_cell"
        if check_list.count(player) == 2 and Inteligence in check_list:
            if mode == "first_simple":
                return True,check_list.index(Inteligence),col
            elif mode == "second_simple":
                return True,check_list.index(Inteligence),check_list.index(Inteligence)
            elif mode == "third_simple":
                col = check_list.index(Inteligence)
            if col == 0:
                col = 2
            elif col == 2:
                col = 0
            return True,check_list.index(Inteligence),col
        return False,None,None
    
    def get_ai_move(self, board, enemy):# Get AI move
        row, col = 0, 0
        check, row, col = self.check_two_cell(board, self)
        if check:
            return row, col
        check, row, col = self.check_two_cell(board,enemy)
        if check:
            return row, col
        check, row, col = self.check_coreners(enemy,board)
        if check:
            return row, col
        while True:
            row = Parameters.abc_to_digit[Parameters.abc[random.randint(0,2)]]
            col = random.randint(0,2)
            if board[row][col] != Inteligence:
                continue
            else:
                return row, col
    
    def check_coreners(self, enemy, board):
        row, col = 0, 0
        right_list = []
        left_list = []
        for i in range(len(board)):
            right_list.append(board[0][i])
            left_list.append(board[i][0])
            if i == 2:
                for j in range(1,3):
                    right_list.append(board[j][i])
                    left_list.append(board[i][j])
        if enemy not in left_list or enemy not in right_list:
            if board[0][0] == Inteligence:
                return True, 0,0
            elif board[2][2] == Inteligence:
                return True, 2,2
        else:
            if board[0][0] == Inteligence:
                return True, 0,0
            elif board[2][2] == Inteligence:
                return True, 2,2
        if enemy not in left_list and Inteligence in left_list:
            if board[2][0] == Inteligence:
                return True, 2,0
        elif enemy not in right_list and Inteligence in right_list:
            if board[0][2] == Inteligence:
                return True, 0, 2

        return  False, row, col

    
    def move(self,enemy,board):# AI move
        self.clear_screen()
        print(self.name + ": " + self.get_random_line())
        self.print_board(board)
        time.sleep(self.a_i_time_sleep)
        row,col = self.get_ai_move(board,enemy)
        board = self.mark(board,row,col)
        winner,tie = self.check_finish(board,enemy)
        return board,winner,tie


    def get_random_line(self):# Get random line from file
        with open(self.lines_file_name) as file_word:
                return random.choice(list(file_word))

