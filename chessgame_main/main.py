"""[summary]

Returns:
    [type] -- [description]
"""
###############################################################################################################################################################
#       Chess main                                                                                                   Author: Frank Rübenkönig                 #
#                                                                                                                    Date:   03.04.2020                       #
#                                                                                                                    Version: V1.00                           #
###############################################################################################################################################################
#
try:
    import platform
    import os
    import sys
    import consts
    from game import ActiveGame
    from computer_gegner.opponent_move import Opponent
    from chess_storage.chess_storage import ChessStorage
except ImportError:
    print("Import Error!")
    sys.exit()
######################################################################## main file ############################################################################
#
def main():
    """Main Method of chess computer
    """
    ####################################################################### main ##############################################################################
    #
    __storage = ChessStorage()
    __start_game = __print_welcome_screen()
    #
    CLEAR()
    #
    while consts.FOREVER:
        if __start_game == consts.GAME_MODE["NEW_GAME"]:
            __active_game = __set_new_game(__storage)
            __start_game = consts.GAME_MODE["RUN_GAME"]
        elif __start_game == consts.GAME_MODE["LOAD"]:
            __games = __storage.get_all_games()
            __game_load_name = __get_load_game(__games)
            __active_game = __storage.load_data(__game_load_name)
            __start_game = consts.GAME_MODE["RUN_GAME"]
        elif __start_game == consts.GAME_MODE["RUN_GAME"]:
            __game_run = True
            while __game_run:
                CLEAR()
                __game_result = __active_game.run_game()
                if not isinstance(__game_result, bool):
                    if __game_result == consts.GAME_MODE["QUIT"]:
                        __check_game_saved(__active_game, __storage)
                        __start_game = consts.GAME_MODE["HOME"]
                        break
                    elif __game_result == consts.GAME_MODE["SAVE"]:
                        __check_game_saved(__active_game, __storage)
                    elif __game_result == consts.GAME_MODE["LOAD"]:
                        __start_game = consts.GAME_MODE["LOAD"]
                        __check_game_saved(__active_game, __storage)
                        break
                    elif __game_result == consts.GAME_MODE["NEW_GAME"]:
                        __start_game = __check_new_game(__active_game, __storage)
                        break
        elif __start_game == consts.GAME_MODE["RESET"]:
            __game_name = __active_game.get_game_name()+"("+str(1)+")"
            __playername_one = __active_game.get_playername_one()
            __playername_two = __active_game.get_playername_two()
            __play_against_bot = __active_game.get_play_against_bot()
            #
            __active_game = ActiveGame(__playername_one, __playername_two, __game_name, __play_against_bot, __storage)
            __start_game = consts.GAME_MODE["RUN_GAME"]
        elif __start_game == consts.GAME_MODE["QUIT"]:
            __quit_game()
            break
        elif __start_game == consts.GAME_MODE["HOME"]:
            __start_game = __print_welcome_screen()
    #
    ####################################################################### End: main #########################################################################
#
#
def __print_welcome_screen():
    """prints The welcome screen and aks for options
    Returns:
        const.GAME_MODE["NEW_GAME"] -- stars a new Game
        const.GAME_MODE["LOAD"] -- stars a new Game
        const.GAME_MODE["QUIT"] -- stars a new Game
    """
    #################################################################### __print_welcome_screen ###############################################################
    #
    CLEAR()
    print("\n\t\t\t\t\t\tSchachautomat\t\t")
    print("\t\t________________________________________________________________________________\n")
    print("\t\t\t\t\t        Neues Spiel(N)\t\t")
    print("\t\t\t\t\t        Spiel Laden(L)\t\t")
    print("\t\t\t\t\t        Beenden(B)\t\t")
    print("\n\t\t________________________________________________________________________________")
    #
    while consts.FOREVER:
        __input = str.upper(input("\n\t\t\t\t\t\tWas möchten sie tun: "))
        if __input == "N":
            return consts.GAME_MODE["NEW_GAME"]
        elif __input == "L":
            return consts.GAME_MODE["LOAD"]
        elif __input == "B":
            return consts.GAME_MODE["QUIT"]
        else:
            print("\n\t\t\t\t\t\t\033[0;31;47mFalsche eingabe !\033[0;30;47m")
    #
    #################################################################### End: __print_welcome_screen ##########################################################
#
#
def __get_load_game(games):
    """Aks user to load game and returns the game
    Returns:
        string -- Name of the game wich should be load
    """
    ################################################################### __get_load_game #######################################################################
    #
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
    #
    ################################################################### End: __get_load_game ##################################################################
