from Display import *
from Play import *
from TilesMoves import *
from user_entries import *

def check_indice(plateau, indice):
    if indice < plateau['n'] and indice >= 0:
        return True
    else:
        return False

def check_room(plateau, lig, col):
    if check_indice(plateau, lig) and check_indice(plateau, col):
        return True
    else:
        return False

def get_value(plateau, lig, col):
    if check_room(plateau, lig, col) == False:
        return 'Error'
    temp = plateau['tiles']
    return temp[lig * 4 + col]

def set_value(plateau, lig, col, val):
    if check_room(plateau, lig, col) == False:
        return 'Error'
    temp = plateau['tiles']
    temp[lig * 4 + col] = val
    plateau['tiles'] = temp
    return plateau

def is_room_empty(plateau, lig, col):
    if get_value(plateau, lig, col) == 0:
        return True
    else:
        return False

