import random


def check_win(player_symbol, gamestate):
    # Horizontal
    if gamestate[0] == player_symbol and gamestate[1] == player_symbol and gamestate[2] == player_symbol: return True
    if gamestate[3] == player_symbol and gamestate[4] == player_symbol and gamestate[5] == player_symbol: return True
    if gamestate[6] == player_symbol and gamestate[7] == player_symbol and gamestate[8] == player_symbol: return True
    # Vertikal
    if gamestate[0] == player_symbol and gamestate[3] == player_symbol and gamestate[6] == player_symbol: return True
    if gamestate[1] == player_symbol and gamestate[4] == player_symbol and gamestate[7] == player_symbol: return True
    if gamestate[2] == player_symbol and gamestate[5] == player_symbol and gamestate[8] == player_symbol: return True
    # Diagonal
    if gamestate[0] == player_symbol and gamestate[4] == player_symbol and gamestate[8] == player_symbol: return True
    if gamestate[2] == player_symbol and gamestate[4] == player_symbol and gamestate[6] == player_symbol: return True
    return False


def can_make_three(position, player_symbol, gamestate):
    '''

    which position to check in 3 in a ROW is possible :param position:
    which symbol to check for                         :param player_symbol:
    List to check                                     :param gamestate:
    return which position to use                      :return:

    check for each position if a win is possible for CPU or Opponent

    '''
    temp_gamestate = gamestate[:]
    if temp_gamestate[position] != " ":
        return False

    temp_gamestate[position] = player_symbol
    return check_win(player_symbol, temp_gamestate)


def can_make_two(position, player_symbol, gamestate):

    '''

    which position to check in 3 in a ROW is possible :param position:
    which symbol to check for                         :param player_symbol:
    List to check                                     :param gamestate:
    return which position to use                      :return:

    check for each position is useful to build a row if TWO

    '''
    options_horizontale = False
    options_vertikale = False
    options_diagonale = False
    if gamestate[position] == " ":
        if position == 0:
            if gamestate[1] == player_symbol and gamestate[2] == " ": options_horizontale = True
            if gamestate[2] == player_symbol and gamestate[1] == " ": options_horizontale = True
            if gamestate[3] == player_symbol and gamestate[6] == " ": options_vertikale = True
            if gamestate[6] == player_symbol and gamestate[3] == " ": options_vertikale = True
            if gamestate[4] == player_symbol and gamestate[8] == " ": options_diagonale = True
            if gamestate[8] == player_symbol and gamestate[4] == " ": options_diagonale = True
        if position == 1:
            if gamestate[0] == player_symbol and gamestate[2] == " ": options_horizontale = True
            if gamestate[2] == player_symbol and gamestate[0] == " ": options_horizontale = True
            if gamestate[4] == player_symbol and gamestate[7] == " ": options_vertikale = True
            if gamestate[7] == player_symbol and gamestate[4] == " ": options_vertikale = True
        if position == 2:
            if gamestate[0] == player_symbol and gamestate[1] == " ": options_horizontale = True
            if gamestate[1] == player_symbol and gamestate[0] == " ": options_horizontale = True
            if gamestate[5] == player_symbol and gamestate[8] == " ": options_vertikale = True
            if gamestate[8] == player_symbol and gamestate[5] == " ": options_vertikale = True
            if gamestate[4] == player_symbol and gamestate[6] == " ": options_diagonale = True
            if gamestate[6] == player_symbol and gamestate[4] == " ": options_diagonale = True
        if position == 3:
            if gamestate[4] == player_symbol and gamestate[5] == " ": options_horizontale = True
            if gamestate[5] == player_symbol and gamestate[4] == " ": options_horizontale = True
            if gamestate[0] == player_symbol and gamestate[6] == " ": options_vertikale = True
            if gamestate[6] == player_symbol and gamestate[0] == " ": options_vertikale = True
        if position == 4:
            if gamestate[3] == player_symbol and gamestate[5] == " ": options_horizontale = True
            if gamestate[1] == player_symbol and gamestate[7] == " ": options_vertikale = True1
            if gamestate[5] == player_symbol and gamestate[3] == " ": options_horizontale = True
            if gamestate[7] == player_symbol and gamestate[1] == " ": options_vertikale = True
            if gamestate[0] == player_symbol and gamestate[8] == " ": options_diagonale = True
            if gamestate[2] == player_symbol and gamestate[6] == " ": options_diagonale = True
            if gamestate[8] == player_symbol and gamestate[0] == " ": options_diagonale = True
            if gamestate[6] == player_symbol and gamestate[2] == " ": options_diagonale = True
        if position == 5:
            if gamestate[3] == player_symbol and gamestate[4] == " ": options_horizontale = True
            if gamestate[2] == player_symbol and gamestate[8] == " ": options_vertikale = True
            if gamestate[4] == player_symbol and gamestate[3] == " ": options_horizontale = True
            if gamestate[8] == player_symbol and gamestate[2] == " ": options_vertikale = True
        if position == 6:
            if gamestate[7] == player_symbol and gamestate[8] == " ": options_horizontale = True
            if gamestate[0] == player_symbol and gamestate[3] == " ": options_vertikale = True
            if gamestate[8] == player_symbol and gamestate[7] == " ": options_horizontale = True
            if gamestate[3] == player_symbol and gamestate[0] == " ": options_vertikale = True
            if gamestate[2] == player_symbol and gamestate[4] == " ": options_diagonale = True
            if gamestate[4] == player_symbol and gamestate[2] == " ": options_diagonale = True
        if position == 7:
            if gamestate[6] == player_symbol and gamestate[8] == " ": options_horizontale = True
            if gamestate[1] == player_symbol and gamestate[4] == " ": options_vertikale = True
            if gamestate[8] == player_symbol and gamestate[6] == " ": options_horizontale = True
            if gamestate[4] == player_symbol and gamestate[1] == " ": options_vertikale = True
        if position == 8:
            if gamestate[6] == player_symbol and gamestate[7] == " ": options_horizontale = True
            if gamestate[2] == player_symbol and gamestate[5] == " ": options_vertikale = True
            if gamestate[7] == player_symbol and gamestate[6] == " ": options_horizontale = True
            if gamestate[5] == player_symbol and gamestate[2] == " ": options_vertikale = True
            if gamestate[0] == player_symbol and gamestate[4] == " ": options_diagonale = True
            if gamestate[4] == player_symbol and gamestate[0] == " ": options_diagonale = True

    if options_horizontale or options_vertikale or options_diagonale:
        return True
    else:
        return False


