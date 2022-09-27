''' Board class file'''
import time
import os
import colorama

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
        """ Method to draw the board """
        os.system("clear")
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
        print("  -", end = "")
        for row in range(self.board_size):
            print(str(row)[-1], end = "")
        print("-")


    def draw_winning_lines(self, symbol, stone1, stone2, stone3, stone4):
        ''' draw helper lines for debugging '''
        backup_list = self.board_state[:]
        self.board_state[stone1] = colorama.Fore.GREEN + symbol + colorama.Fore.RESET
        self.board_state[stone2] = colorama.Fore.GREEN + symbol + colorama.Fore.RESET
        self.board_state[stone3] = colorama.Fore.GREEN + symbol + colorama.Fore.RESET
        self.board_state[stone4] = colorama.Fore.GREEN + symbol + colorama.Fore.RESET
        self.draw()
        time.sleep(.1)
        self.board_state = backup_list[:]


    def drop_stone(self, player_symbol, collumn: int):
        """drop a stone of a player check if move is valide place stone"""
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
        show_line = "----" # DDVH flag to show debug lines!

        if self.board_state[index] == player_symbol:
            # diagonal left -> right \ up -> down 
            for i in range(4):
                # calculate stones 4 stones
                root_row = index // self.board_size               
                stone1 = index - (3 - i) - (self.board_size * 3) + (i * self.board_size)
                stone2 = index - (2 - i) - (self.board_size * 2) + (i * self.board_size)
                stone3 = index - (1 - i) - (self.board_size * 1) + (i * self.board_size)
                stone4 = index - (0 - i) - (self.board_size * 0) + (i * self.board_size)
                # check intersection
                if stone1 < ((root_row - (3-i))*self.board_size) or stone1 < 0: continue
                if stone1 > (self.board_size-1) + (root_row - (3-i))*self.board_size or stone1 > (self.board_size*self.board_size)-1: continue
                if stone2 < ((root_row - (2-i))*self.board_size) or stone1 < 0: continue
                if stone2 > (self.board_size-1) + (root_row - (2-i))*self.board_size or stone2 > (self.board_size*self.board_size)-1: continue
                if stone3 < ((root_row - (1-i))*self.board_size) or stone1 < 0: continue
                if stone3 > (self.board_size-1) + (root_row - (1-i))*self.board_size or stone3 > (self.board_size*self.board_size)-1: continue
                if stone4 < ((root_row - (0-i))*self.board_size) or stone1 < 0: continue
                if stone4 > ((self.board_size-1) + (root_row - (0-i))*self.board_size) or stone4 > (self.board_size*self.board_size)-1: continue
                # draw helper lines (debug)
                if show_line[0] == "D":
                    self.draw_winning_lines(
                        self.board_state[index], stone1, stone2, stone3, stone4
                    )
                # return stones if 4-in-a-row!
                if (
                    self.board_state[stone1] == player_symbol
                    and self.board_state[stone2] == player_symbol
                    and self.board_state[stone3] == player_symbol
                    and self.board_state[stone4] == player_symbol
                ):
                    return (stone1, stone2, stone3, stone4)

            # diagonal right -> left / up -> down
            for i in range(4):
                # calculate stones 4 stones
                root_row = index // self.board_size
                stone1 = index + (3 - i) - (self.board_size * 3) + (i * self.board_size)
                stone2 = index + (2 - i) - (self.board_size * 2) + (i * self.board_size)
                stone3 = index + (1 - i) - (self.board_size * 1) + (i * self.board_size)
                stone4 = index + (0 - i) - (self.board_size * 0) + (i * self.board_size)
                # check intersection
                if stone1 < ((root_row - (3-i))*self.board_size) or stone1 < 0: continue
                if stone1 > (self.board_size-1) + (root_row - (3-i))*self.board_size or stone1 > (self.board_size*self.board_size)-1: continue
                if stone2 < ((root_row - (2-i))*self.board_size) or stone1 < 0: continue
                if stone2 > (self.board_size-1) + (root_row - (2-i))*self.board_size or stone2 > (self.board_size*self.board_size)-1: continue
                if stone3 < ((root_row - (1-i))*self.board_size) or stone1 < 0: continue
                if stone3 > (self.board_size-1) + (root_row - (1-i))*self.board_size or stone3 > (self.board_size*self.board_size)-1: continue
                if stone4 < ((root_row - (0-i))*self.board_size) or stone1 < 0: continue
                if stone4 > ((self.board_size-1) + (root_row - (0-i))*self.board_size) or stone4 > (self.board_size*self.board_size)-1: continue
                # draw helper lines (debug)
                if show_line[1] == "D":
                    self.draw_winning_lines(
                        self.board_state[index], stone1, stone2, stone3, stone4
                    )
                # return stones if 4-in-a-row!
                if (
                    self.board_state[stone1] == player_symbol
                    and self.board_state[stone2] == player_symbol
                    and self.board_state[stone3] == player_symbol
                    and self.board_state[stone4] == player_symbol
                ):
                    return (stone1, stone2, stone3, stone4)

            # vertical
            for i in range(4):
                # calculate stones 4 stones
                root_row = (index - ((index // self.board_size) * self.board_size))+1
                root_collomn = index // self.board_size
                max_index = index + ((self.board_size-1-root_collomn)*self.board_size)
                stone1 = ((index - (i * self.board_size)) + self.board_size*0)
                stone2 = ((index - (i * self.board_size)) + self.board_size*1)
                stone3 = ((index - (i * self.board_size)) + self.board_size*2)
                stone4 = ((index - (i * self.board_size)) + self.board_size*3)
                # check intersection
                if stone1 < 0 or stone2 < 0 or stone3 < 0 or stone4 < 0: continue
                if stone1 > max_index or stone2 > max_index or stone3 > max_index or stone4 > max_index: continue
                # draw helper lines (debug)
                if show_line[2] == "V":
                    self.draw_winning_lines(
                        self.board_state[index], stone1, stone2, stone3, stone4
                    )
                # return stones if 4-in-a-row!
                if (
                    self.board_state[stone1] == player_symbol
                    and self.board_state[stone2] == player_symbol
                    and self.board_state[stone3] == player_symbol
                    and self.board_state[stone4] == player_symbol
                ):
                    return (stone1, stone2, stone3, stone4)

            # Horizontal
            for i in range(4):
                # calculate stones 4 stones
                stone1 = index - (3 - i)
                stone2 = index - (2 - i)
                stone3 = index - (1 - i)
                stone4 = index - (0 - i)
                # check intersection
                if stone1 < ((index // self.board_size) * self.board_size): continue
                if stone1 > ((index // self.board_size) * self.board_size) + self.board_size - 1: break
                if stone2 < ((index // self.board_size) * self.board_size): continue
                if stone2 > ((index // self.board_size) * self.board_size) + self.board_size - 1: break
                if stone3 < ((index // self.board_size) * self.board_size): continue
                if stone3 > ((index // self.board_size) * self.board_size) + self.board_size - 1: break
                if stone4 < ((index // self.board_size) * self.board_size): continue
                if stone4 > ((index // self.board_size) * self.board_size) + self.board_size - 1: break
                # draw helper lines (debug)
                if show_line[3] == "H":
                    self.draw_winning_lines(
                        self.board_state[index], stone1, stone2, stone3, stone4
                    )
                # return stones if 4-in-a-row!
                if (
                    self.board_state[stone1] == player_symbol
                    and self.board_state[stone2] == player_symbol
                    and self.board_state[stone3] == player_symbol
                    and self.board_state[stone4] == player_symbol
                ):
                    return (stone1, stone2, stone3, stone4)
        # return failure!
        return (False,)
