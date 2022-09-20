import random
import time
import os

class Board:
    def __init__(self, board_size: int):
        self.empty_space = " "
        self.board_size = board_size
        self.board_state = list(self.empty_space * self.board_size*self.board_size)


    def draw(self):
        print("/" + ("-" * self.board_size) + "\\   ")
        count = 0
        for row in range(self.board_size):
            print("|", end="")
            for collumn in range(self.board_size):
                print(self.board_state[count], end="")
                count = count + 1
            print("|")
        print("\\" + ("-" * self.board_size) + "/")

    def drop_stone(self, symbole, collumn: int) -> bool:
        safed_last_empty = -1
        for i in range(collumn, self.board_size*self.board_size, self.board_size):
            if self.board_state[i] == self.empty_space:
                safed_last_empty = i
                
        if safed_last_empty != -1:
            self.board_state[safed_last_empty] = symbole
            return True
        return False
            

def main():
    ''' This is the main program '''
    played_steps = 0
    game_size = 5
    main_board1 = Board(game_size)
    
    
    while True:
        place_at_rnd = random.randint(0,game_size-1)
        if played_steps % 2 == 0:
            player_symbol = "X"
            #place_at_rnd = int(input("where : "))
        else:
            player_symbol = "O"
        if main_board1.drop_stone(player_symbol, place_at_rnd):   # random.randint(0,game_size)
            played_steps = played_steps + 1

        os.system("clear")
        main_board1.draw()
        print ("Turn", played_steps, "at collumn", place_at_rnd)
        #time.sleep(0.1)
        if played_steps == game_size*game_size: break

if __name__ == "__main__":
    main()
    