import math
import copy
import c4_Board


class KIPlayer:
    """KI Player class"""

    def __init__(
        self,
        board_to_play: c4_Board.Board,
        player_symbol: str,
        enemy_symbol: str,
        cpu_depth: int = 5,
    ):
        self.current_board = board_to_play
        self.player_symbol = player_symbol
        self.enemy_symbol = enemy_symbol
        self.cpu_depth = cpu_depth

    def field_evaluation(self, depth, player):
        value = 1.0
        for y in range(self.current_board.board_size_y):
            for x in range(self.current_board.board_size_x):
                if self.current_board.board_state[y][x] == self.enemy_symbol:
                    value -= self.current_board.lookup_table[y][x]
                if self.current_board.board_state[y][x] == self.player_symbol:
                    value += self.current_board.lookup_table[y][x]
        #Adjust the value based on the depth of the search and the player whose turn it is
        if player == self.player_symbol:
            value += depth * 0.1
        else:
            value -= depth * 0.1
        return value

    def minmax(self, depth, player, alpha, beta):

        win = self.current_board.check_win(self.player_symbol, self.enemy_symbol)[0]

        if win == self.player_symbol:
            return 10
        elif win == self.enemy_symbol:
            return -10

        if depth <= 0:
            return self.field_evaluation(depth, player)

        if player == self.player_symbol:
            enemy = self.enemy_symbol

            for column in range(self.current_board.board_size_x):
                if (
                    self.current_board.board_state[0][column]
                    == self.current_board.empty_space
                ):
                    self.current_board.drop_stone(player, column)
                    score = self.minmax(depth - 1, enemy, alpha, beta)
                    self.current_board.remove_stone(player, column)
                    beta = max(beta, score)
                    alpha = max(alpha, score)
                    # if the maximum score is greater than or equal to beta, return it
                    if alpha >= beta:
                        return beta
            return alpha
        else:
            enemy = self.player_symbol
            for column in range(self.current_board.board_size_x):
                if (
                    self.current_board.board_state[0][column]
                    == self.current_board.empty_space
                ):
                    self.current_board.drop_stone(player, column)
                    score = self.minmax(depth - 1, enemy, alpha, beta)
                    self.current_board.remove_stone(player, column)
                    alpha = min(alpha, score)
                    beta = min(beta, score)
                    # if the minimum score is less than or equal to alpha, return it
                    if beta <= alpha:
                        return alpha
            return beta

    def ki_player_do_turn(self, player):
        if self.cpu_depth < 1:
            self.cpu_depth = 1
        win = int(
            self.current_board.check_win(self.player_symbol, self.enemy_symbol)[0]
        )
        if win != -1:
            return win

        ki_should_play_this_column = -1

        if player == self.player_symbol:
            max_score = -math.inf
            alpha = -math.inf
            beta = math.inf
            enemy = self.enemy_symbol
            for column in range(self.current_board.board_size_x):

                if (
                    self.current_board.board_state[0][column]
                    == self.current_board.empty_space
                ):
                    self.current_board.drop_stone(player, column)
                    score = self.minmax(self.cpu_depth, enemy, alpha, beta)
                    self.current_board.remove_stone(player, column)
                    alpha = max(alpha, score)
                    if score > max_score:
                        max_score = score
                        ki_should_play_this_column = column
                    alpha = max(alpha, score)
        else:
            min_score = math.inf
            alpha = -math.inf
            beta = math.inf
            enemy = self.player_symbol
            for column in range(self.current_board.board_size_x):
                if (
                    self.current_board.board_state[0][column]
                    == self.current_board.empty_space
                ):
                    self.current_board.drop_stone(player, column)
                    score = self.minmax(self.cpu_depth, enemy, alpha, beta)
                    self.current_board.remove_stone(player, column)
                    beta = min(beta, score)
                    if score < min_score:
                        min_score = score
                        ki_should_play_this_column = column
                    beta = min(beta, score)
        return ki_should_play_this_column
