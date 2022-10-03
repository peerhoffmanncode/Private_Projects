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
        value = 1
        for x in range(self.current_board.board_size):
            for y in range(self.current_board.board_size):
                if self.current_board.board_state[x*y] == self.enemy_symbol:
                    value -= self.current_board.lookup_table[x*y]
                if self.current_board.board_state[x*y] == self.player_symbol:
                    value += self.current_board.lookup_table[x*y]
        return value
    
    def find_max(self, depth, alpha, beta):
        win = self.current_board.check_win(self.player_symbol,0,4)
        if win != (False,):
            return win
        if depth == 0:
            return self.field_evaluation()
        
        maxvalue = -999
        for y in range(self.current_board.board_size):
            tmp = copy.deepcopy(self.current_board)
            if self.current_board.board_state[y] == self.current_board.empty_space:
                self.current_board.drop_stone(self.player_symbol, y)
                value = self.find_min(depth - 1, alpha, beta)
                if value > maxvalue:
                    maxvalue = value
                self.current_board = copy.deepcopy(tmp)
        return maxvalue

    def find_min(self, depth, alpha, beta):
        win = self.current_board.check_win(self.player_symbol, -1, 4)
        if win != (False,):
            return win
        if depth == 0:
            return self.field_evaluation()
        
        minvalue = 999
        for y in range(self.current_board.board_size):
            tmp = copy.deepcopy(self.current_board)
            if self.current_board.board_state[y] == self.current_board.empty_space:
                self.current_board.drop_stone(self.enemy_symbol, y)
                value = self.find_max(depth - 1, alpha, beta)
                if value < minvalue:
                    minvalue = value
                self.current_board = copy.deepcopy(tmp)
        return minvalue
    
    def KIplayer_do_turn(self, depth=5):
        print("'schhh deeengge!")
        alpha, beta = 0,0
        KiShouldPlay_Column=None
        win = self.current_board.check_win(self.player_symbol, -1, 4)
        if win != (False,):
            return win
        if depth == 0:
            return self.field_evaluation()
        
        minvalue = 999
        for y in range(self.current_board.board_size):
            tmp = copy.deepcopy(self.current_board)
            if self.current_board.board_state[y] == self.current_board.empty_space:
                self.current_board.drop_stone(self.enemy_symbol, y)
                value = self.find_min(depth - 1, alpha, beta)
                if value < minvalue:
                    minvalue = value
                    KiShouldPlay_Column = y
                    print(KiShouldPlay_Column)
                self.current_board = copy.deepcopy(tmp)
        return minvalue