from art import logo


class GameFunctionality:
    final_input = ""
    play_again = None
    final_input_wrong_answer = False

    @staticmethod
    def print_logo():
        print(logo)

    @staticmethod
    def print_initial_message():
        print("Welcome to my Tic Tac Toe game!")
        print("Below is the start board!")
        print("Each player could chose one square identified from left to right and from up to down with number of line"
              " from 0 to 2 and number of column from 0 to 2. Enter you chose in tuple format ex (1,1)")
        print("If you want to win try to complete any line or any column or one of the diagonals!")
        print("Good luck!")

    def check_play_again_answer(self) -> bool:
        if self.final_input == "y" or "n":
            return True
        else:
            return False

    @staticmethod
    def ask_player_about_game_mode():
        print("They are two type of game mode \nvs PC (type 1) \nand vs HUMAN (type 2) \ntype here: ")

    def ask_player_to_play_again(self):
        self.final_input = input("If you want to play again pres Y! \nFor exit play N! \nType here: ")
        if self.check_play_again_answer():
            if self.final_input == "y":
                self.play_again = True
            elif self.final_input == "n":
                self.play_again = False
            else:
                self.final_input_wrong_answer = True
                print("Wrong option! Please type Y or N!")
                self.ask_player_to_play_again()
