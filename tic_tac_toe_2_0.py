import random
from Clases import *

class Game(Global):
    player_1 = object
    player_2 = object
    board = [['.','.','.'],['.','.','.'],['.','.','.']]
    
    def __init__(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                self.board[i][j] = Inteligence

#1
    def tictactoe_game(self, player_1, player_2):
        self.player_1,self.player_2, = self.set_players_position(player_1, player_2)
        while True:
            self.board,winner, tie = self.player_1.move(self.player_2, self.board)
            if winner or tie:
                return self.player_1.finish(winner,tie,self.board)
            self.board,winner, tie = self.player_2.move(self.player_1, self.board)
            if winner or tie:
                return self.player_2.finish(winner,tie,self.board)

#2
    def set_players_position(self, player_1, player_2):
        rand_pos = random.randint(1, 2)
        if rand_pos == 1:
            return self.set_players_style(player_1, player_2)
        else:
            return self.set_players_style(player_2, player_1)

#3
    def set_players_style(self, player_1, player_2):
        player_1.name = Parameters.red + player_1.name + Parameters.reset
        player_1.symbol = Parameters.red + "x" + Parameters.reset
        player_2.name = Parameters.blue + player_2.name + Parameters.reset
        player_2.symbol = Parameters.blue + "o" + Parameters.reset
        return player_1,player_2
    
    def ask_about_input(self):
        print(self.change_color("Please choose mode:\n\n",Parameters.underline))
        print(self.change_color("1 - HUMAN-AI\n\n ",Parameters.blue))
        print(self.change_color("2 - HUMAN-HUMAN\n\n",Parameters.green))
        print(self.change_color("3 - AI-AI\n\n",Parameters.red))
        return input(self.change_color("Command - ",Parameters.underline))

def main():
    game = Game()
    game.clear_screen()
    #game.loading_game()
    user_input = ""
    game.clear_screen()
    while user_input != "1" and user_input != "2" and user_input != "3":
        user_input = game.ask_about_input()
    if user_input == "1":
        game.clear_screen()
        game.tictactoe_game(Human(input("Registration form:\n  Player name - ")), Artificial_Intelligence())
    elif user_input == "2":
        game.clear_screen()
        game.tictactoe_game(Human(input("Registration form:\n  Player 1 name - ")), Human(input("  Player 2 name - ")))
    else:
        game.clear_screen()
        game.tictactoe_game(Artificial_Intelligence(),Artificial_Intelligence())
        

if __name__ == "__main__":
    main()
    while True:
        user_input = input("\nDo you want to play again? Y/N: ")
        if user_input.lower() == "y":
            os.system("cls || clear")
            main()
        else:
            print("See you soon")
            sys.exit()

