import time
import colorama
import c4_Board
import c4_KIPlayer


def user_input(board_size: int) -> int:
    """function to get user input/ move"""
    while True:
        user_choice = input(f"Enter a position [0-{board_size-1}] : ")
        try:
            column_to_place_stone = int(user_choice)
            # validate input
            if 0 <= column_to_place_stone < board_size:
                return column_to_place_stone
            else:
                print("wrong input!")
        except ValueError:
            print("wrong input!")


def KI_player_move(
    board: c4_Board.Board, KIplayer: c4_KIPlayer.KIPlayer, player_symbol: str, main_depth=5) -> int:
    """function to get KI Player move"""
    print(f"[{player_symbol}] players turn, logical depth [{main_depth}] steps")  # for debug!
    column_to_place_stone=KIplayer.KIplayer_do_turn(player_symbol, depth=main_depth)
    print(f"final KI {player_symbol} decision >>{column_to_place_stone}<< press enter to continue...")
    
    return column_to_place_stone


##################################################### MAIN FUNCTION #############################################
def main():
    """This is the main function :-)"""
    # board size?
    game_size = 7
    # rounds played?
    played_steps = 0
    # list of all stones played
    all_played_moves = []
    # Player symbols
    player_symbol1 = "2"
    player_symbol2 = "0"
    # create board and KI Player objects
    main_board1 = c4_Board.Board(game_size, player_symbol1, player_symbol2)
    cpu_player = c4_KIPlayer.KIPlayer(main_board1, player_symbol1, player_symbol2)
    #cpu_player2 = c4_KIPlayer.KIPlayer(main_board1, player_symbol2, player_symbol1)

    # draw empty board
    main_board1.draw()
    # main game loop
    cpu_depth = 5
    while True:
        # Which player is to play?
        if played_steps % 2 == 0:
            player_symbol = player_symbol1
            enemy_symbol = player_symbol2
            # CPU player call
            check = time.time()
            column_to_place_a_stone = KI_player_move(
                main_board1, cpu_player, player_symbol, main_depth=cpu_depth
            )
            if time.time() - check > .5:
                cpu_depth = 5
            else:
                cpu_depth += 1
        else:
            player_symbol = player_symbol2
            enemy_symbol = player_symbol1
            # CPU player call
            # check = time.time()
            # column_to_place_a_stone = KI_player_move(
            #     main_board1, cpu_player, player_symbol, main_depth=cpu_depth
            # )
            # if time.time() - check > .5:
            #     cpu_depth = 5
            # else:
            #     cpu_depth += 1
            # Human player call
            column_to_place_a_stone = user_input(main_board1.board_size)
            
        
        #input()
            
        # drop stone if chosen move is valid ?
        valid_move, last_played_position = main_board1.drop_stone(
            player_symbol, column_to_place_a_stone
        )
        if valid_move:
             # add a played step
            played_steps = played_steps + 1
            all_played_moves.append(last_played_position)
            print(f"Stones played: {played_steps}")

            # Draw updated board
            main_board1.draw()

            # Does one player win?
            winning_stones = main_board1.check_win(player_symbol, enemy_symbol)
            if winning_stones[0] != -1 and winning_stones[0] != 1:

                # last stone of looser marked as RED
                main_board1.board_state[all_played_moves[-2][0]][all_played_moves[-2][1]] = (
                    colorama.Fore.RED
                    + main_board1.board_state[all_played_moves[-2][0]][all_played_moves[-2][1]]
                    + colorama.Fore.RESET
                )
                # update board drawing to show red stone!
                main_board1.draw()
                # update board drawing to show winning stones
                main_board1.draw_winning_lines(*winning_stones)

                print("Stones played       :", played_steps)
                print(
                    "Win by players move :",
                    player_symbol,
                    winning_stones,
                    "winning stone: ",
                    last_played_position,
                )
                print("Others player move  :", all_played_moves[-2])
                print("All moves played    :", all_played_moves)

                # game restart ! -> init all objects again!
                main_board1 = c4_Board.Board(game_size, player_symbol1, player_symbol2)
                played_steps = 0
                all_played_moves = []
                input("press to restart!!")
                continue


        # is the board full board?
        board_full = 0
        for i in range(game_size):
            if main_board1.board_state[0][i] != main_board1.empty_space:
                board_full += 1
        # end game if -> board full or all stones are played!
        if (played_steps == game_size * game_size) or board_full == game_size:
            break

    # End of game loop
    print(
        f"Took {played_steps} turns, last turn was at column {column_to_place_a_stone}"
    )


##################################################### CALL MAIN FUNCTION #############################################
if __name__ == "__main__":
    main()
