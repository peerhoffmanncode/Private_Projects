import copy
import c4_Board as c4_Board

class KIPlayer:
    """KI Player class"""
    def __init__(self, board_to_play: c4_Board.Board, player_symbol: str, enemy_symbol: str):
        self.current_board = board_to_play
        self.player_symbol = player_symbol
        self.enemy_symbol = enemy_symbol


    def check_player_win(self):
        temp_board = copy.deepcopy(self.current_board)
        for KI_player_choice in range(temp_board.board_size):
            player_valid_move, player_last_played_position = temp_board.drop_stone(self.player_symbol, KI_player_choice)
            if player_valid_move:
                player_win_with = temp_board.check_win(self.player_symbol, 
                                                       player_last_played_position)
                if player_win_with != (False,):
                    return KI_player_choice

            temp_board = copy.deepcopy(self.current_board)

        temp_board = None
        return -1

    def check_enemy_win(self):
        temp_board = copy.deepcopy(self.current_board)

        for KI_player_choice in range(temp_board.board_size):
            enemy_valid_move, enemy_last_played_position = temp_board.drop_stone(self.enemy_symbol, KI_player_choice)
            if enemy_valid_move:
                enemy_win_with = temp_board.check_win(self.enemy_symbol, 
                                                      enemy_last_played_position)
                if enemy_win_with != (False,):
                    return KI_player_choice

            temp_board = copy.deepcopy(self.current_board)
                       
        temp_board = None
        return -1


    def play_one_turn_ahead(self):
        temp_board = copy.deepcopy(self.current_board)
        boardsize = temp_board.board_size
        options_to_choose_from = []
        for collumn in range(boardsize):
            temp_board = copy.deepcopy(self.current_board)
            valid_move, _ = temp_board.drop_stone(self.player_symbol, collumn)
            if not valid_move: continue

            sub_temp_board = copy.deepcopy(temp_board)
            enemy_win_with = (False,)
            for choise in range(boardsize):
                enemy_valid_move, enemy_last_played_position = sub_temp_board.drop_stone(self.enemy_symbol, choise)
                if enemy_valid_move:
                    enemy_win_with = sub_temp_board.check_win(self.enemy_symbol, 
                                                              enemy_last_played_position)
                    if enemy_win_with != (False,):
                        break
                sub_temp_board = copy.deepcopy(temp_board)

            sub_temp_board = None
            if enemy_win_with == (False,):
                options_to_choose_from.append(collumn)

        temp_board = None
        if options_to_choose_from == []:
            return tuple(range(boardsize))
        else:
            return tuple(options_to_choose_from)


    def play_best_option(self, only_choose_from_this_list: tuple):
        temp_board = copy.deepcopy(self.current_board)
        boardsize = temp_board.board_size
        options_to_choose_from = []
        
        if not only_choose_from_this_list:
            return tuple(range(boardsize))

        for collumn in only_choose_from_this_list:
            temp_board = copy.deepcopy(self.current_board)
            valid_move, _ = temp_board.drop_stone(self.player_symbol, collumn)
            if not valid_move: continue

            sub_temp_board = copy.deepcopy(temp_board)
            player_win_with = (False,)
            for choise in range(boardsize):
                player_valid_move, player_last_played_position = sub_temp_board.drop_stone(self.player_symbol, choise)
                if player_valid_move:
                    player_win_with = sub_temp_board.check_win(self.player_symbol, 
                                                              player_last_played_position)
                    if player_win_with != (False,):
                        options_to_choose_from.append(collumn)
                        break
                sub_temp_board = copy.deepcopy(temp_board)
            sub_temp_board = None

        temp_board = None
        if options_to_choose_from == []:
            return only_choose_from_this_list
        else:
            return tuple(options_to_choose_from)