#
#
def __check_new_game(game, storage):
    """Check if the user Wants a new Game or a Game Reset
    Arguments:
        storage ChessStorage -- the Instance of ChessStorage to get file access
    Returns:
        consts.GAME_MODE["RESET"] -- User wants to Reset a Game
        consts.GAME_MODE["NEW_GAME"] -- User wants to start a new Game
    """
    ############################################################## __check_new_game ###########################################################################
    #
    if game.get_game_name() in storage.get_all_games():
        CLEAR()
        print("\n\t\t\t\t\t\tSchachautomat\t\t")
        print("\t\t________________________________________________________________________________\n")
        print("\t\t\t\t\t\tSpiel "+game.get_game_name()+" existiert bereits\n")
        print("\t\t\t\t\t\tSpiel Was möchten sie tun\n")
        print("\t\t\t\t\t\t(1)\tNochmal Spielen\n")
        print("\t\t\t\t\t\t(2)\tNeues Spiel Starten\n")
        __decision = int(input())
        while consts.FOREVER:
            if __decision == 1:
                return consts.GAME_MODE["RESET"]
            elif __decision == 2:
                return consts.GAME_MODE["NEW_GAME"]
            else:
                print("Falsche eingabe")
    return consts.GAME_MODE["RESET"]
    #
    ############################################################ End: __check_new_game ########################################################################
#
#
def __check_game_saved(game, storage):
    """Check if game is saved and saves the game by user input
    Arguments:
        storage ChessStorage -- the Instance of ChessStorage to get file access
    """
    ################################################################# __check_game_saved ######################################################################
    #
    if not game.get_game_name() in storage.get_all_games():
        print("\t\t\t\t\tSpiel wurde noch nicht gepspeichert")
        print("\t\t\t\t\t("+consts.GAME_MODE["SAVE"]+")\tSpiel Speichern")
        print("\t\t\t\t\t("+consts.GAME_MODE["QUIT"]+")\tohne Speichern fortfahren")
    else:
        print("\t\t\t\t\tSpiel wurde bereits gespeichert\n\t\t\t\t\tSoll der Spielstand überschrieben werden")
        print("\t\t\t\t\t("+consts.GAME_MODE["SAVE"]+")\tSpiel Überschreiben")
        print("\t\t\t\t\t("+consts.GAME_MODE["SAVE_NEW"]+")\tSpiel Überschreiben")
        print("\t\t\t\t\t("+consts.GAME_MODE["QUIT"]+")\tohne Speichern fortfahren")
    decision = ""
    while decision not in [consts.GAME_MODE["SAVE"], consts.GAME_MODE["SAVE_NEW"], consts.GAME_MODE["QUIT"]]:
        decision = str.upper(input("\t\t\t\t\t"))
    if decision == consts.GAME_MODE["SAVE"]:
        storage.save_data(game.get_game_name(), game, True, False)
    elif decision == consts.GAME_MODE["SAVE_NEW"]:
        storage.save_data(game.get_game_name(), game, False, True)
    #
    ################################################################# __check_game_saved ######################################################################
#
#
def __set_new_game(storage):
    """GEt Infos for a new game and returns them
    Returns:
        ActiveGame -- a new instance with all entered Informantions
    """
    #################################################################### __set_new_game #######################################################################
    #
    CLEAR()
    print("\n\t\t\t\t\t\tSchachautomat\t\t")
    print("\t\t________________________________________________________________________________\n")
    #
    while consts.FOREVER:
        __play_against_bot = str.upper(input("\t\t\t\t\t\tWollen sie gegen den Computer Spielen (J/N) :\n\t\t\t\t\t\t"))
        if __play_against_bot == "J":
            __play_against_bot = True
            __bot = Opponent()
        elif __play_against_bot == "N":
            __play_against_bot = False
        if not isinstance(__play_against_bot, bool):
            print("\t\t\t\t\t\t\033[0;31;47mFalsche eingabe bitte erneut Versuchen\033[0;30;47m")
        else:
            break
        #
    #
    __game_name = str(input("\t\t\t\t\t\tBitte Spielname eingeben :\n\t\t\t\t\t\t"))
    __playername_one = str(input("\t\t\t\t\t\tBitte Spieler Name 1 :\n\t\t\t\t\t\t"))
    if not __play_against_bot:
        __playername_two = str(input("\t\t\t\t\t\tBitte Spieler Name 2 :\n\t\t\t\t\t\t"))
        return ActiveGame(__playername_one, __playername_two, __game_name, __bot, storage)
    return ActiveGame(__playername_one, "Computergegner", __game_name, __bot, storage,)
    #
    #################################################################### End: __set_new_game ##################################################################
#
#
def __quit_game():
    """Quits the game
    Returns:
        bool -- every time False to Exit game
    """
    ################################################################## __quit_game ############################################################################
    #
    CLEAR()
    os.system('color 0F')
    return False
    #
    ################################################################## End: __quit_game #######################################################################
#
#
if platform.system() == "Windows":
    CLEAR = lambda: os.system("cls")
    os.system('color F0')
elif platform.system() == "Linux":
    CLEAR = lambda: os.system('clear')
    os.system('setterm -background white -foreground white -store')
#
if __name__ == "__main__":
    main()
#
######################################################################## End: main file #######################################################################
    