def find_best_choise(player_symbol, opponent_symbol, gamestate):
    '''

    which symbol uses the player/cpu                  :param player_symbol:
    which symbol uses the Opponent                    :param opponent_symbol::
    List to check                                     :param gamestate:
    return which position to use                      :return:

    Main routine to decide to steps of the CPU

    '''

    # Create a +1/-1 Random value to spice up cpu behavior
    random_value = random.randint(-1, 1)
    while random_value == 0:
        random_value = random.randint(-1, 1)

    if random_value < 0:
        von = 8
        bis = -1
    else:
        von = 0
        bis = 9

    # is somehow a cpu win possible? First interest!
    for i in range(von, bis, random_value):
        if can_make_three(i, player_symbol, gamestate):
            print("cpu win with: " + str(i + 1))
            return i + 1

    # Somehow Opp win possible? Needed to be blocked is second interest
    for i in range(von, bis, random_value):
        if can_make_three(i, opponent_symbol, gamestate):
            print("opp win with: " + str(i + 1) + " so CPU plays this field!")
            return i + 1

    # Can make 2 in row?
    for i in range(von, bis, random_value):
        if can_make_two(i, player_symbol, gamestate):
            print("cpu makes two with: " + str(i + 1) + " so CPU plays this field!")
            return i + 1

    # decide if CPU wants to use center cell (5)
    if gamestate[4] == " " and random_value > 0:
        print("cpu uses center cell !")
        return 5

    # Place at any free cell
    for i in range(von, bis, random_value):
        if gamestate[i] == " ":
            print("cpu uses random cell: " + str(i + 1))
            return i + 1

    return -1