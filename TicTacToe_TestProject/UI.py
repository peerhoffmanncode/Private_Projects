import pygame


def draw_ruls():
    print("===========")
    print("Tic Tac Toe")
    print("===========")
    print("Bitte die Zahlen von 1 - 9 für die Felder eingeben. 3 x 3 Spieleld.\n")


def draw_game(WINDOW, gamestate, player, symbol):
    color1 = (0, 0, 255)
    color2 = (255, 0, 0)

    # draw_ruls()
    WINDOW.fill((255, 255, 255))

    if player == 1:
        pygame.draw.rect(WINDOW, color1, pygame.Rect(0, 0, 500, 500), 10)
        draw_string(WINDOW, "Spieler : " + str(player), 100, 20, 20)
    elif player == 2:
        pygame.draw.rect(WINDOW, color2, pygame.Rect(0, 0, 500, 500), 10)
        draw_string(WINDOW, "Spieler : " + str(player), 100, 20, 20)
    else:
        pass

    for i in range(0, 300, 100):
        pygame.draw.rect(WINDOW, (0, 0, 0), pygame.Rect(100, 50 + i, 100, 100), 1)
        pygame.draw.rect(WINDOW, (0, 0, 0), pygame.Rect(200, 50 + i, 100, 100), 1)
        pygame.draw.rect(WINDOW, (0, 0, 0), pygame.Rect(300, 50 + i, 100, 100), 1)

    x = 0
    y = 0
    for i in range(9):
        if gamestate[i] == " ":
            pass
        elif gamestate[i] == symbol:
            pygame.draw.rect(WINDOW, color1, pygame.Rect(110 + x, 60 + y, 80, 80))
        else:
            pygame.draw.rect(WINDOW, color2, pygame.Rect(110 + x, 60 + y, 80, 80))

        x += 100
        if x > 250:
            x = 0
            y += 100

    pygame.display.update()


def draw_ask_for_input(WINDOW, message):
    return input(message)


def draw_string(WINDOW, message, x_pos, y_pos, font_size):
    my_font = pygame.font.SysFont('Arial', font_size)
    text_surface = my_font.render(message, True, (0, 0, 0))
    WINDOW.blit(text_surface, (x_pos, y_pos))
    pygame.display.update()


def draw_final_stats(WINDOW, gamestoplay, games_won_player1, games_won_player2, games_tie):
    a = "{0:.1f}".format(100 * (games_won_player1 / gamestoplay))
    b = "{0:.1f}".format(100 * (games_won_player2 / gamestoplay))
    c = "{0:.1f}".format(100 * (games_tie / gamestoplay))
    line1 = "Gespielte Spiele : " + str(gamestoplay)
    line2 = "Spieler 1 hat " + a + "% der Spiele gewonnen, Spieler 2 hat " + b + "% der Spiele gewonnen"
    line3 = c + "% Spiele ware unentschieden."

    draw_string(WINDOW, line1, 20, 370, 15)
    draw_string(WINDOW, line2, 20, 390, 12)
    draw_string(WINDOW, line3, 20, 405, 12)
    pygame.display.update()
