import os

def draw_init_window():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_ruls():
    print("===========")
    print("Tic Tac Toe")
    print("===========")
    print("Bitte die Zahlen von 1 - 9 für die Felder eingeben. 3 x 3 Spieleld.\n")
    #print("\n")

def draw_game(gamestate):

    draw_ruls()
    for i in range(-1, 8, 3):
        print("-[" + str(i + 2) + "]-[" + str(i + 3) + "]-[" + str(i + 4) + "]-")
        printedline = "| " + gamestate[i + 1] + " | " + gamestate[i + 2] + " | " + gamestate[i + 3] + " |"
        print(printedline)
    print("-------------")



def draw_ask_for_input(Message):
    return input(Message)

def draw_string(Message):
    print(Message)

def draw_final_stats(gamestoplay, games_won_player1, games_won_player2, games_tie):
    a = "{0:.1f}".format(100 * (games_won_player1 / gamestoplay))
    b = "{0:.1f}".format(100 * (games_won_player2 / gamestoplay))
    c = "{0:.1f}".format(100 * (games_tie / gamestoplay))
    print("Spieler 1 hat " + a + "% Spiele gewonnen, Spieler 2 hat " + b + "% Spiele gewonnen, " + c + "% Spiele ware untetschieden.")