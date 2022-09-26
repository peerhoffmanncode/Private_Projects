import random
import time
import os
import colorama
import c4_Board as c4_Board
import c4_KIPlayer as c4_KIPlayer

def user_input(board_size) -> int:
    while True:
        user_choice = input(f"Enter a position [0-{board_size-1}] : ")
        try:
            place_at_rnd = int(user_choice)
            if 0 <= place_at_rnd < board_size:
                return place_at_rnd
            else:
                print("wrong input!")
        except ValueError:
            print("wrong input!")

def KI_player_move(board: c4_Board.Board, KIplayer: c4_KIPlayer.KIPlayer, player_symbol):
    # Cpu Player
    print (f"[{player_symbol}] players turn")
    pl_win = KIplayer.check_player_win()
    en_win = KIplayer.check_enemy_win()
    if pl_win != -1:
        place_at_rnd = pl_win
        print(f"player {player_symbol} can win!")
    elif en_win != -1:
        place_at_rnd = en_win
        print("prohibit enemy players win!")
    else:
        options_to_choosefrom = []
        options_to_choosefrom = KIplayer.play_one_turn_ahead()
        print(f"|play_one_turn_ahead| -> left options to choose from {options_to_choosefrom}")
        options_to_choosefrom = KIplayer.play_best_option(options_to_choosefrom)
        print(f"|play_best_option|    -> left options to choose from {options_to_choosefrom}")
        if options_to_choosefrom:
            # fields restricted
            print(f"KI will chose from this list => {options_to_choosefrom}")
            place_at_rnd = random.choice(options_to_choosefrom)
        else:
            # can use any field!
            print("KI will chose from random object")
            place_at_rnd = random.randint(0, board.board_size)
    print()
    input(f"final KI decision >>{place_at_rnd}<< press enter to continue...")
    return place_at_rnd

##################################################### MAIN FUNCTION #############################################
def main():
    """This is the main program"""
    game_size = 7
    player_symbol1 = "0"
    player_symbol2 = "O"
    # create all objects
    main_board1 = c4_Board.Board(game_size, player_symbol1, player_symbol2)
    cpu_player1 = c4_KIPlayer.KIPlayer(main_board1, player_symbol1, player_symbol2)
    cpu_player2 = c4_KIPlayer.KIPlayer(main_board1, player_symbol2, player_symbol1)

    played_steps = 0
    last_go = []
    main_board1.draw()
    while True:

        # Which player is to play?
        if played_steps % 2 == 0:
            player_symbol = player_symbol1
            # CPU player call
            place_at_rnd = KI_player_move(main_board1, cpu_player1, player_symbol)
            
        else:
            player_symbol = player_symbol2
            # CPU player call
            place_at_rnd = KI_player_move(main_board1, cpu_player2, player_symbol)
            
            # Human player call
            #place_at_rnd = user_input(main_board1.board_size)

        # is chosen collumn valid ?
        valid_move, last_played_position = main_board1.drop_stone(player_symbol, place_at_rnd)
        if valid_move:
            played_steps = played_steps + 1
            # Draw updated board
            main_board1.draw()
            
            #input()

            # Does one player win?
            winning_stones = main_board1.check_win(player_symbol, last_played_position)
            if winning_stones != (False,):

                main_board1.board_state[last_go[-1]] = colorama.Fore.RED + main_board1.board_state[last_go[-1]] + colorama.Fore.RESET
                main_board1.draw_winning_lines(player_symbol, *winning_stones)

                last_go.append(last_played_position)
                print("Stones played       :", played_steps)
                print("Win by players move :", player_symbol, winning_stones, "winning stone: ", last_played_position)
                print("Others player move  :", last_go[-2])
                print("All moves played    :", last_go)

                # recreated all objects
                main_board1 = c4_Board.Board(game_size, player_symbol1, player_symbol2)
                cpu_player1 = c4_KIPlayer.KIPlayer(main_board1, player_symbol1, player_symbol2)
                cpu_player2 = c4_KIPlayer.KIPlayer(main_board1, player_symbol2, player_symbol1)
                played_steps = 0
                last_go = []
                input("press to restart!!")
                continue

            last_go.append(last_played_position)
            print(f"Stones played: {played_steps}")

            # Full board?
            boardfull = 0
            for i in range(game_size):
                if main_board1.board_state[i] != " ":
                    boardfull += 1

        if (played_steps == game_size * game_size) or boardfull == game_size:
            break

    # End of game loop
    print("Took", played_steps, "turns, last turn was at collumn", place_at_rnd)

##################################################### CALL MAIN FUNCTION #############################################
if __name__ == "__main__":
    main()
