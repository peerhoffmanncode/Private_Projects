""" Board class file"""
import time
import os
import copy
import colorama


class Board:
    """Main board class"""

    def __init__(self, board_size: int, player_symbol1: str, player_symbol2: str):
        """Initialize the board"""
        self.empty_space = "-"
        if board_size < 5:
            board_size = 5
        self.board_size_x = board_size
        self.board_size_y = board_size-1
        self.board_state = [
            [self.empty_space for j in range(self.board_size_x)]
            for i in range(self.board_size_y)
        ]

        self.player_symbol1 = player_symbol1
        self.player_symbol2 = player_symbol2

        ### 7x7 static (to be implemented)
        self.lookup_table = [
            [0.0 for j in range(self.board_size_x)] for i in range(self.board_size_y)
        ]

        # call build_lookup_table to create the lookup table
        self.build_lookup_table()

    def build_lookup_table(self):
        add_up = 0.001
        # Vertical
        for x in range(self.board_size_x - 3):
            for y in range(self.board_size_y):
                self.lookup_table[y][x + 0] += add_up
                self.lookup_table[y][x + 1] += add_up
                self.lookup_table[y][x + 2] += add_up
                self.lookup_table[y][x + 3] += add_up
        # Horizontal
        for x in range(self.board_size_x):
            for y in range(self.board_size_y - 3):
                self.lookup_table[y + 0][x] += add_up
                self.lookup_table[y + 1][x] += add_up
                self.lookup_table[y + 2][x] += add_up
                self.lookup_table[y + 3][x] += add_up
        # Diagonal
        for x in range(self.board_size_x - 3):
            for y in range(self.board_size_y - 3):
                self.lookup_table[y + 0][x + 0] += add_up
                self.lookup_table[y + 1][x + 1] += add_up
                self.lookup_table[y + 2][x + 2] += add_up
                self.lookup_table[y + 3][x + 3] += add_up
        # Diagonal
        for x in range(self.board_size_x - 3, self.board_size_x):
            for y in range(self.board_size_y - 3):
                self.lookup_table[y + 0][x - 0] += add_up
                self.lookup_table[y + 1][x - 1] += add_up
                self.lookup_table[y + 2][x - 2] += add_up
                self.lookup_table[y + 3][x - 3] += add_up

    def draw(self):
        """Method to draw the board"""
        os.system("clear")
        print("  /" + ("-" * self.board_size_x) + "\\")
        for row in range(self.board_size_y):
            print(f"{row:2}|", end="")
            for column in range(self.board_size_x):
                if self.player_symbol1 == self.board_state[row][column]:
                    print(
                        colorama.Fore.CYAN
                        + self.board_state[row][column]
                        + colorama.Fore.RESET,
                        end="",
                    )
                elif self.player_symbol2 == self.board_state[row][column]:
                    print(
                        colorama.Fore.YELLOW
                        + self.board_state[row][column]
                        + colorama.Fore.RESET,
                        end="",
                    )
                else:
                    print(self.board_state[row][column], end="")
            print("|")
        print("  \\", end ="")
        for row in range(self.board_size_x):
            print(str(row)[-1], end="")
        print("/")

    def draw_winning_lines(self, symbol, stone1, stone2, stone3, stone4):
        """draw helper lines for debugging"""
        bkp1 = self.board_state[stone1[0]][stone1[1]]
        bkp2 = self.board_state[stone2[0]][stone2[1]]
        bkp3 = self.board_state[stone3[0]][stone3[1]]
        bkp4 = self.board_state[stone4[0]][stone4[1]]

        self.board_state[stone1[0]][stone1[1]] = (
            colorama.Fore.GREEN + symbol + colorama.Fore.RESET
        )
        self.board_state[stone2[0]][stone2[1]] = (
            colorama.Fore.GREEN + symbol + colorama.Fore.RESET
        )
        self.board_state[stone3[0]][stone3[1]] = (
            colorama.Fore.GREEN + symbol + colorama.Fore.RESET
        )
        self.board_state[stone4[0]][stone4[1]] = (
            colorama.Fore.GREEN + symbol + colorama.Fore.RESET
        )
        self.draw()
        self.board_state[stone1[0]][stone1[1]] = bkp1
        self.board_state[stone2[0]][stone2[1]] = bkp2
        self.board_state[stone3[0]][stone3[1]] = bkp3
        self.board_state[stone4[0]][stone4[1]] = bkp4
        # time.sleep(0.05)

    def drop_stone(self, player_symbol, column: int):
        """drop a stone of a player check if move is valid place stone"""
        for y in range(self.board_size_y - 1, -1, -1):
            if self.board_state[y][column] == self.empty_space:
                self.board_state[y][column] = player_symbol
                return True, (y, column)
        return False, None

    def remove_stone(self, symbol: str, column: int):
        """remove a stone of a player"""
        for y in range(self.board_size_y):
            if self.board_state[y][column] != self.empty_space:
                self.board_state[y][column] = self.empty_space
                break

    def check_win(self, player_symbol: str, enemy_symbol: str) -> tuple:
        """check if a player is winning"""
        show_line = "-"  # DDVH flag to show debug lines!4
        for winner_symbol in (enemy_symbol, player_symbol):
            # Horizontal
            for x in range(self.board_size_x - 3):
                for y in range(self.board_size_y):
                    if "H" in show_line:
                        self.draw_winning_lines(
                            winner_symbol,
                            (x + 0, y),
                            (x + 1, y),
                            (x + 2, y),
                            (x + 3, y),
                        )
                    if (
                        self.board_state[y][x + 0] == winner_symbol
                        and self.board_state[y][x + 1] == winner_symbol
                        and self.board_state[y][x + 2] == winner_symbol
                        and self.board_state[y][x + 3] == winner_symbol
                    ):
                        return (
                            winner_symbol,
                            (x + 0, y),
                            (x + 1, y),
                            (x + 2, y),
                            (x + 3, y),
                        )
            # Vertical
            for x in range(self.board_size_x):
                for y in range(self.board_size_y - 3):
                    if "V" in show_line:
                        self.draw_winning_lines(
                            winner_symbol,
                            (x, y + 0),
                            (x, y + 1),
                            (x, y + 2),
                            (x, y + 3),
                        )
                    if (
                        self.board_state[y + 0][x] == winner_symbol
                        and self.board_state[y + 1][x] == winner_symbol
                        and self.board_state[y + 2][x] == winner_symbol
                        and self.board_state[y + 3][x] == winner_symbol
                    ):
                        return (
                            winner_symbol,
                            (x, y + 0),
                            (x, y + 1),
                            (x, y + 2),
                            (x, y + 3),
                        )
            # Diagonal
            for x in range(self.board_size_x - 3):
                for y in range(self.board_size_y - 3):
                    if "1" in show_line:
                        self.draw_winning_lines(
                            winner_symbol,
                            (x + 0, y + 0),
                            (x + 1, y + 1),
                            (x + 2, y + 2),
                            (x + 3, y + 3),
                        )
                    if (
                        self.board_state[y + 0][x + 0] == winner_symbol
                        and self.board_state[y + 1][x + 1] == winner_symbol
                        and self.board_state[y + 2][x + 2] == winner_symbol
                        and self.board_state[y + 3][x + 3] == winner_symbol
                    ):
                        return (
                            winner_symbol,
                            (x + 0, y + 0),
                            (x + 1, y + 1),
                            (x + 2, y + 2),
                            (x + 3, y + 3),
                        )
            # Diagonal BUG ?!
            for x in range(self.board_size_x - 3, self.board_size_x):
                for y in range(self.board_size_y - 3):
                    if "2" in show_line:
                        self.draw_winning_lines(
                            winner_symbol,
                            (x - 0, y + 0),
                            (x - 1, y + 1),
                            (x - 2, y + 2),
                            (x - 3, y + 3),
                        )
                    if (
                        self.board_state[y + 0][x - 0] == winner_symbol
                        and self.board_state[y + 1][x - 1] == winner_symbol
                        and self.board_state[y + 2][x - 2] == winner_symbol
                        and self.board_state[y + 3][x - 3] == winner_symbol
                    ):
                        return (
                            winner_symbol,
                            (x - 0, y + 0),
                            (x - 1, y + 1),
                            (x - 2, y + 2),
                            (x - 3, y + 3),
                        )

        for x_l in range(self.board_size_x):
            if self.board_state[0][x_l] == self.empty_space:
                # no win, board not full
                return (-1,)

        # board full!
        return (1,)
