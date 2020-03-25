"""[summary]

Returns:
    [type] -- [description]
"""
import platform
import os
# from colorama import Fore, Back
try:
    import consts
except ImportError:
    print("Import Error!")
    exit()

def main():
    """[summary]
    """
    #TODO Frank docstring
    __gamefield = __fill_default_game()
    for k in range(8):
        __gamefield[1][k] = "♙"
        __gamefield[6][k] = "♟"

    __run_game = True
    while __run_game:
        CLEAR()
        __print_menu()
        __print_game(__gamefield)
        __print_footer()
        __run_game = __get_input(__gamefield)

def __fill_default_game():
    gamefield = [[0 for i in range(consts.GAME_SIZE)] for j in range(consts.GAME_SIZE)]
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:
                    gamefield[i][j] = "◼"
                else:
                    gamefield[i][j] = "◻"
            else:
                if j % 2 == 0:
                    gamefield[i][j] = "◻"
                else:
                    gamefield[i][j] = "◼"
    return gamefield

def __print_menu():
    print("\t\tNeues Spiel(N)\t\tSpeichern(S)\tLaden(L)\t\tSpiel Beenden(B)")
    print("\t\t________________________________________________________________________________")

def __print_footer():
    print("\t\t________________________________________________________________________________")

def __print_game(gamefield):
    print("\n\t\t\t\t    A    B    C    D    E    F    G    H\n")
    for i in range(8):
        __print_game_line(gamefield, i)
   
    print("\n\t\t\t\t    A    B    C    D    E    F    G    H")

def __print_game_line(gamefield, line_number):
    print("\t\t\t       ", end="")
    print(str(line_number+1)+"", end="")
    for i in range(8):
        print("    "+str(gamefield[line_number][i])+"", end="")
    print("     "+str(line_number+1))

def __get_input(gamefield):
    print("\t\t\t\tBitte Menü Aktion eingeben oder Bauer wählen")
    desiccion = input("\t\t\t\t")
    desiccion = str.upper(desiccion)

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
        __letter = str.upper(list(desiccion)[0])
        __number = int(list(desiccion)[1])-1
        return __move_figure(__letter, __number, gamefield)

    else:
        return True

def __move_figure(letter, number, gamefield):
    row = ord(letter) - 65
    col = number
    gamefield[col][row] = '\033[3;32;47m'+ str(gamefield[col][row])+"\033[0;30;47m"
    
    # for move in moves: #TODO Possible moves from figures
        
        

    return True
    

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
    