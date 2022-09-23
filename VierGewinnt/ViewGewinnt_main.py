import random
import time
import os

class Board:
    ''' Main board class'''
    def __init__(self, board_size: int):
        ''' Initialize the board '''
        self.empty_space = " "
        self.board_size = board_size
        self.board_state = list(self.empty_space * self.board_size*self.board_size)


    def draw(self):
        os.system("clear")
        ''' Draw the board '''
        print("/" + ("-" * self.board_size) + "\\")
        count = 0
        for row in range(self.board_size):
            print("|", end="")
            for collumn in range(self.board_size):
                print(self.board_state[count], end="")
                count = count + 1
            print("|")
        print("\\" + ("-" * self.board_size) + "/")


    def drop_stone(self, player_symbol, collumn: int):
        ''' drop a stone of a player
            check if move is valide
            place stone
        '''
        safed_last_empty = -1
        for i in range(collumn, self.board_size*self.board_size, self.board_size):
            if self.board_state[i] == self.empty_space:
                safed_last_empty = i
                
        if safed_last_empty != -1:
            self.board_state[safed_last_empty] = player_symbol
            return True, safed_last_empty
        return False, safed_last_empty

    def draw_silly_lines(self, stone1, stone2, stone3, stone4):
        backup_list = self.board_state[:]
        self.board_state[stone1] = "!"
        self.board_state[stone2] = "!"
        self.board_state[stone3] = "!"
        self.board_state[stone4] = "!"
        self.draw()
        #time.sleep(0.1)
        self.board_state = backup_list[:]

    def check_win(self, player_symbol, index) -> bool:
        ''' check if a player is winning '''
                
        if self.board_state[index] == player_symbol:
            # horizontal
            for i in range(4):
                stone1 = index - (3 - i)
                if stone1 < ((index // self.board_size) * self.board_size): stone1 = ((index // self.board_size) * self.board_size)
                if stone1 > ((index // self.board_size) * self.board_size) + self.board_size - 1: stone1 = ((index // self.board_size) * self.board_size) + self.board_size -1
                stone2 = index - (2 - i)
                if stone2 < ((index // self.board_size) * self.board_size): stone2 = ((index // self.board_size) * self.board_size)
                if stone2 > ((index // self.board_size) * self.board_size) + self.board_size - 1: stone2 = ((index // self.board_size) * self.board_size) + self.board_size -1
                stone3 = index - (1 - i)
                if stone3 < ((index // self.board_size) * self.board_size): stone3 = ((index // self.board_size) * self.board_size)
                if stone3 > ((index // self.board_size) * self.board_size) + self.board_size - 1: stone3 = ((index // self.board_size) * self.board_size) + self.board_size -1 
                stone4 = index - (0 - i)
                if stone4 < ((index // self.board_size) * self.board_size): stone4 = ((index // self.board_size) * self.board_size)
                if stone4 > ((index // self.board_size) * self.board_size) + self.board_size - 1: stone4 = ((index // self.board_size) * self.board_size) + self.board_size -1
                #print((index // self.board_size), (index // self.board_size) * self.board_size, ((index // self.board_size) * self.board_size) + self.board_size -1)
                #print("index:", index, i, stone1, stone2, stone3, stone4, "=", stone4 - stone1)
                #print("index:", index, "checking :",i, stone1,self.board_state[stone1], stone2,self.board_state[stone2], stone3,self.board_state[stone3], stone4 ,self.board_state[stone4])
                #input()
                
                if (stone4 - stone1 == 3) and self.board_state[stone1] == player_symbol and self.board_state[stone2] == player_symbol and self.board_state[stone3] == player_symbol and self.board_state[stone4] == player_symbol:
                    return True
                
                self.draw_silly_lines(stone1, stone2, stone3, stone4)

            # vertical
            for i in range(self.board_size-3):
                stone1 = (index - (index // self.board_size) * self.board_size) + (i * self.board_size) 
                #if stone1 < (index - (index // self.board_size) * self.board_size): stone1 = (index - (index // self.board_size))
                #if stone1 > (index - (index // self.board_size) * self.board_size) * self.board_size: stone1 = (index - (index // self.board_size) * self.board_size) * self.board_size
                stone2 = (index - (index // self.board_size) * self.board_size) + ((i +1 )* self.board_size) 
                #if stone2 < (index - (index // self.board_size) * self.board_size): stone2 = (index - (index // self.board_size))
                #if stone2 > (index - (index // self.board_size) * self.board_size) * self.board_size: stone2 = (index - (index // self.board_size) * self.board_size) * self.board_size
                stone3 = (index - (index // self.board_size) * self.board_size) + ((i +2 ) * self.board_size) 
                #if stone3 < (index - (index // self.board_size) * self.board_size): stone3 = (index - (index // self.board_size))
                #if stone3 > (index - (index // self.board_size) * self.board_size) * self.board_size: stone3 = (index - (index // self.board_size) * self.board_size) * self.board_size 
                stone4 = (index - (index // self.board_size) * self.board_size) + ((i +3 ) * self.board_size) 
               
                if (stone4 - stone1 == self.board_size * 3) and self.board_state[stone1] == player_symbol and self.board_state[stone2] == player_symbol and self.board_state[stone3] == player_symbol and self.board_state[stone4] == player_symbol:
                    return True
                
                self.draw_silly_lines(stone1, stone2, stone3, stone4)      
        return False



##################################################### MAIN FUNCTION #############################################
def main():
    ''' This is the main program '''
    played_steps = 0
    game_size = 7
    main_board1 = Board(game_size)
    
    while True:
        place_at_rnd = random.randint(0,game_size-1)
        if played_steps % 2 == 0:
            player_symbol = "X"
        else: 
            player_symbol = "O"
        
        valid_move, last_played_position = main_board1.drop_stone(player_symbol, place_at_rnd)   # random.randint(0,game_size)
        if valid_move:
            played_steps = played_steps + 1

        os.system("clear")
        main_board1.draw()
        
        if main_board1.check_win(player_symbol, last_played_position):
            main_board1.draw()
            print("Win by player:",player_symbol )
            #time.sleep(5)
            break

        if played_steps == game_size*game_size: break
    print ("Took", played_steps, "turns, last turn was at collumn", place_at_rnd)


##################################################### CALL MAIN FUNCTION #############################################
if __name__ == "__main__":
    main()
    