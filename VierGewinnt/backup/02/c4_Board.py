""" Board class file"""
import time
import os
from tkinter import S
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
        
        ### 7x7 static (to be implemented)
        self.lookup_table = [0.03, 0.04, 0.05, 0.07, 0.05, 0.04, 0.03,
                             0.04, 0.06, 0.08, 0.10, 0.08, 0.06, 0.04,
                             0.05, 0.08, 0.11, 0.13, 0.11, 0.08, 0.05,
                             0.07, 0.10, 0.13, 0.15, 0.13, 0.10, 0.07,
                             0.05, 0.08, 0.11, 0.13, 0.11, 0.08, 0.05,
                             0.04, 0.06, 0.08, 0.10, 0.08, 0.06, 0.04,
                             0.03, 0.04, 0.05, 0.07, 0.05, 0.04, 0.03]

    def draw(self):
        """Method to draw the board"""
        os.system("clear")
        print("  /" + ("-" * self.board_size) + "\\")
        count = 0
        for row in range(self.board_size):
            print(f"{row:2}|", end="")
            for column in range(self.board_size):
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
        print("  -", end="")
        for row in range(self.board_size):
            print(str(row)[-1], end="")
        print("-")

    def draw_winning_lines(self, symbol, stone1, stone2, stone3, stone4):
        """draw helper lines for debugging"""
        backup_list = self.board_state[:]
        if stone1:
            self.board_state[stone1] = (
                colorama.Fore.GREEN + symbol + colorama.Fore.RESET
            )
        if stone2:
            self.board_state[stone2] = (
                colorama.Fore.GREEN + symbol + colorama.Fore.RESET
            )
        if stone3:
            self.board_state[stone3] = (
                colorama.Fore.GREEN + symbol + colorama.Fore.RESET
            )
        if stone4:
            self.board_state[stone4] = (
                colorama.Fore.GREEN + symbol + colorama.Fore.RESET
            )
        self.draw()
        time.sleep(0.05)
        self.board_state = backup_list[:]

    def drop_stone(self, player_symbol, column: int):
        """drop a stone of a player check if move is valid place stone"""
        safed_last_empty = -1
        for i in range(column, self.board_size * self.board_size, self.board_size):
            if self.board_state[i] == self.empty_space:
                safed_last_empty = i

        if safed_last_empty != -1:
            self.board_state[safed_last_empty] = player_symbol
            return True, safed_last_empty
        return False, safed_last_empty
    
    def remove_stone(self, column: int):
        """remove a stone of a player """
        for i in range(column, self.board_size * self.board_size, self.board_size):
            if self.board_state[i] != self.empty_space:
                self.board_state[i] = self.empty_space
                break

    def check_win(self, player_symbol: str, index, check_for_x_in_a_row: int) -> tuple:
        """check if a player is winning"""
        show_line = "----"  # DDVH flag to show debug lines!
        stone_list = [None, None, None, None]

        #if self.board_state[index] == player_symbol:
        if index == -1:
            from_start = 0
            to_end = self.board_size * self.board_size
        else:
            from_start = index
            to_end = index+1
        for index in range(from_start, to_end):
            # diagonal left -> right \ up -> down
            for i in range(check_for_x_in_a_row):
                # calculate stones 4 stones
                root_row = index // self.board_size

                if check_for_x_in_a_row > 3:
                    stone_list[3] = (
                        index - (3 - i) - (self.board_size * 3) + (i * self.board_size))
                    if (
                        stone_list[3] < ((root_row - (3 - i)) * self.board_size)
                        or stone_list[3] < 0):
                        continue
                    if (
                        stone_list[3]
                        > (self.board_size - 1) + (root_row - (3 - i)) * self.board_size
                        or stone_list[3] > (self.board_size * self.board_size) - 1):
                        continue
                if check_for_x_in_a_row > 2:
                    stone_list[2] = (
                        index - (2 - i) - (self.board_size * 2) + (i * self.board_size))
                    if (
                        stone_list[2] < ((root_row - (2 - i)) * self.board_size)
                        or stone_list[2] < 0):
                        continue
                    if (
                        stone_list[2]
                        > (self.board_size - 1) + (root_row - (2 - i)) * self.board_size
                        or stone_list[2] > (self.board_size * self.board_size) - 1):
                        continue
                if check_for_x_in_a_row > 1:
                    stone_list[1] = (
                        index - (1 - i) - (self.board_size * 1) + (i * self.board_size))
                    if (
                        stone_list[1] < ((root_row - (1 - i)) * self.board_size)
                        or stone_list[1] < 0):
                        continue
                    if (
                        stone_list[1]
                        > (self.board_size - 1) + (root_row - (1 - i)) * self.board_size
                        or stone_list[1] > (self.board_size * self.board_size) - 1):
                        continue
                if check_for_x_in_a_row > 0:
                    stone_list[0] = (
                        index - (0 - i) - (self.board_size * 0) + (i * self.board_size))
                    if (
                        stone_list[0] < ((root_row - (0 - i)) * self.board_size)
                        or stone_list[0] < 0):
                        continue
                    if (
                        stone_list[0]
                        > (
                            (self.board_size - 1)
                            + (root_row - (0 - i)) * self.board_size
                        )
                        or stone_list[0] > (self.board_size * self.board_size) - 1):
                        continue
                # draw helper lines (debug)
                if show_line[0] == "D":
                    self.draw_winning_lines(
                        self.board_state[index],
                        stone_list[0],
                        stone_list[1],
                        stone_list[2],
                        stone_list[3],
                    )
                # return stones if X-in-a-row!
                found_stone = []
                for i in range(check_for_x_in_a_row):
                    if self.board_state[stone_list[i]] == player_symbol:
                        found_stone.append(stone_list[i])
                if len(found_stone) >= check_for_x_in_a_row:
                    found_stone.insert(0, player_symbol)
                    return tuple(found_stone)

            # diagonal right -> left / up -> down
            for i in range(check_for_x_in_a_row):
                # calculate stones 4 stones
                root_row = index // self.board_size
                # check intersection
                if check_for_x_in_a_row > 3:
                    stone_list[3] = (
                        index + (3 - i) - (self.board_size * 3) + (i * self.board_size))
                    if (
                        stone_list[3] < ((root_row - (3 - i)) * self.board_size)
                        or stone_list[3] < 0):
                        continue
                    if (
                        stone_list[3]
                        > (self.board_size - 1) + (root_row - (3 - i)) * self.board_size
                        or stone_list[3] > (self.board_size * self.board_size) - 1):
                        continue
                if check_for_x_in_a_row > 2:
                    stone_list[2] = (
                        index + (2 - i) - (self.board_size * 2) + (i * self.board_size))
                    if (
                        stone_list[2] < ((root_row - (2 - i)) * self.board_size)
                        or stone_list[2] < 0):
                        continue
                    if (
                        stone_list[2]
                        > (self.board_size - 1) + (root_row - (2 - i)) * self.board_size
                        or stone_list[2] > (self.board_size * self.board_size) - 1):
                        continue
                if check_for_x_in_a_row > 1:
                    stone_list[1] = (
                        index + (1 - i) - (self.board_size * 1) + (i * self.board_size))
                    if (
                        stone_list[1] < ((root_row - (1 - i)) * self.board_size)
                        or stone_list[1] < 0):
                        continue
                    if (
                        stone_list[1]
                        > (self.board_size - 1) + (root_row - (1 - i)) * self.board_size
                        or stone_list[1] > (self.board_size * self.board_size) - 1):
                        continue
                if check_for_x_in_a_row > 0:
                    stone_list[0] = (
                        index + (0 - i) - (self.board_size * 0) + (i * self.board_size))
                    if (
                        stone_list[0] < ((root_row - (0 - i)) * self.board_size)
                        or stone_list[0] < 0):
                        continue
                    if (
                        stone_list[0]
                        > (
                            (self.board_size - 1)
                            + (root_row - (0 - i)) * self.board_size
                        )
                        or stone_list[0] > (self.board_size * self.board_size) - 1):
                        continue
                # draw helper lines (debug)
                if show_line[1] == "D":
                    self.draw_winning_lines(
                        self.board_state[index],
                        stone_list[0],
                        stone_list[1],
                        stone_list[2],
                        stone_list[3],
                    )
                found_stone = []
                for i in range(check_for_x_in_a_row):
                    if self.board_state[stone_list[i]] == player_symbol:
                        found_stone.append(stone_list[i])
                if len(found_stone) >= check_for_x_in_a_row:
                    found_stone.insert(0, player_symbol)
                    return tuple(found_stone)

            # Vertical
            for i in range(check_for_x_in_a_row):
                # calculate stones 4 stones
                root_row = (index - ((index // self.board_size) * self.board_size)) + 1
                root_collomn = index // self.board_size
                max_index = index + (
                    (self.board_size - 1 - root_collomn) * self.board_size
                )
                if check_for_x_in_a_row > 0:
                    stone_list[0] = (
                        index - (i * self.board_size)
                    ) + self.board_size * 0
                if check_for_x_in_a_row > 1:
                    stone_list[1] = (
                        index - (i * self.board_size)
                    ) + self.board_size * 1
                if check_for_x_in_a_row > 2:
                    stone_list[2] = (
                        index - (i * self.board_size)
                    ) + self.board_size * 2
                if check_for_x_in_a_row > 3:
                    stone_list[3] = (
                        index - (i * self.board_size)
                    ) + self.board_size * 3
                # check intersection
                if stone_list[0]:
                    if stone_list[0] < 0 or stone_list[0] > max_index:
                        continue
                if stone_list[1]:
                    if stone_list[1] < 0 or stone_list[1] > max_index:
                        continue
                if stone_list[2]:
                    if stone_list[2] < 0 or stone_list[2] > max_index:
                        continue
                if stone_list[3]:
                    if stone_list[3] < 0 or stone_list[3] > max_index:
                        continue
                # draw helper lines (debug)
                if show_line[2] == "V":
                    self.draw_winning_lines(
                        self.board_state[index],
                        stone_list[0],
                        stone_list[1],
                        stone_list[2],
                        stone_list[3],
                    )
                found_stone = []
                for i in range(check_for_x_in_a_row):
                    if self.board_state[stone_list[i]] == player_symbol:
                        found_stone.append(stone_list[i])
                if len(found_stone) >= check_for_x_in_a_row:
                    found_stone.insert(0, player_symbol)
                    return tuple(found_stone)

            # Horizontal
            for i in range(check_for_x_in_a_row):
                # calculate stones 4 stones
                # check intersection
                if check_for_x_in_a_row > 3:
                    stone_list[3] = index - (3 - i)
                    if stone_list[3] < ((index // self.board_size) * self.board_size):
                        continue
                    if (
                        stone_list[3]
                        > ((index // self.board_size) * self.board_size)
                        + self.board_size
                        - 1):
                        break
                if check_for_x_in_a_row > 2:
                    stone_list[2] = index - (2 - i)
                    if stone_list[2] < ((index // self.board_size) * self.board_size):
                        continue
                    if (
                        stone_list[2]
                        > ((index // self.board_size) * self.board_size)
                        + self.board_size
                        - 1):
                        break
                if check_for_x_in_a_row > 1:
                    stone_list[1] = index - (1 - i)
                    if stone_list[1] < ((index // self.board_size) * self.board_size):
                        continue
                    if (
                        stone_list[1]
                        > ((index // self.board_size) * self.board_size)
                        + self.board_size
                        - 1):
                        break
                if check_for_x_in_a_row > 0:
                    stone_list[0] = index - (0 - i)
                    if stone_list[0] < ((index // self.board_size) * self.board_size):
                        continue
                    if (
                        stone_list[0]
                        > ((index // self.board_size) * self.board_size)
                        + self.board_size
                        - 1):
                        break

                # draw helper lines (debug)
                if show_line[3] == "H":
                    self.draw_winning_lines(
                        self.board_state[index],
                        stone_list[0],
                        stone_list[1],
                        stone_list[2],
                        stone_list[3],
                    )
                found_stone = []
                for i in range(check_for_x_in_a_row):
                    if self.board_state[stone_list[i]] == player_symbol:
                        found_stone.append(stone_list[i])
                if len(found_stone) >= check_for_x_in_a_row:
                    found_stone.insert(0, player_symbol)
                    return tuple(found_stone)

        # return not enough stones in a row!
        for s in range(self.board_size):
            if self.board_state[s] == self.empty_space:
                return (False,)
        return (None,)
