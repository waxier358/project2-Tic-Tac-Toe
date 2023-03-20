import random


class Board:
    """create game board"""
    def __init__(self):
        self.matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.line: str
        self.column: str
        self.current_player: str
        self.current_player_chose_index = 0
        self.nr_entry_on_board = 0
        self.won_mode: str
        self.game_mode: str

    def print_board(self):
        """print game board
            0   1   2
        0 |   |   |   |
        1 |   |   |   |
        2 |   |   |   |
        """
        print("    0   1   2")
        print("0", "|", self.matrix[0][0], "|", self.matrix[0][1], "|", self.matrix[0][2], "|")
        print("1", "|", self.matrix[1][0], "|", self.matrix[1][1], "|", self.matrix[1][2], "|")
        print("2", "|", self.matrix[2][0], "|", self.matrix[2][1], "|", self.matrix[2][2], "|")

    def ask_player_about_game_mode(self):
        """chose game mode
        They are two type of game mode
        vs PC (type 1) and
        vs HUMAN (type 2)
        type here:
        """
        message = input("They are two type of game mode \nvs PC (type 1) and \nvs HUMAN (type 2) \ntype here: ")
        if message == "1" or message == "2":
            self.game_mode = message
        else:
            self.ask_player_about_game_mode()

    def chose_current_player(self):
        if self.current_player_chose_index % 2 == 0:
            self.current_player = "X"
        elif self.current_player_chose_index % 2 == 1:
            self.current_player = "0"
        self.current_player_chose_index += 1

    def player_chose_random_position(self):
        available_positions = []
        for nr_line in range(0, len(self.matrix)):
            for nr_column in range(0, len(self.matrix)):
                if self.matrix[nr_line][nr_column] == " ":
                    available_positions.append((nr_line, nr_column))
        self.line = random.choice(available_positions)[0]
        self.column = random.choice(available_positions)[1]

    def ask_player_to_insert_position(self):
        if self.game_mode == "1":
            if self.current_player == "X":
                self.line = input(f"Player {self.current_player} chose line number: ")
                self.column = input(f"And column number: ")
            elif self.current_player == "0":
                self.player_chose_random_position()
        elif self.game_mode == "2":
            self.line = input(f"Player {self.current_player} chose line number: ")
            self.column = input(f"And column number: ")
        else:
            print("You enter an invalid option. Please try again!")
            self.ask_player_about_game_mode()

    def check_if_position_is_free(self) -> bool:
        if self.matrix[int(self.line)][int(self.column)] == " ":
            return True
        else:
            self.current_player_chose_index -= 1
            return False

    def check_line_and_column(self) -> bool:
        if 0 <= int(self.line) < 3 and 0 <= int(self.column) < 3:
            return True
        else:
            print("You chose a wrong option!Please type again!")
            return False

    def add_element_at_line_and_column(self):
        if self.check_if_position_is_free():
            self.matrix[int(self.line)][int(self.column)] = self.current_player
            self.print_board()
            self.nr_entry_on_board += 1
        else:
            print(f"Position line {self.line} and column {self.column} already taken!")

    def check_if_player_win(self) -> bool:
        # check line
        for line_nr in range(0, 3):
            if self.matrix[line_nr][0] == self.matrix[line_nr][1] == self.matrix[line_nr][2] != " ":
                self.won_mode = f"Player {self.current_player} win! Line {line_nr} completed!"
                return True
        for column_nr in range(0, 3):
            if self.matrix[0][column_nr] == self.matrix[1][column_nr] == self.matrix[2][column_nr] != " ":
                self.won_mode = f"Player {self.current_player} win! Column {column_nr} completed!"
                return True
        if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] != " ":
            self.won_mode = f"Player {self.current_player} win! First diagonal completed!"
            return True
        if self.matrix[2][0] == self.matrix[1][1] == self.matrix[0][2] != " ":
            self.won_mode = f"Player {self.current_player} win! Second diagonal completed!"
            return True
        else:
            return False

    def check_if_draw(self):
        if self.nr_entry_on_board == 9:
            if not self.check_if_player_win():
                self.won_mode = "Draw game!"
                return True
