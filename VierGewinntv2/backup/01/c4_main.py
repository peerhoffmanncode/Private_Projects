import random
import time
import os
import colorama
import c4_Board as c4_Board
import c4_KIPlayer as c4_KIPlayer

def user_input(board_size: int) -> int:
    ''' function to get user input/ move '''
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

def KI_player_move(board: c4_Board.Board, KIplayer: c4_KIPlayer.KIPlayer, player_symbol: str) -> int:
    ''' function to get KI Player move '''
    print (f"[{player_symbol}] players turn") # for debug!
    #/--/ init list of possible moves
    options_to_choosefrom = []
    if player_symbol == board.player_symbol1:
        enemy_symbol = board.player_symbol2
    if player_symbol == board.player_symbol2:
        enemy_symbol = board.player_symbol1

    #/--/ check if KI player can win with next move?
    pl_win = KIplayer.check_player_win(player_symbol)
    #/--/ check if enemy player can win with next move?
    en_win = KIplayer.check_player_win(enemy_symbol)
    #en_win = KIplayer.check_enemy_win()
    
    if pl_win != -1:
        column_to_place_stone = pl_win
        print(f"player {player_symbol} can win! KI Should place stone @ {column_to_place_stone}") # for debug!
    elif en_win != -1:
        column_to_place_stone = en_win
        print(f"prohibit enemy players win! KI Should place stone @ {column_to_place_stone}") # for debug!
    else:
        #/--/ check if enemy player could win after KI player place a stone!
        options_to_choosefrom = KIplayer.play_one_turn_ahead()
        print(f"|play_one_turn_ahead| -> left options to choose from {options_to_choosefrom}") # for debug!
        #/--/ check if player could win with the next two stones!
        #options_to_choosefrom = (0,1)
        options_to_choosefrom = KIplayer.play_best_option(options_to_choosefrom)
        
        column_to_place_stone = random.choice(options_to_choosefrom) # options_to_choosefrom[0]
        print(f"|play_best_option|    -> left options to choose from {options_to_choosefrom}") # for debug!
        
        
        
        # if len(options_to_choosefrom) == board.board_size:
        #     # fields restricted
        #     column_to_place_stone = None
        #     for find_column in range(((board.board_size//2)+1)):
        #         if column_to_place_stone != None:
        #             break
        #         for directional_switch in range(-1,2,2):
        #             pick_columnen = (board.board_size*board.board_size)-1-((board.board_size)//2)+(find_column * directional_switch)
        #             if board.board_state[pick_columnen] != board.player_symbol1 and board.board_state[pick_columnen] != board.player_symbol2:
        #                 column_to_place_stone = board.board_size-((board.board_size*board.board_size) - pick_columnen)
        #                 break
        #     if column_to_place_stone == None:
        #         column_to_place_stone = random.randint(0, board.board_size-1)
        #         print("KI will chose from random object") # for debug!
        #     else:
        #         print(f"KI will chose from first played stones!!") # for debug!
        # elif len(options_to_choosefrom) > 0:
        #     print(f"KI will chose from this list => {options_to_choosefrom}") # for debug!
        #     column_to_place_stone = random.choice(options_to_choosefrom)
        # else:
        #     # can use any field!
        #     print("KI will chose from random object") # for debug!
        #     column_to_place_stone = random.randint(0, board.board_size-1)

    input(f"final KI decision >>{column_to_place_stone}<< press enter to continue...")
    return column_to_place_stone

##################################################### MAIN FUNCTION #############################################
def main():
    """ This is the main function :-) """
    # board size?
    game_size = 7
    # rounds played?
    played_steps = 0
    # list of all stones played
    all_played_moves = []
    # Player symbols
    player_symbol1 = "0"
    player_symbol2 = "O"
    # create board and KI Player objects
    main_board1 = c4_Board.Board(game_size, player_symbol1, player_symbol2)
    cpu_player1 = c4_KIPlayer.KIPlayer(main_board1, player_symbol1, player_symbol2)
    cpu_player2 = c4_KIPlayer.KIPlayer(main_board1, player_symbol2, player_symbol1)

    # draw empty board
    main_board1.draw()
    # main game loop
    while True:
        # Which player is to play?
        if played_steps % 2 == 0:
            player_symbol = player_symbol1
            # CPU player call
            column_to_place_a_stone = KI_player_move(main_board1, cpu_player1, player_symbol)
        else:
            player_symbol = player_symbol2
            # CPU player call
            column_to_place_a_stone = KI_player_move(main_board1, cpu_player2, player_symbol)
            # Human player call
            #place_at_rnd = user_input(main_board1.board_size)

        # drop stone if chosen move is valid ?
        valid_move, last_played_position = main_board1.drop_stone(player_symbol, column_to_place_a_stone)
        if valid_move:
            # add a played step
            played_steps = played_steps + 1
            all_played_moves.append(last_played_position)
            print(f"Stones played: {played_steps}")
            
            # Draw updated board
            main_board1.draw()
            
            # Does one player win?
            winning_stones = main_board1.check_win(player_symbol, last_played_position)
            if winning_stones != (False,):
                
                # last stone of looser marked as RED
                main_board1.board_state[all_played_moves[-2]] = colorama.Fore.RED + main_board1.board_state[all_played_moves[-2]] + colorama.Fore.RESET
                # update board drawing to show red stone!
                main_board1.draw()
                # update board drawing to show winning stones
                main_board1.draw_winning_lines(player_symbol, *winning_stones)

                print("Stones played       :", played_steps)
                print("Win by players move :", player_symbol, winning_stones, "winning stone: ", last_played_position)
                print("Others player move  :", all_played_moves[-2])
                print("All moves played    :", all_played_moves)

                # game restart ! -> init all objects again!
                main_board1 = c4_Board.Board(game_size, player_symbol1, player_symbol2)
                cpu_player1 = c4_KIPlayer.KIPlayer(main_board1, player_symbol1, player_symbol2)
                cpu_player2 = c4_KIPlayer.KIPlayer(main_board1, player_symbol2, player_symbol1)
                played_steps = 0
                all_played_moves = []
                input("press to restart!!")
                continue

        # is the board full board?
        boardfull = 0
        for i in range(game_size):
            if main_board1.board_state[i] != " ":
                boardfull += 1
        # end game if -> board full or all stones are played!
        if (played_steps == game_size * game_size) or boardfull == game_size:
            break

    # End of game loop
    print(f"Took {played_steps} turns, last turn was at column {column_to_place_a_stone}")

##################################################### CALL MAIN FUNCTION #############################################
if __name__ == "__main__":
    main()
