from Display import *
from Play import *
from TilesAcces import *
from TilesMoves import *
from user_entries import *

def threes():
    print("Welcome to Threes!")
    plateau = None
    choix = None
    while choix != 'Q':
        choix = get_user_menu(plateau)
        if choix == 'N':
            plateau = None
            plateau = cycle_play(plateau)
        elif choix == 'C':
            plateau = cycle_play(plateau)
        elif choix == 'S':
            if plateau == None:
                print("No game in progress")
            else:
                save_game(plateau)
        elif choix == 'L':
            load_game()
    print("Thank you for playing ;-)")