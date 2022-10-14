from Display import *
from Jeu import *
from TilesAcces import *
from TilesMoves import *
from user_entries import *
import json

def init_play():
    plateau = {'n' : 4, 'nb_cases_libres' : 16, 'tiles' : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]}
    return plateau

def is_game_over(plateau):
    get_nb_empty_rooms(plateau)
    if plateau['nb_cases_libres'] == 0:
        return True
    else:
        return False

def get_scores(plateau):
    i = 0
    temp = plateau['tiles']
    score = 0
    while i < 16:
        score += temp[i]
        i += 1
    return score

def create_new_play():
    plateau = init_play()
    get_next_alea_tiles(plateau, 'init')
    play = {'plateau': plateau, 'score': get_scores(plateau)}
    return play

def cycle_play(plateau):
    if plateau == None:
        plateau = init_play()
        get_next_alea_tiles(plateau, 'init')
    while is_game_over(plateau) == False:
        medium_display(plateau)
        score = get_scores(plateau)
        print("Score = ", score)
        move = get_user_move()
        if move == 'm':
            return plateau
        play_move(plateau, move)
        get_next_alea_tiles(plateau, 'encours')
    print("Game Over")
    print("Score = ", get_scores(plateau))
    plateau = None
    return plateau

def save_game(plateau):

	datas = plateau
	with open("saved_game.json","W") as f_write:
		json.dump(datas,f_write)

def load_game(plateau):

	with open("saved_game.json","r") as f_read:
		plateau = json.load(datas,f_read)
