def get_user_move():
    move = ''
    while move.lower() != 'm' and move.lower() != 'z' and move.lower() != 'q' and move.lower() != 's' and move.lower() != 'd':
        print("Directions: z, q, s ,d   Menu: m")
        move = input()
    return move.lower()

def get_user_menu(plateau):
    choix = ''
    while choix.upper() != 'N' and choix.upper() != 'L' and choix.upper() != 'S' and choix.upper() != 'Q':
        print("N: New game, L: Load game, S: Save game, C: Continue game, Q: Quit game")
        choix = input()
        if choix.upper() == 'C':
            if plateau == None:
                print("No game in progress")
            else:
                return 'C'
    return choix.upper()
