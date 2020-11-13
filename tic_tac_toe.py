import random
<<<<<<< HEAD
=======
import os
import time,sys
>>>>>>> observe

abc = ["A","B","C"]


class colors:
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


def init_board():#[[.,.,.],[.,.,.],[.,.,.]]
    """Returns an empty 3-by-3 board (with .)."""
    board = [['.','.','.'],['.','.','.'],['.','.','.']]
    return board

 
def get_move(board, player):
    col = None
    row = None
<<<<<<< HEAD
    
    while col == None or row == None or col > 3 or row > 3:
        try:
            col = int(input(f"Player {player} choose column (1-3): "))
            row = int(input(f"Player {player} choose row (1-3): "))
            if col > 3 or row > 3:
                raise Exception("Try smaller numbers")
        except ValueError:
            print("It should be digit or try smaller numbers")
        except Exception as arg:
            print(arg)
              
    return row-1, col-1

=======
    while col == None or row == None or col > 3:
        while True:
            row = input(f"Player {players_names[player]} choose row (A-C): " ).upper()
            if row not in abc_check:
                continue
            break
        while True:
            try:
                col = int(input(f"Player {players_names[player]} choose column (1-3): "))#Проблема: нужно два отдельных while сделать 
                if col > 3:
                    continue
                else:
                    break
            except ValueError:
                print("Please write a digit!")
    return row, col-1
>>>>>>> observe

def loading_game():
    procent = 0
    print("Loading...")
    while procent <= 100:
        sys.stdout.write(u"\u001b[1000D" + str(procent) + "%")
        sys.stdout.flush()
        time.sleep(0.05)
        procent += random.randint(1,5)
    print("\nCompleted")
    time.sleep(1)
    os.system("cls || clear")

def enemy_looking_two_cell(board,player,col,check_list = []):
    if check_list.count(enemy[player]) == 2 and "." in check_list:
        return True,check_list.index("."),col
    return False,None,None

def enemy_two_cell(board,player):
    check_list1,check_list2 = [],[]
    board_len = len(board)
    for i in range(board_len):
        for j in range(board_len):
            check_list1.append(board[i][j])
            check,col,row = enemy_looking_two_cell(board,player,i,check_list1)
            if check:
                return check,row,col
            check_list2.append(board[j][i])
            check,row,col = enemy_looking_two_cell(board,player,i,check_list2)
            if check:
                return check,row,col
        check_list1,check_list2 = [],[]
    for i in range(board_len):
        for j in range(board_len):
            if i == j:
                check_list1.append(board[i][j])
                check,row,col = enemy_looking_two_cell(board,player,i,check_list1)
                if check:
                    return check,row,col
    check_list1 = []
    count = 3
    for i in range(board_len):
        count -= 1
        check_list1.append(board[i][count])
        check,row,col = enemy_looking_two_cell(board,player,count,check_list1)
        if check:
            return check,row,col
    return False,0,0

def get_ai_move(board, player):
    """Returns the coordinates of a valid move for Ai on board."""
    row, col = 0, 0
<<<<<<< HEAD
=======
    if board[1][1] == ".":
        row = "B"
        col = 1
    else:
        check,row,col = enemy_two_cell(board,player)
        while True:
            if check:
                return abc[row],col
            else:
                row = abc[random.randint(0,2)]
                col = random.randint(0,2)
            if board[abc_mark[row]][col] != ".":
                continue
            else:
                break
>>>>>>> observe
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    if player == 1 and board[row][col] == ".":
        board[row][col] = "x"
    elif player == 2 and board[row][col] == ".":
        board[row][col] = "o"
    return board


def has_won(board, player):
    
    """Returns True if player has won the game."""    
    return False


def is_full(board):
    """Returns True if board is full."""
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    print("   1   2   3")
    for i in range(3):
<<<<<<< HEAD
        print(f"{abc[i]}  {board[i][0]} | {board[i][1]} | {board[i][2]} \n  ---+---+---")
    pass


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
=======
        print(str(abc[i]),end="  ")
        if i < 2:
            #print(colors.red + str(abc[i]) + colors.reset + "  " + str(board[i][0]) + " | " + str(board[i][1]) + " | " + str(board[i][2]) + "\n"
            for j in range(3):
                if board[i][j] == "x":
                    print(color_1 + str(board[i][j]) + colors.reset, end="")
                elif board[i][j] == "o":
                    print(color_2 + str(board[i][j]) + colors.reset, end="")
                else:
                    print(str(board[i][j]), end="")
                if j < 2:
                    print(" | ", end="")
                elif j == 2:
                    print("\n  ---+---+---")
        else:
            #print(f"{abc[i]}  {board[i][0]} | {board[i][1]} | {board[i][2]} \n  ---+---+---")
            
            for j in range(3):
                if board[i][j] == "x":
                    print(color_1 + str(board[i][j]) + colors.reset, end="")
                elif board[i][j] == "o":
                    print(color_2 + str(board[i][j]) + colors.reset, end="")
                else:
                    print(str(board[i][j]), end="")
                if j < 2:
                    print(" | ", end="")
    print("\n")

