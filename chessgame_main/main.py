#TODO SCHACHFELD Falschrum
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
    __logic_gamefield = Field()
    __file_usage = ChessStorage()
    __file_usage.log("test", "Hallo du Nudel", False)
    __printed_gamefield = UIutil.fill_default_game()
    __run_game = True
    while __run_game:
        __printed_gamefield = UIutil.fill_default_game()
        __printed_gamefield = UIutil.fill_game_field(__logic_gamefield.get_field(), __printed_gamefield)
        __print_all(__printed_gamefield)

        # __testarray = __printed_gamefield
        # for i in range(8):
        #     for j in range(8):
        #         __testarray[i][j] = "B"


        # __file_usage.log("game1", __printed_gamefield, True)
        # __file_usage.log("game1", "________________________________________________________________________", True)

        __run_game = __get_input(__printed_gamefield, __logic_gamefield)

def __print_all(printed_gamefield):
    CLEAR()
    __print_menu()
    __print_game(printed_gamefield)
    __print_footer()

def __print_menu():
    print("\n\t\t\t\t\t\tSchachautomat\t\t")
    print("\n\t\tNeues Spiel(N)\t\tSpeichern(S)\tLaden(L)\t\tSpiel Beenden(B)")
    print("\t\t________________________________________________________________________________")

def __print_footer():
    print("\t\t________________________________________________________________________________")

def __print_game(printed_gamefield):
    print("\n\t\t\t\t\033[6;34;47m    A    B    C    D    E    F    G    H\033[0;30;47m\n")
    for i in range(8):
        __print_game_line(printed_gamefield, i)
    print("\n\t\t\t\t\033[6;34;47m    A    B    C    D    E    F    G    H\033[0;30;47m\n")

def __print_game_line(printed_gamefield, line_number):
    print("\t\t\t       ", end="")
    print('\033[6;34;47m'+str(8-line_number)+"", end="\033[0;30;47m")
    for i in range(8):
        print("    "+str(printed_gamefield[line_number][i])+"", end="")
    print("     \033[6;34;47m"+str(8-line_number), end="\033[0;30;47m\n")

def __get_input(printed_gamefield, logic_gamefield):
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
        __pos = Position(str(list(desiccion)[0]), int(list(desiccion)[1]))
        return __turn(__pos, printed_gamefield, logic_gamefield)
    else:
        return True

def __turn(selceted_position, printed_gamefield, logic_gamefield):
    row = ord(selceted_position.get_pos_char()) - 65
    print_col = 8 - selceted_position.get_pos_number()
    printed_gamefield[print_col][row] = '\033[3;32;47m'+ str(printed_gamefield[(print_col)][row])+"\033[0;30;47m"
    #TODO Spohn einbinden
    # Aufruf get_possiblemoves
    # moves = getpossiblemoves(row.col)

    #Beispielcode kann entfernt werden nach Implementierung
    __moves = logic_gamefield.get_possible_moves(selceted_position)

    #
    for move in __moves: #TODO mögliche Bewewgung anzeigen von Spielfeld (Tobias Spohn)
        move_row = ord(move.get_pos_char()) - 65
        move_col = 8 - move.get_pos_number()
        printed_gamefield[move_col][move_row] = '\033[0;31;47m'+ str(printed_gamefield[move_col][move_row])+"\033[0;30;47m"
    __print_all(printed_gamefield)
    #TODO SAHRA###################################################################################################################################
    # Computer Gegener Einbauen stattdessen#
    __next_move = __get_input_move(__moves)
    ###############################################################################################################################################
    logic_gamefield.do_move(selceted_position, __next_move)
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
    __move = str.upper(__move)
    __move_pos = Position(str(list(__move)[0]), int(list(__move)[1]))
    return __move_pos

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
    