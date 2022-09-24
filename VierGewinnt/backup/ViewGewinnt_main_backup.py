import random
import time
import os
import colorama
import copy


class Board:
    """Main board class"""

    def __init__(self, board_size: int, player_symbol1: str, player_symbol2: str):
        """Initialize the board"""
        self.empty_space = " "
        self.board_size = board_size
        self.board_state = list(self.empty_space * self.board_size * self.board_size)
        self.player_symbol1 = player_symbol1
        self.player_symbol2 = player_symbol2

    def draw(self):
        os.system("clear")
        """ Draw the board """
        print("  /" + ("-" * self.board_size) + "\\")
        count = 0
        for row in range(self.board_size):
            print(f"{row:2}|", end="")
            for collumn in range(self.board_size):
                if self.player_symbol1 == self.board_state[count]:
                    print(
                        colorama.Fore.CYAN
                        + self.board_state[count]
                        + colorama.Fore.RESET,
                        end="",
                    )
                else:
                    print(
                        colorama.Fore.YELLOW
                        + self.board_state[count]
                        + colorama.Fore.RESET,
                        end="",
                    )
                count = count + 1
            print("|")
        print("  \\" + ("-" * self.board_size) + "/")
        
        
    def draw_winning_lines(self, symbol, stone1, stone2, stone3, stone4):
        backup_list = self.board_state[:]

        self.board_state[stone1] = colorama.Fore.RED + symbol + colorama.Fore.RESET
        self.board_state[stone2] = colorama.Fore.RED + symbol + colorama.Fore.RESET
        self.board_state[stone3] = colorama.Fore.RED + symbol + colorama.Fore.RESET
        self.board_state[stone4] = colorama.Fore.RED + symbol + colorama.Fore.RESET
        self.draw()
        #time.sleep(.05)
        self.board_state = backup_list[:]


    def drop_stone(self, player_symbol, collumn: int):
        """drop a stone of a player
        check if move is valide
        place stone"""
        safed_last_empty = -1
        for i in range(collumn, self.board_size * self.board_size, self.board_size):
            if self.board_state[i] == self.empty_space:
                safed_last_empty = i

        if safed_last_empty != -1:
            self.board_state[safed_last_empty] = player_symbol
            return True, safed_last_empty
        return False, safed_last_empty
    

    def check_win(self, player_symbol, index) -> tuple:
        """check if a player is winning"""

        if self.board_state[index] == player_symbol:
            
            # diagonal right -> left / up -> down
            for i in range(4):
                root_row = index // self.board_size
                stone1 = index + (3 - i) - (self.board_size * 3) + (i * self.board_size)
                stone2 = index + (2 - i) - (self.board_size * 2) + (i * self.board_size)
                stone3 = index + (1 - i) - (self.board_size * 1) + (i * self.board_size)
                stone4 = index + (0 - i) - (self.board_size * 0) + (i * self.board_size)
                                           
                if stone1 < ((root_row - (3-i))*self.board_size) or stone1 < 0: continue
                if stone1 > (self.board_size-1) + (root_row - (3-i))*self.board_size or stone1 > (self.board_size*self.board_size)-1: continue
                if stone2 < ((root_row - (2-i))*self.board_size) or stone1 < 0: continue
                if stone2 > (self.board_size-1) + (root_row - (2-i))*self.board_size or stone2 > (self.board_size*self.board_size)-1: continue
                if stone3 < ((root_row - (1-i))*self.board_size) or stone1 < 0: continue
                if stone3 > (self.board_size-1) + (root_row - (1-i))*self.board_size or stone3 > (self.board_size*self.board_size)-1: continue
                if stone4 < ((root_row - (0-i))*self.board_size) or stone1 < 0: continue
                if stone4 > ((self.board_size-1) + (root_row - (0-i))*self.board_size) or stone4 > (self.board_size*self.board_size)-1: continue

                if (
                    self.board_state[stone1] == player_symbol
                    and self.board_state[stone2] == player_symbol
                    and self.board_state[stone3] == player_symbol
                    and self.board_state[stone4] == player_symbol
                ):
                    return (stone1, stone2, stone3, stone4)
                
                # self.draw_winning_lines(
                #     self.board_state[index], stone1, stone2, stone3, stone4
                # )
            
            # diagonal left -> right \ up -> down 
            for i in range(4):
                root_row = index // self.board_size               
                stone1 = index - (3 - i) - (self.board_size * 3) + (i * self.board_size)
                stone2 = index - (2 - i) - (self.board_size * 2) + (i * self.board_size)
                stone3 = index - (1 - i) - (self.board_size * 1) + (i * self.board_size)
                stone4 = index - (0 - i) - (self.board_size * 0) + (i * self.board_size)

                if stone1 < ((root_row - (3-i))*self.board_size) or stone1 < 0: continue
                if stone1 > (self.board_size-1) + (root_row - (3-i))*self.board_size or stone1 > (self.board_size*self.board_size)-1: continue
                if stone2 < ((root_row - (2-i))*self.board_size) or stone1 < 0: continue
                if stone2 > (self.board_size-1) + (root_row - (2-i))*self.board_size or stone2 > (self.board_size*self.board_size)-1: continue
                if stone3 < ((root_row - (1-i))*self.board_size) or stone1 < 0: continue
                if stone3 > (self.board_size-1) + (root_row - (1-i))*self.board_size or stone3 > (self.board_size*self.board_size)-1: continue
                if stone4 < ((root_row - (0-i))*self.board_size) or stone1 < 0: continue
                if stone4 > ((self.board_size-1) + (root_row - (0-i))*self.board_size) or stone4 > (self.board_size*self.board_size)-1: continue
                
                if (
                    self.board_state[stone1] == player_symbol
                    and self.board_state[stone2] == player_symbol
                    and self.board_state[stone3] == player_symbol
                    and self.board_state[stone4] == player_symbol
                ):
                    return (stone1, stone2, stone3, stone4)
                
                # self.draw_winning_lines(
                #     self.board_state[index], stone1, stone2, stone3, stone4
                # )
                
            # Horizontal
            for i in range(self.board_size - 3):
                stone1 = index - (3 - i)
                stone2 = index - (2 - i)
                stone3 = index - (1 - i)
                stone3 = index - (0 - i)
                
                if stone1 < ((index // self.board_size) * self.board_size):
                    continue
                    stone1 = (index // self.board_size) * self.board_size
                if (stone1 > ((index // self.board_size) * self.board_size) + self.board_size - 1): 
                    continue
                    
                
                if stone2 < ((index // self.board_size) * self.board_size):
                    continue
                    stone2 = (index // self.board_size) * self.board_size
                if (
                    stone2
                    > ((index // self.board_size) * self.board_size)
                    + self.board_size
                    - 1
                ): continue
                    # stone2 = (
                    #     ((index // self.board_size) * self.board_size)
                    #     + self.board_size
                    #     - 1
                    # )
                
                if stone3 < ((index // self.board_size) * self.board_size):
                    continue
                    stone3 = (index // self.board_size) * self.board_size
                if (
                    stone3
                    > ((index // self.board_size) * self.board_size)
                    + self.board_size
                    - 1
                ): continue
                    # stone3 = (
                    #     ((index // self.board_size) * self.board_size)
                    #     + self.board_size
                    #     - 1
                    # )
               
                if stone4 < ((index // self.board_size) * self.board_size):
                    continue
                    stone4 = (index // self.board_size) * self.board_size
                if (
                    stone4
                    > ((index // self.board_size) * self.board_size)
                    + self.board_size
                    - 1
                ): continue
                    # stone4 = (
                    #     ((index // self.board_size) * self.board_size)
                    #     + self.board_size
                    #     - 1
                    # )

                if (
                     self.board_state[stone1] == player_symbol
                    and self.board_state[stone2] == player_symbol
                    and self.board_state[stone3] == player_symbol
                    and self.board_state[stone4] == player_symbol
                ):
                    return (stone1, stone2, stone3, stone4)

                self.draw_winning_lines(
                    self.board_state[index], stone1, stone2, stone3, stone4
                )

            # vertical
            for i in range(self.board_size - 3):
                stone1 = (index - (index // self.board_size) * self.board_size) + (
                    i * self.board_size
                )
                stone2 = (index - (index // self.board_size) * self.board_size) + (
                    (i + 1) * self.board_size
                )
                stone3 = (index - (index // self.board_size) * self.board_size) + (
                    (i + 2) * self.board_size
                )
                stone4 = (index - (index // self.board_size) * self.board_size) + (
                    (i + 3) * self.board_size
                )
                if (
                    (stone4 - stone1 == self.board_size * 3)
                    and self.board_state[stone1] == player_symbol
                    and self.board_state[stone2] == player_symbol
                    and self.board_state[stone3] == player_symbol
                    and self.board_state[stone4] == player_symbol
                ):
                    return (stone1, stone2, stone3, stone4)

                # self.draw_winning_lines(
                #     self.board_state[index], stone1, stone2, stone3, stone4
                # )
        return (False,)

class KIPlayer:
    """KI Player class"""
    def __init__(self, board_to_play: Board, player_symbol: str, enemy_symbol: str):
        self.current_board = board_to_play
        self.player_symbol = player_symbol
        self.enemy_symbol = enemy_symbol
        
    def check_player_win(self):
        temp_board = copy.deepcopy(self.current_board)
        for choise in range(temp_board.board_size):
            player_valid_move, player_last_played_position = temp_board.drop_stone(self.player_symbol, choise)
            if player_valid_move:
                player_win_with = temp_board.check_win(self.player_symbol, player_last_played_position)
                if player_win_with != (False,):
                    return choise, player_win_with

            temp_board = copy.deepcopy(self.current_board)
                       
        temp_board = None
        return -1, (False, )
        
    def check_enemy_win(self):
        temp_board = copy.deepcopy(self.current_board)
        for choise in range(temp_board.board_size):
            enemy_valid_move, enemy_last_played_position = temp_board.drop_stone(self.enemy_symbol, choise)
            if enemy_valid_move:
                enemy_win_with = temp_board.check_win(self.enemy_symbol, enemy_last_played_position)
                if enemy_win_with != (False,):
                    return choise, enemy_win_with

            temp_board = copy.deepcopy(self.current_board)
                       
        temp_board = None
        return -1, (False, )



##################################################### MAIN FUNCTION #############################################
def main():
    """This is the main program"""
    played_steps = 0
    game_size = 20
    player_symbol1 = "0"
    player_symbol2 = "O"
    main_board1 = Board(game_size, player_symbol1, player_symbol2)
    cpu_player1 = KIPlayer(main_board1, player_symbol1, player_symbol2)
    cpu_player2 = KIPlayer(main_board1, player_symbol2, player_symbol1)

    while True:
        
        #place_at_rnd = random.randint(0, game_size - 1)
        if played_steps % 2 == 0:
            player_symbol = player_symbol1
        else:
            player_symbol = player_symbol2
        
        if player_symbol == player_symbol1:
            pl_win, pl_winnig_order = cpu_player1.check_player_win()
            en_win, en_winnig_order = cpu_player1.check_enemy_win()
            
            if pl_win != -1:
                place_at_rnd = pl_win
            elif en_win != -1:
                place_at_rnd = en_win
            else:
                place_at_rnd = random.randint(0, game_size - 1)
        else:
            pl_win, pl_winnig_order = cpu_player2.check_player_win()
            en_win, en_winnig_order = cpu_player2.check_enemy_win()
            
            if pl_win != -1:
                place_at_rnd = pl_win
            elif en_win != -1:
                place_at_rnd = en_win
            else:
                place_at_rnd = random.randint(0, game_size - 1)

        valid_move, last_played_position = main_board1.drop_stone(player_symbol, place_at_rnd)  
        if valid_move:
            played_steps = played_steps + 1

        os.system("clear")
        main_board1.draw()
        
        print(f"player {player_symbol1} would win with :{pl_winnig_order}")
        print(f"enemy {player_symbol2} would win with  :{en_winnig_order}")
        
        time.sleep(.6)

        winning_stones = main_board1.check_win(player_symbol, last_played_position)
        if winning_stones != (False,):
            main_board1.draw()
            main_board1.draw_winning_lines(player_symbol, *winning_stones)
            print("Win by player:", player_symbol, winning_stones)
            time.sleep(2)
            main_board1 = Board(game_size, player_symbol1, player_symbol2)
            cpu_player1 = KIPlayer(main_board1, player_symbol1, player_symbol2)
            cpu_player2 = KIPlayer(main_board1, player_symbol2, player_symbol1)
            played_steps = 0

        if played_steps == game_size * game_size:
            break
    print("Took", played_steps, "turns, last turn was at collumn", place_at_rnd)


##################################################### CALL MAIN FUNCTION #############################################
if __name__ == "__main__":
    main()
