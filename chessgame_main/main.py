"""[summary]

Returns:
    [type] -- [description]
"""
import platform
import os
# from colorama import Fore, Back
# import consts
try:
    import consts
    from util import UIutil
    #
    from chess_storage.chess_storage import ChessStorage
    #
    from chess_logik.position import Position
    from chess_logik.field import Field
except ImportError:
    print("Import Error!")
    exit()


def main():
    """[summary]
    """
    #TODO Frank docstring
    __gamefield = UIutil.fill_default_game()
    # Fliegt raus nach Implementierung
    # for k in range(8):
    #     __gamefield[1][k] = "♙"
    #     __gamefield[6][k] = "♟"
    # Fliegt raus nach Implementierung

    __run_game = True
    while __run_game:
        __print_all(__gamefield)
        __run_game = __get_input(__gamefield)

def __print_all(gamefield):
    CLEAR()
    __print_menu()
    __print_game(gamefield)
    __print_footer()

def __print_menu():
    print("\n\t\t\t\t\t\tSchachautomat\t\t")
    print("\n\t\tNeues Spiel(N)\t\tSpeichern(S)\tLaden(L)\t\tSpiel Beenden(B)")
    print("\t\t________________________________________________________________________________")

def __print_footer():
    print("\t\t________________________________________________________________________________")

def __print_game(gamefield):
    print("\n\t\t\t\t\033[6;34;47m    A    B    C    D    E    F    G    H\033[0;30;47m\n")
    for i in range(8):
        __print_game_line(gamefield, i)
    print("\n\t\t\t\t\033[6;34;47m    A    B    C    D    E    F    G    H\033[0;30;47m\n")

def __print_game_line(gamefield, line_number):
    print("\t\t\t       ", end="")
    print('\033[6;34;47m'+str(8-line_number)+"", end="\033[0;30;47m")
    for i in range(8):
        print("    "+str(gamefield[line_number][i])+"", end="")
    print("     \033[6;34;47m"+str(8-line_number), end="\033[0;30;47m\n")

def __get_input(gamefield):
    print("\t\t\t\tBitte Menü Aktion eingeben oder Bauer wählen")
    desiccion = input("\t\t\t\t")
    desiccion = str.upper(desiccion)
    #TODO falsche Eingabe Abfangen
    if desiccion == consts.LOAD:
        print("\t\t\t\tSpiel Laden")
        #TODO Spiel Laden einbauen
        return True
    elif desiccion == consts.SAVE:
        print("\t\t\t\tSpiel Speichern ...")
        #TODO Spiel Speichern einbauen
        return True
    elif desiccion == consts.NEW_GAME:
        print("\t\t\t\tNeues Spiel")
        #TODO Neues Spiel einbaune
        return True
    elif desiccion == consts.QUIT:
        return __quit_game()
    elif len(desiccion) == 2:
        #TODO Abfangen von Falsch eingaben
        __letter = str(list(desiccion)[0])
        __number = int(list(desiccion)[1])-1
        return __turn(__letter, __number, gamefield)
    else:
        return True

def __turn(letter, number, gamefield):
    row = ord(letter) - 65
    col = number
    gamefield[col][row] = '\033[3;32;47m'+ str(gamefield[col][row])+"\033[0;30;47m"
    #TODO Spohn einbinden
    # Aufruf get_possiblemoves
    # moves = getpossiblemoves(row.col)

    #Beispielcode kann entfernt werden nach Implementierung
    __moves = []
    __moves.append(Position('H', 2))
    __moves.append(Position('A', 1))
    __moves.append(Position('G', 7))
    #
    for move in __moves: #TODO mögliche Bewewgung anzeigen von Spielfeld (Tobias Spohn)
        move_row = ord(move.get_pos_char()) - 65
        move_col = move.get_pos_number()
        gamefield[move_col][move_row] = '\033[4;31;47m'+ str(gamefield[move_col][move_row])+"\033[0;30;47m"
    __print_all(gamefield)
    __next_move = __get_input_move(__moves)
    #TODO Spoh einbinden
    #spielplan = domove(__nextmove)
    #gamefield = gamefield #spielfeld do turn
    return True

def __get_input_move(posible_moves):
    print("\t\t\t\tBitte einen der folgenden Züge auswählen:")
    print("\t\t\t\t\t", end="\033[0;31;47m")
    for move in posible_moves:
        print(""+str(move.get_pos_char())+""+str(move.get_pos_number())+"", end="\t")
    __move = input("\033[0;30;47m\n\t\t\t\t")
    return __move

def __quit_game():
    CLEAR()
    os.system('color 0F')
    return False

if platform.system() == "Windows":
    CLEAR = lambda: os.system("cls")
    os.system('color F0')
elif platform.system() == "Linux":
    CLEAR = lambda: os.system('clear')
    os.system('setterm -background white -foreground white -store')

if __name__ == "__main__":
    main()
    