import random
import time
import os
import colorama

import c4_Board as c4_Board
import c4_KIPlayer as c4_KIPlayer

##################################################### MAIN FUNCTION #############################################
def main():
    """This is the main program"""
    played_steps = 0
    game_size = 7
    last_go = -1
    player_symbol1 = "0"
    player_symbol2 = "O"
    # create all objects
    main_board1 = c4_Board.Board(game_size, player_symbol1, player_symbol2)
    cpu_player1 = c4_KIPlayer.KIPlayer(main_board1, player_symbol1, player_symbol2)
    cpu_player2 = c4_KIPlayer.KIPlayer(main_board1, player_symbol2, player_symbol1)
    
    # valid_move, last_played_position = main_board1.drop_stone(player_symbol2, 0)
    # valid_move, last_played_position = main_board1.drop_stone(player_symbol2, 0)
    # valid_move, last_played_position = main_board1.drop_stone(player_symbol2, 0)
    # valid_move, last_played_position = main_board1.drop_stone(player_symbol1, 0)
    # valid_move, last_played_position = main_board1.drop_stone(player_symbol2, 1)
    # valid_move, last_played_position = main_board1.drop_stone(player_symbol2, 1)
    # valid_move, last_played_position = main_board1.drop_stone(player_symbol1, 1)
    # valid_move, last_played_position = main_board1.drop_stone(player_symbol2, 2)

    while True:
        
        # Which player is to play?
        if played_steps % 2 == 0:
            player_symbol = player_symbol1
            
            # Cpu Player
            pl_win, pl_winnig_order = cpu_player1.check_player_win()
            en_win, en_winnig_order = cpu_player1.check_enemy_win()
            if pl_win != -1:
                place_at_rnd = pl_win
            elif en_win != -1:
                place_at_rnd = en_win
            else:
                win, pl_winnig_order = cpu_player1.played_ahead_turn()
                if win != -1:
                    place_at_rnd = win
                    print ("player1 choice: ", place_at_rnd)
                else:
                    place_at_rnd = random.randint(0, game_size - 1)
                    print ("player1 random choice: ", place_at_rnd)
        else:
            player_symbol = player_symbol2
            
            # Cpu Player
            pl_win, pl_winnig_order = cpu_player2.check_player_win()
            en_win, en_winnig_order = cpu_player2.check_enemy_win()
            if pl_win != -1:
                place_at_rnd = pl_win
            elif en_win != -1:
                place_at_rnd = en_win
            else:
                win, pl_winnig_order = cpu_player2.played_ahead_turn()
                if win != -1:
                    place_at_rnd = win
                    print ("player1 choice: ", place_at_rnd)
                else:
                    place_at_rnd = random.randint(0, game_size - 1)
                    print ("player2 random choice: ", place_at_rnd)

        # calculated player status
        # if player_symbol == player_symbol1:
        #     print(f"player {player_symbol1} would win with :{pl_winnig_order} choose {pl_win} to play")
        #     print(f"enemy {player_symbol2} would win with  :{en_winnig_order} choose {en_win} to play")
        #     print(f"Player {player_symbol} will drop stone at: {place_at_rnd}")
        # else:
        #     print(f"player {player_symbol2} would win with :{pl_winnig_order} choose {pl_win} to play")
        #     print(f"enemy {player_symbol1} would win with  :{en_winnig_order} choose {en_win} to play")
        #     print(f"Player {player_symbol} will drop stone at: {place_at_rnd}")
            
        
        #time.sleep(0.6)
        #input()
        
        # is chosen collumn valid ?
        valid_move, last_played_position = main_board1.drop_stone(player_symbol, place_at_rnd)
        if valid_move:
            played_steps = played_steps + 1
            # Draw updated board
            main_board1.draw()
        
        # Does one player win?
        winning_stones = main_board1.check_win(player_symbol, last_played_position)
        if winning_stones != (False,):
            main_board1.draw()
            
            main_board1.board_state[last_go] = colorama.Fore.RED + main_board1.board_state[last_go] + colorama.Fore.RESET
            
            main_board1.draw_winning_lines(player_symbol, *winning_stones)
            print("Win by players move :", player_symbol, winning_stones, "wining stone: ", last_played_position)
            print("Others player move  :", last_go)

            # recreated all objects
            main_board1 = c4_Board.Board(game_size, player_symbol1, player_symbol2)
            cpu_player1 = c4_KIPlayer.KIPlayer(main_board1, player_symbol1, player_symbol2)
            cpu_player2 = c4_KIPlayer.KIPlayer(main_board1, player_symbol2, player_symbol1)
            played_steps = 0
            input("press to restart!!")
        
        last_go = last_played_position
        print(f"Stones player: {played_steps}")
        
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
