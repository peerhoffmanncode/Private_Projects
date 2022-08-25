import pygame
from pygame.locals import *
import sys
import KI
import UI


def quit_game():
    # pygame.quit
    sys.exit()


def input_move(player):
    while True:
        player_input = UI.draw_ask_for_input(TicTacToe_Game_Window, "Spieler " + str(player) + "bitte geben Sie Ihren "
                                                                                               "Zug ein: ")
        try:
            player_input = int(player_input)
            if 1 <= player_input <= 9:
                return player_input
        except ValueError:
            pass
        UI.draw_string(TicTacToe_Game_Window, "Bitte nur die Zahlen 1 - 9 eingeben.", 50, 400, 20)


def check_valid_move(player_move, player_symbol, gamestate):
    if player_move > 9 or player_move < 1:
        return False

    if gamestate[player_move - 1] == " ":
        gamestate[player_move - 1] = player_symbol
        return True
    else:
        UI.draw_string(TicTacToe_Game_Window, "ungültiger Zug! Bitte nochmal eingeben.", 50, 400, 20)
        return False


def make_turn(player, is_it_a_cpu_player, player_symbol, the_gegner_symbol, gamestate):
    #print (player, player_symbol)
    valide_move_done = False
    grid = [(100, 50), (200, 50), (300, 50), (100, 150), (200, 150), (300, 150), (100, 250), (200, 250), (300, 250)]
    mouse_x_pos, mouse_y_pos = 0, 0

    if is_it_a_cpu_player == 0:
        while not valide_move_done:

            clicked = False
            while not clicked:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        mouse_x_pos, mouse_y_pos = pygame.mouse.get_pos()
                        clicked = True
                    if event.type == pygame.QUIT:
                        quit_game()

            playerturn = -1
            for i in range(9):
                x, y = grid[i]
                if x <= mouse_x_pos < x + 99 and y <= mouse_y_pos < y + 99:
                    playerturn = i + 1
                    break

            valide_move_done = check_valid_move(playerturn, player_symbol, gamestate)

    else:
        while not valide_move_done:
            playerturn = KI.find_best_choise(player_symbol, the_gegner_symbol, gamestate)
            if playerturn == -1:
                break
            valide_move_done = check_valid_move(playerturn, player_symbol, gamestate)


def check_board_full(gamestate):
    for i in gamestate:
        if i == " ":
            return False
    return True

def game(gamestoplay = 1, symbol_to_use1 = "X", is_cpu_player_1 = 0, symbol_to_use2 = "O", is_cpu_player_2 = 1):
    games_won_player1 = 0
    games_won_player2 = 0
    games_tie = 0

    allgames = gamestoplay

    # Game loop
    Run = True
    while Run:
        allgames -= 1
        if allgames < 1:
            Run = False

        spieler_nummer = 1
        spieler_symbol = symbol_to_use1
        gegner_symbol = symbol_to_use2
        is_cpu_player = is_cpu_player_1

        # inital Values
        tictactoe_gamestate = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        game_done = False
        board_full = False


        UI.draw_game(TicTacToe_Game_Window, tictactoe_gamestate, spieler_nummer, symbol_to_use1)

        pygame.event.clear()
        while game_done is not True and board_full is not True:
            # Pygame event handler

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Run = False

            # while True:
            #     event = pygame.event.wait()
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         sys.exit()
            #     elif event.type == KEYDOWN:
            #         break

            # Player or CPU makes a turn
            make_turn(spieler_nummer, is_cpu_player, spieler_symbol, gegner_symbol, tictactoe_gamestate)

            # Check game states
            game_done = KI.check_win(spieler_symbol, tictactoe_gamestate)
            board_full = check_board_full(tictactoe_gamestate)

            # change to current player
            if not game_done and not board_full:
                if spieler_nummer == 1:
                    spieler_nummer = 2
                    spieler_symbol = symbol_to_use2
                    gegner_symbol = symbol_to_use1
                    is_cpu_player = is_cpu_player_2
                else:
                    # Spieler 1 spielt
                    spieler_nummer = 1
                    spieler_symbol = symbol_to_use1
                    gegner_symbol = symbol_to_use2
                    is_cpu_player = is_cpu_player_1

            # DRAW GAME
            UI.draw_game(TicTacToe_Game_Window, tictactoe_gamestate, spieler_nummer, symbol_to_use1)

            # FPS
            clock.tick(FPS)

        if game_done is True:
            UI.draw_string(TicTacToe_Game_Window, "Spieler " + str(spieler_nummer) + " hat Gewonnen! :-) yeeeay!!!",
                           50, 400, 20)
            pygame.time.wait(1500)
            if spieler_nummer == 1:
                games_won_player1 += 1
            else:
                games_won_player2 += 1
        elif board_full is True:
            UI.draw_string(TicTacToe_Game_Window, "Unentschieden! Kein Spieler hat gewonnen ;-)", 50, 400, 20)
            games_tie += 1
            pygame.time.wait(1500)
        else:
            pass



    UI.draw_game(TicTacToe_Game_Window, tictactoe_gamestate, -1, symbol_to_use1)
    UI.draw_final_stats(TicTacToe_Game_Window, abs(allgames - gamestoplay),
                        games_won_player1, games_won_player2, games_tie)


if __name__ == '__main__':
    # Init pygame
    pygame.init()
    pygame.font.init()

    # Interface
    WIDTH = 500
    HIGH = 500
    FPS = 60

    # init Window
    TicTacToe_Game_Window = pygame.display.set_mode((WIDTH, HIGH))
    pygame.display.set_caption("Tic Tac Toe !")
    clock = pygame.time.Clock()

    keep_playing = True
    while keep_playing:

        game(100, "X", 0, "O", 1)

        UI.draw_string(TicTacToe_Game_Window, "Nochmal Spielen? >Klick hier!<", 110, 450, 20)
        playagain = False
        while not playagain:
            for event in pygame.event.get():
                # play again clicked?
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x_pos, mouse_y_pos = pygame.mouse.get_pos()
                    x = 110
                    y = 450
                    if x <= mouse_x_pos < x + 280 and y <= mouse_y_pos < y + 50:
                        playagain = True
                        break

                # quit game?
                if event.type == pygame.QUIT:
                    quit_game()
