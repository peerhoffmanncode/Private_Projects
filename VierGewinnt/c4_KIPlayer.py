import copy
import c4_Board

class KIPlayer:
    """KI Player class"""
    def __init__(self, board_to_play: c4_Board.Board, player_symbol: str, enemy_symbol: str):
        self.current_board = board_to_play
        self.player_symbol = player_symbol
        self.enemy_symbol = enemy_symbol


    def check_player_win(self, symbol):
        ''' method to check if a player can win with this stone '''
        # copy of current board!
        temp_board = copy.deepcopy(self.current_board)
        for KI_player_choice in range(temp_board.board_size):
            # drop a stone in virtual board copy!
            player_valid_move, player_last_played_position = temp_board.drop_stone(symbol, KI_player_choice)
            if player_valid_move:
                # check if KI player would win with this stone
                player_win_with = temp_board.check_win(symbol, player_last_played_position, 4)
                if player_win_with != (False,):
                    # if player can win return column to win
                    return KI_player_choice
            # rest copy to current board!
            temp_board = copy.deepcopy(self.current_board)
        temp_board = None
        return -1


    def player_looks_one_turn_ahead(self):
        ''' method to check if enemy can win with this stone '''
        # copy of current board!
        temp_board = copy.deepcopy(self.current_board)
        boardsize = temp_board.board_size
        options_to_choose_from = []
        for column in range(boardsize):
            # copy of current board!
            temp_board = copy.deepcopy(self.current_board)
            # drop a stone in virtual board copy!
            valid_move, _ = temp_board.drop_stone(self.player_symbol, column)
            if not valid_move: continue
            # copy of temp_board board!!! (2nd layer deepness)
            sub_temp_board = copy.deepcopy(temp_board)
            enemy_win_with = (False,)
            for choice in range(boardsize):
                # drop a stone in 2nd layer virtual board copy!
                enemy_valid_move, enemy_last_played_position = sub_temp_board.drop_stone(self.enemy_symbol, choice)
                if enemy_valid_move:
                    # check if ENEMY player would win with his next stone!!
                    enemy_win_with = sub_temp_board.check_win(self.enemy_symbol, enemy_last_played_position, 4)
                    if enemy_win_with != (False,):
                        # if ENEMY plyer would win break out and ignore this column!
                        break
                sub_temp_board = copy.deepcopy(temp_board)
            sub_temp_board = None
            # if ENEMY plyer can not win add column to OPTIONS
            if enemy_win_with == (False,):
                options_to_choose_from.append(column)
        temp_board = None
        # return options_to_choose_from
        if options_to_choose_from == []:
            return tuple(range(boardsize))
        else:
            return tuple(options_to_choose_from)


    def play_best_option(self, only_choose_from_this_list: tuple) -> tuple:
        ''' method to check for best stone to play '''
        # copy of current board!
        temp_board = copy.deepcopy(self.current_board)
        boardsize = temp_board.board_size
        #options_to_choose_from = []

        # if given list only_choose_from_this_list is empty, return all options!
        if not only_choose_from_this_list:
            return tuple(range(boardsize))

        for lenght_of_connecting_stones in range(4,1,-1):
            options_to_choose_from = []
            # is it possible to make a connecting 4 in a 2 step move?!
            for column in only_choose_from_this_list:
                # copy of current board!
                temp_board = copy.deepcopy(self.current_board)
                # drop a stone in virtual board copy!
                valid_move, _ = temp_board.drop_stone(self.player_symbol, column)
                if not valid_move: continue
                # copy of temp_board board!!! (2nd layer deepness)
                sub_temp_board = copy.deepcopy(temp_board)
                player_win_with = (False,)
                for choice in range(boardsize):
                    # drop a stone in 2nd layer virtual board copy!
                    player_valid_move, player_last_played_position = sub_temp_board.drop_stone(self.player_symbol, choice)
                    if player_valid_move:
                        # check if KI player would win with his next stone!!
                        player_win_with = sub_temp_board.check_win(self.player_symbol, player_last_played_position, lenght_of_connecting_stones)
                        # if KI player can win add column to OPTIONS
                        #print(lenght_of_connecting_stones, player_win_with)
                        #input()
                        if player_win_with != (False,):
                            #print("column:",column,"length:", lenght_of_connecting_stones,"stones:", player_win_with)
                            options_to_choose_from.append(column)
                            break
                    sub_temp_board = copy.deepcopy(temp_board)
                sub_temp_board = None

            # return options_to_choose_from if connectig 4
            print("Length:",lenght_of_connecting_stones, "Columns:", options_to_choose_from)
            if options_to_choose_from:
                temp_board = None
                return tuple(options_to_choose_from)

        temp_board = None
        # return options_to_choose_from
        if options_to_choose_from == []:
            return only_choose_from_this_list
        else:
            return options_to_choose_from
            