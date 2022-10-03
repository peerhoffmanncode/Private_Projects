import copy
import c4_Board


class KIPlayer:
    """KI Player class"""

    def __init__(
        self, board_to_play: c4_Board.Board, player_symbol: str, enemy_symbol: str
    ):
        self.current_board = board_to_play
        self.player_symbol = player_symbol
        self.enemy_symbol = enemy_symbol

    def field_evaluation(self):
        value = 1.0
        
        for x in range(self.current_board.board_size):
            for y in range(self.current_board.board_size):
                if self.current_board.board_state[x][y] == self.enemy_symbol:
                    value -= self.current_board.lookup_table[x][y]
                if self.current_board.board_state[x][y] == self.player_symbol:
                    value += self.current_board.lookup_table[x][y]
        return value

    def find_max(self, depth, alpha, beta):
        tmp = self.current_board.check_win(self.player_symbol, self.enemy_symbol)
        win = int(tmp[0])
        # if win[0]== self.player_symbol:
        #     return 2
        # elif win[0]== self.enemy_symbol:
        #     return 0
        if win != -1:
            return win
        if depth == 0:
            return self.field_evaluation()

        for y in range(self.current_board.board_size):
            if self.current_board.board_state[0][y] == self.current_board.empty_space:
                self.current_board.drop_stone(self.player_symbol, y)
                value = self.find_min(depth - 1, alpha, beta)
                if value > alpha:
                    alpha = value
                self.current_board.remove_stone(self.player_symbol, y)
                if alpha >= beta:
                    return beta
        return alpha

    def find_min(self, depth, alpha, beta):
        tmp = self.current_board.check_win(self.player_symbol, self.enemy_symbol)
        win = int(tmp[0])
        # if win[0]== self.player_symbol:
        #     return 2
        # elif win[0]== self.enemy_symbol:
        #     return 0
        if win != -1:
            return win

        if depth == 0:
            return self.field_evaluation()

        for y in range(self.current_board.board_size):
            if self.current_board.board_state[0][y] == self.current_board.empty_space:
                self.current_board.drop_stone(self.enemy_symbol, y)
                value = self.find_max(depth - 1, alpha, beta)
                if value < beta:
                    beta = value
                self.current_board.remove_stone(self.enemy_symbol, y)
                if beta <= alpha:
                    return alpha
        return beta

    def KIplayer_do_turn(self, symbol, depth=5):
        if depth < 1: depth = 1
        tmp = self.current_board.check_win(self.player_symbol, self.enemy_symbol)
        win = int(tmp[0])
        if win != -1:
            return win
        alpha = -999
        beta = 999
        KiShouldPlay_Column=0
        for y in range(self.current_board.board_size):
            if self.current_board.board_state[0][y] == self.current_board.empty_space:
                self.current_board.drop_stone(self.enemy_symbol, y)
                value = self.find_max(depth, alpha, beta)
                if value < beta:
                    beta = value
                    KiShouldPlay_Column = y
                self.current_board.remove_stone(self.enemy_symbol, y)
        return KiShouldPlay_Column