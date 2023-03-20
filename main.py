from board import Board
from gamefunctionality import GameFunctionality

play_again = True
while play_again:
    play_game = True
    game_functionality = GameFunctionality()
    tictactoe_board = Board()
    game_functionality.print_logo()
    game_functionality.print_initial_message()
    tictactoe_board.print_board()
    tictactoe_board.ask_player_about_game_mode()
    while play_game:
        correct_choice = True
        tictactoe_board.chose_current_player()
        while correct_choice:
            tictactoe_board.ask_player_to_insert_position()
            if tictactoe_board.check_line_and_column():
                correct_choice = False

        tictactoe_board.add_element_at_line_and_column()
        if tictactoe_board.check_if_player_win():
            print(tictactoe_board.won_mode)
            play_game = False
        elif not tictactoe_board.check_if_player_win():
            if tictactoe_board.check_if_draw():
                print(tictactoe_board.won_mode)
                play_game = False
        if not play_game:
            game_functionality.ask_player_to_play_again()
            if game_functionality.play_again:
                play_again = True
            elif not game_functionality.play_again:
                play_again = False
                correct_answer = False