def print_result(player,board,board_is_full,players_names,winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    os.system("cls || clear")
    if players_names[player] == "Compukter" and winner:
        print(colors.purple+ "Next time try to beat a calculator first, baby!\n" +colors.white)
    print_board(board)
    if board_is_full:
        print(colors.yellow+ "It's tie!" +colors.reset)
    else:
        print(f"{players_names[player]} is a winner!!!")
    

def human_human(registration_list):
    global step_count
    players_names = {1:colors.red + registration_list[0] + colors.reset,2:colors.blue + registration_list[1] + colors.reset}
>>>>>>> observe
    board = init_board()
    player = 1
    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    while True:
        print_board(board)
        row, col = get_move(board, player)
        board = mark(board, player, row, col)
<<<<<<< HEAD
=======
        if step_count > 4:
            winner = has_won(board,player)
            if winner or step_count == 9:
                print_result(player,board,is_full(),players_names,winner)
                break
>>>>>>> observe
        if player == 1:
            player = 2
        else:
            player = 1

<<<<<<< HEAD
    winner = 0
    print_result(winner)
    
def main_menu():
    userinput = input("Please choose mode:\n 1 - Human-Human\n 2 - Human-AI\nCommand - ")
    while True:
        if userinput == "1":
            tictactoe_game('HUMAN-HUMAN')
            break
        elif userinput == "2":
            tictactoe_game('HUMAN-AI')
            break

=======
def registration_player(mode):
    first_second = {1: colors.red+ 'first' +colors.white, 2: colors.blue+ 'second' +colors.white}
    registration_list = []
    print("\nLet's start registration")
    i = 0
    n = i
    while i < mode:
        try:
            if mode == 1:
                user_input = input("Please, enter your name: ")
            else:
                user_input = input(f"Please, enter {first_second[n+1]} player's name: ") 
                n += 1
                if len(user_input) == 0:
                    raise Exception("Player name must have at least one symbol")
            registration_list.append(user_input)
            i += 1
        except Exception as arg:
            if arg == "Player name must have at least one symbol":
                print(arg)
    return registration_list

def human_ai(registration_list):
    global step_count
    global color_1
    global color_2 
    rand_choise = random.randint(1,2)
    players_names = {1:"",2:""}
    if rand_choise == 1:
        color_1 = colors.red
        color_2 = colors.blue
        players_names[1] = colors.red+ "Compukter" +colors.reset
        players_names[2] = colors.blue+ registration_list[0] +colors.reset
    else:
        color_1 = colors.blue
        color_2 = colors.red 
        players_names[1] = colors.blue+ registration_list[0] +colors.reset
        players_names[2] = colors.red+ "Compukter" +colors.reset
    board = init_board()
    player = 1
    winner = False
    random_word = ""
    file_dir = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(file_dir, "Phrases.txt")
    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    while True:
        os.system("cls || clear")
        if players_names[player] == colors.red+ "Compukter" +colors.reset:
            with open(my_file) as file_word:
                random_word = random.choice(list(file_word)) #рандомный выбор строки из файла
            print(random_word)
            print_board(board)
            time.sleep(2)
            os.system("cls || clear")
            row_c, col_c = get_ai_move(board, player)
            board = mark(board, player, row_c, col_c)
            if step_count > 4:
                winner = has_won(board,player)
                if winner or step_count == 9:
                    print_result(player,board,is_full(),players_names,winner)
                    break
            if players_names[1] == colors.red+ "Compukter" +colors.reset:
                player = 2
            else:
                player = 1
        if players_names[player] == colors.blue+ registration_list[0] +colors.reset:
            print(random_word)
            print_board(board)
            row, col = get_move(board, player,players_names)
            board = mark(board, player, row, col)
            if step_count > 4:
                winner = has_won(board,player)
                if winner or step_count == 9:
                    print_result(player,board,is_full(),players_names,winner)
                    break
            if players_names[1] == colors.blue+ registration_list[0] +colors.reset:
                player = 2
            else:
                player = 1

def tictactoe_game(mode_index,mode='HUMAN-HUMAN'):
    if mode == "HUMAN-HUMAN":
        human_human(registration_player(mode_index))
    elif mode == "HUMAN-AI":
        human_ai(registration_player(mode_index))
    
def main_menu():
    os.system("cls || clear")
    loading_game()
    userinput = input(colors.underline+"Please choose mode:\n\n"+colors.white+ colors.blue+ " 1 - HUMAN-AI\n\n "+colors.green+ "2 - HUMAN-HUMAN"+colors.white+ colors.underline+"\n\nCommand - "+colors.reset)
    while userinput != "1" and userinput != "2":
        userinput = input(colors.underline+"Please choose mode:\n\n"+colors.white+ colors.blue+ " 1 - HUMAN-AI\n\n "+colors.green+ "2 - HUMAN-HUMAN"+colors.white+ colors.underline+"\n\nCommand - "+colors.reset)
    if userinput == "1":
        tictactoe_game(int(userinput),'HUMAN-AI')     
    else:
        tictactoe_game(int(userinput),'HUMAN-HUMAN')
            
>>>>>>> observe
if __name__ == '__main__':
    main_menu()
    while True:
        userinput = input("\nDo you want to play again? Y/N: ")
        if userinput == "Y" or userinput == "y":
            os.system("cls || clear")
            main_menu()
        else:
            print("See you soon")
            sys.exit()
        
