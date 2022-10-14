from Display import *
from Play import *
from TilesAcces import *
from TilesMoves import *
from user_entries import *

p = init_play()
assert p == {'n' : 4, 'nb_cases_libres' : 16, 'tiles' : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]}
print("init_play_ok")

p = init_play()
assert check_indice(p, 0) == True
assert check_indice(p, 10) == False
assert check_indice(p, 3) == True
assert check_indice(p, 4) == False
assert check_indice(p, -1) == False
print("check_indice_ok")

p = init_play()
assert check_room(p, 2, 1) == True
assert check_room(p, 10, 2) == False
assert check_room(p, -1, 3) == False
assert check_room(p, 3, 3) == True
print("check_room_ok")

p = {'n' : 4, 'nb_cases_libres' : 6, 'tiles' : [6, 2, 3, 2, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0,]}
assert get_value(p, 0, 0) == 6
assert get_value(p, 2, 3) == 0
assert get_value(p, 1, 3) == 2
assert get_value(p, 3, 0) == 1
print("get_value_ok")

p = init_play()
set_value(p, 0, 0, 1)
assert p == {'n': 4, 'nb_cases_libres': 16, 'tiles': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
set_value(p, 1, 2, 0)
assert p == {'n': 4, 'nb_cases_libres': 16, 'tiles': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
set_value(p, 2, 3, 6)
assert p == {'n': 4, 'nb_cases_libres': 16, 'tiles': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0]}
assert set_value(p, 18, 3, 1) == 'Error'
print("set_value_ok")

assert is_room_empty(p, 1, 1) == False
assert is_room_empty(p, 3, 2) == True
print("is_room_empty_ok")

p = {'n' : 4, 'nb_cases_libres' : 5, 'tiles' : [6, 2, 3, 2, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0,]}
get_nb_empty_rooms(p)
assert p['nb_cases_libres'] == 6
print("get_nb_empty_rooms_ok")

p = {'n' : 4, 'nb_cases_libres' : 6, 'tiles' : [6, 2, 3, 2, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0,]}
assert is_game_over(p) == False
p = {'n' : 4, 'nb_cases_libres' : 6, 'tiles' : [6, 2, 3, 2, 12, 2, 6, 2, 6, 2, 2, 12, 1, 6, 3, 1,]}
assert is_game_over(p) == True
print("is_game_over_ok")

p = {'n' : 4, 'nb_cases_libres' : 6, 'tiles' : [6, 2, 3, 2, 6, 2, 12, 2, 2, 2, 2, 1, 1, 6, 1, 12,]}
assert get_scores(p) == 62
p = {'n' : 4, 'nb_cases_libres' : 6, 'tiles' : [6, 2, 3, 12, 6, 2, 12, 2, 2, 3, 2, 1, 1, 6, 1, 12,]}
assert get_scores(p) == 73
print("get_scores_ok")
