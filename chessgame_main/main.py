"""[summary]

Returns:
    [type] -- [description]
"""
import platform
import os
import sys

# from colorama import Fore, Back
# import consts
try:
    import consts
    from game import ActiveGame
    from chess_storage.chess_storage import ChessStorage
except ImportError:
    print("Import Error!")
    sys.exit()


def main():
    """[summary]
    """
    #TODO Frank docstring
    
    storage = ChessStorage()
    start_game = __print_welcome_screen()
    CLEAR()
    while consts.FOREVER:
        if(start_game == consts.NEW_GAME):
            __active_game = __set_new_game(storage)
            start_game = consts.RUN_GAME
        elif start_game == consts.LOAD:
            __games = storage.get_all_games()
            __game_load_name = __get_load_game(__games)
            __active_game = storage.load_data(__game_load_name)
            start_game = consts.RUN_GAME
        elif start_game == consts.RUN_GAME:
            __game_run = True
            while __game_run:
                CLEAR()
                __game_result = __active_game.run_game()
                if not isinstance(__game_result, bool):
                    if __game_result == consts.QUIT:
                        start_game = consts.HOME
                        break
                    elif __game_result == consts.SAVE:
                        storage.save_
                        data(__active_game.get_game_name(), __active_game, True)
        elif start_game == consts.QUIT:
            __quit_game()
            break
        elif start_game == consts.HOME:
            start_game = __print_welcome_screen()
    # __run_game = True
    # while __run_game:
    #    

def __print_welcome_screen():
    """[Starts the Game]
    
    Returns:
        [string] -- [
            const.QUIT
            const.NEW_Game
            cons.LOAD_GAME
            ]
    """
    CLEAR()
    print("\n\t\t\t\t\t\tSchachautomat\t\t")
    print("\t\t________________________________________________________________________________\n")
    print("\t\t\t\t\t        Neues Spiel(N)\t\t")
    print("\t\t\t\t\t        Spiel Laden(L)\t\t")
    print("\t\t\t\t\t        Beenden(B)\t\t")
    print("\n\t\t________________________________________________________________________________")
    while(consts.FOREVER):
        __input = str.upper(input("\n\t\t\t\t\t\tWas möchten sie tun: "))
        if __input == "N":
            return consts.NEW_GAME
        elif __input == "L":
            return consts.LOAD
        elif __input == "B":
            return consts.QUIT
        else:
            print("\n\t\t\t\t\t\t\033[0;31;47mFalsche eingabe !\033[0;30;47m")

def __get_load_game(games):
    CLEAR()
    print("\n\t\t\t\t\t\tSchachautomat\t\t")
    print("\t\t________________________________________________________________________________\n")
    print("\n\t\t\t\t\t\tSpiele zum laden\t\t")
    i = 0
    for game in games:
        i += 1
        print("\t\t\t\t\t\t("+str(i)+")\t"+game)
    print("\t\t________________________________________________________________________________\n")
    
    decision = ""
    while not isinstance(decision, int):
        decision = input("\t\t\t\t\t\tBitte Spiel wählen : ")
        decision = int(decision)
    return games[decision-1]



def __set_new_game(storage):
    print("\n\t\t\t\t\t\tSchachautomat\t\t")
    print("\t\t________________________________________________________________________________\n")

    while consts.FOREVER:
        __play_against_bot = str.upper(input("\t\t\t\t\t\tWollen sie gegen den Computer Spielen (J/N) :\n\t\t\t\t\t\t"))
        if __play_against_bot == "J":
            __play_against_bot = True
        elif __play_against_bot == "N":
            __play_against_bot = False
        if not isinstance(__play_against_bot, bool):
            print("\t\t\t\t\t\t\033[0;31;47mFalsche eingabe bitte erneut Versuchen\033[0;30;47m")
        else:
            break
        #
    __game_name = str(input("\t\t\t\t\t\tBitte Spielname eingeben :\n\t\t\t\t\t\t"))
    __playername_one = str(input("\t\t\t\t\t\tBitte Spieler Name 1 :\n\t\t\t\t\t\t"))
    if not __play_against_bot:
        __playername_two = str(input("\t\t\t\t\t\tBitte Spieler Name 2 :\n\t\t\t\t\t\t"))
        return ActiveGame(__playername_one, __playername_two, __game_name, False, storage)
    return ActiveGame(__playername_one, "Computergegner", __game_name, True, storage)


    

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
    