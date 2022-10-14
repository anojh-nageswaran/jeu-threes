from Display import *
from Play import *
from TilesAcces import *
from user_entries import *
from random import *

def get_nb_empty_rooms(plateau):
    i = 0
    compteur = 0
    while i < 16:
        if is_room_empty(plateau, i // 4, i % 4) == True:
            compteur += 1
        i += 1
    plateau['nb_cases_libres'] = compteur

def get_next_alea_tiles(plateau, mode):
    i = 0
    temp = -1
    if mode == 'init':
        while i < 2:
            get_nb_empty_rooms(plateau)
            temp = choice([j for j in range(0, plateau['nb_cases_libres'] - 1) if j not in [temp]])
            plateau['tiles'][temp] = i + 1
            i += 1
    j = 0
    if mode == 'encours':
        get_nb_empty_rooms(plateau)
        temp = randint(0, plateau['nb_cases_libres'] - 1)
        while j < temp:
            if plateau['tiles'][i] == 0:
                j += 1
            i += 1
        plateau['tiles'][i - 1] = randint(1, 3)

def line_pack(plateau, num_lig, sens):
    if sens == 1:
        i = 0
        while i < 3:
            if plateau['tiles'][i + 4 * num_lig] == 0 and plateau['tiles'][i + 1 + 4 * num_lig] != 0:
                plateau['tiles'][i + 4 * num_lig] = plateau['tiles'][i + 1 + 4 * num_lig]
                plateau['tiles'][i + 1 + 4 * num_lig] = 0
            elif (plateau['tiles'][i + 4 * num_lig] == 1 and plateau['tiles'][i + 1 + 4 * num_lig] == 2) or (plateau['tiles'][i + 4 * num_lig] == 2 and plateau['tiles'][i + 1 + 4 * num_lig] == 1):
                plateau['tiles'][i + 4 * num_lig] = 3
                plateau['tiles'][i + 1 + 4 * num_lig] = 0
            elif (plateau['tiles'][i + 4 * num_lig] != 0 and plateau['tiles'][i + 4 * num_lig] == plateau['tiles'][i + 1 + 4 * num_lig]) and (plateau['tiles'][i + 4 * num_lig] != 1 and plateau['tiles'][i + 4 * num_lig] != 2):
                plateau['tiles'][i + 4 * num_lig] = plateau['tiles'][i + 4 * num_lig] * 2
                plateau['tiles'][i + 1 + 4 * num_lig] = 0
            i += 1
    elif sens == 0:
        i = 3
        while i > 0:
            if plateau['tiles'][i + 4 * num_lig] == 0 and plateau['tiles'][i - 1 + 4 * num_lig] != 0:
                plateau['tiles'][i + 4 * num_lig] = plateau['tiles'][i - 1 + 4 * num_lig]
                plateau['tiles'][i - 1 + 4 * num_lig] = 0
            elif (plateau['tiles'][i + 4 * num_lig] == 1 and plateau['tiles'][i - 1 + 4 * num_lig] == 2) or (plateau['tiles'][i + 4 * num_lig] == 2 and plateau['tiles'][i - 1 + 4 * num_lig] == 1):
                plateau['tiles'][i + 4 * num_lig] = 3
                plateau['tiles'][i - 1 + 4 * num_lig] = 0
            elif (plateau['tiles'][i + 4 * num_lig] != 0 and plateau['tiles'][i + 4 * num_lig] == plateau['tiles'][i - 1 + 4 * num_lig]) and (plateau['tiles'][i + 4 * num_lig] != 1 and plateau['tiles'][i + 4 * num_lig] != 2):
                plateau['tiles'][i + 4 * num_lig] = plateau['tiles'][i + 4 * num_lig] * 2
                plateau['tiles'][i - 1 + 4 * num_lig] = 0
            i -= 1

def column_pack(plateau, num_col, sens):
    if sens == 1:
        i = 0
        while i < 3:
            if plateau['tiles'][num_col + 4 * i] == 0 and plateau['tiles'][num_col + 4 + 4 * i] != 0:
                plateau['tiles'][num_col + 4 * i] = plateau['tiles'][num_col + 4 + 4 * i]
                plateau['tiles'][num_col + 4 + 4 * i] = 0
            elif (plateau['tiles'][num_col + 4 * i] == 1 and plateau['tiles'][num_col + 4 + 4 * i] == 2) or (plateau['tiles'][num_col + 4 * i] == 2 and plateau['tiles'][num_col + 4 + 4 * i] == 1):
                plateau['tiles'][num_col + 4 * i] = 3
                plateau['tiles'][num_col + 4 + 4 * i] = 0
            elif (plateau['tiles'][num_col + 4 * i] != 0 and plateau['tiles'][num_col + 4 * i] == plateau['tiles'][num_col + 4 + 4 * i]) and (plateau['tiles'][num_col + 4 * i] != 1 and plateau['tiles'][num_col + 4 * i] != 2):
                plateau['tiles'][num_col + 4 * i] = plateau['tiles'][num_col + 4 * i] * 2
                plateau['tiles'][num_col + 4 + 4 * i] = 0
            i += 1
    elif sens == 0:
        i = 3
        while i > 0:
            if plateau['tiles'][num_col + 4 * i] == 0 and plateau['tiles'][num_col - 4 + 4 * i] != 0:
                plateau['tiles'][num_col + 4 * i] = plateau['tiles'][num_col - 4 + 4 * i]
                plateau['tiles'][num_col - 4 + 4 * i] = 0
            elif (plateau['tiles'][num_col + 4 * i] == 1 and plateau['tiles'][num_col - 4 + 4 * i] == 2) or (plateau['tiles'][num_col + 4 * i] == 2 and plateau['tiles'][num_col - 4 + 4 * i] == 1):
                plateau['tiles'][num_col + 4 * i] = 3
                plateau['tiles'][num_col - 4 + 4 * i] = 0
            elif (plateau['tiles'][num_col + 4 * i] != 0 and plateau['tiles'][num_col + 4 * i] == plateau['tiles'][num_col - 4 + 4 * i]) and (plateau['tiles'][num_col + 4 * i] != 1 and plateau['tiles'][num_col + 4 * i] != 2):
                plateau['tiles'][num_col + 4 * i] = plateau['tiles'][num_col + 4 * i] * 2
                plateau['tiles'][num_col - 4 + 4 * i] = 0
            i -= 1

def lines_pack(plateau, sens):
    i = 0
    while i < 4:
        line_pack(plateau, i, sens)
        i += 1

def columns_pack(plateau, sens):
    i = 0
    while i < 4:
        column_pack(plateau, i, sens)
        i += 1

def play_move(plateau, sens):
    if sens == 'z':
        columns_pack(plateau, 1)
    elif sens == 's':
        columns_pack(plateau, 0)
    elif sens == 'q':
        lines_pack(plateau, 1)
    elif sens == 'd':
        lines_pack(plateau, 0)
