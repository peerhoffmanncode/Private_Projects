import copy
import random, time
import colorama
import c4_Board as Board


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


    def played_ahead_turn(self):
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
                    enemy_win_with = sub_temp_board.check_win(self.enemy_symbol, enemy_last_played_position)
                    if enemy_win_with != (False,):
                        #sub_temp_board.draw_winning_lines(self.enemy_symbol, *enemy_win_with)
                        print(f"cant use {collumn} for {self.player_symbol}!")
                        #time.sleep(.5)
                        break
                sub_temp_board = copy.deepcopy(temp_board)
            
            sub_temp_board = None
            if enemy_win_with == (False,):
                options_to_choose_from.append(collumn)

        temp_board = None
        # print(options_to_choose_from)
        # time.sleep(.5)
        if len(options_to_choose_from) == boardsize or options_to_choose_from == []:
            return -1, (False, )
        else:
            return random.choice(options_to_choose_from), (False, )
