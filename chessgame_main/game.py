"""Contains the class ActiveGame wich contains all functions to run a chessgame
"""
import sys
import time
try:
    import consts
    from chess_logik.position import Position
    from chess_logik import consts as game_consts
    from chess_logik.field import Field
except ImportError:
    print("Import Error!")
    sys.exit()

class ActiveGame:
    """Instance of an ActiveGame with all its functionallity
    """
    ######################################################################### ActiveGame ######################################################################
    #
    def __init__(self, playername_one, playername_two, gamename, bot, storage):
        """Inits a new game with all its parameters
        Arguments:
            playername_one {[string]} -- [Name of Player 1]
            playername_two {[string]} -- [Name of Player 2]
            gamename {[string]} -- [Game Name for Save and Log FileArguments]
            bot {[Opponent]} -- [Instance of the Opponent if needed]
            storage {[ChessStorage]} --[Instance of storage class to log and save game]
        """
        ############################################################# __init__ ################################################################################
        #
        assert isinstance(playername_one, str), "playername_one ist nicht vom typ string"
        assert isinstance(playername_two, str), "playername_two ist nicht vom typ string"
        assert isinstance(gamename, str), "gamename ist nicht vom typ string"
        assert storage is not None, "Kein storage übegeben"
        self.__info_text = ""
        self.__error_text = ""
        self.__active_player = consts.COLOR_WHITE
        self.__storage = storage
        self.__playername_one = playername_one
        self.__playername_two = playername_two
        self.__gamename = gamename
        self.__bot = bot
        self.__successfull_turn = False
        self.__logic_gamefield = Field()
        self.__printed_gamefield = self.__fill_default_game()
        self.__printed_gamefield = self.__fill_game_field()
        self.__storage.log(self.__gamename, "\t\t\t Neues Spiel erstellt "+gamename, True)
        #
        ############################################################# End: __init__ ###########################################################################
    #
    #
    def run_game(self):
        """Runs the actual game
        Returns:
            GAME_MODE["LOAD"] -- Load new Game
            GAME_MODE["RUN_GAME"] -- Game not finished need to run again
            GAME_MODE["RESET"] -- Reset game to default falue
            GAME_MODE["SAVE"] -- Save Game
            GAME_MODE["QUIT"] -- Quit Game
            GAME_MODE["NEW_GAME"] -- User wants a new Game
            GAME_MODE["HOME"] -- Go Back to Home Screen
        """
        ######################################################################## run_game #####################################################################
        #
        if self.__active_player == consts.COLOR_WHITE:
            self.__info_text = "\033[0;30;47m "+self.__playername_one+" ist an der Reihe\033[0;30;47m"
        elif self.__active_player == consts.COLOR_BLACK:
            self.__info_text = "\033[0;37;40m "+self.__playername_two+" ist an der Reihe\033[0;30;47m"
        #
        #
        self.__update_game()
        #
        #
        if self.__successfull_turn:
            self.__storage.log(self.__gamename, "________________________________________________________________________________", True)
            self.__storage.log(self.__gamename, self.__printed_gamefield, True)
            self.__storage.log(self.__gamename, "________________________________________________________________________________", True)
            self.__successfull_turn = False
        elif len(str.split(self.__error_text, "__")) == 3:
            self.__storage.log(self.__gamename, str.split(self.__error_text, "__")[1], True)
        #
        #
        __run_game = self.__get_input()
        #
        #
        if __run_game == game_consts.WINNER_CODES["NoWinner"]:
            return __run_game
        elif __run_game in game_consts.WINNER_CODES.values():
            if __run_game == game_consts.WINNER_CODES["WhiteWon"]:
                self.__info_text = "\033[0;30;47m "+self.__playername_one+" hat gewonnen\033[0;30;47m"
            else:
                self.__info_text = "\033[0;37;40m "+self.__playername_two+" hat gewonnen\033[0;30;47m"
            self.__update_game()
            str_play_again = consts.GAME_MODE["NEW_GAME"]
            str_quit = consts.GAME_MODE["QUIT"]
            decision = input("\t\t\tWas möchten sie machen Nochmal Spielen ("+str_play_again+") oder Beenden ("+str_quit+")\n\t\t\t")
            return str.upper(decision)
        else:
            return __run_game
        #
        ####################################################################### End: run_game #################################################################
    #
    #
    def __update_game(self):
        """Updates the printed Gamefield and prints the new Version out
        """
        ################################################################# __update_game #######################################################################
        #
        self.__printed_gamefield = self.__fill_default_game()
        self.__printed_gamefield = self.__fill_game_field()
        self.__print_game_all()
        #
        ################################################################# End: __update_game ##################################################################
    #
    #
    def __fill_default_game(self):
        """Fills the printed_gameframe with white and black fields
        to display a default chessgame
        Returns:
            gamefield {String[]} -- New version of the gamefield with filled fields
        """
        ################################################################# __fill_default_game #################################################################
        #
        gamefield = [[0 for i in range(consts.GAME_SIZE)] for j in range(consts.GAME_SIZE)]
        for i in range(8):
            for j in range(8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        gamefield[i][j] = "◻"
                    else:
                        gamefield[i][j] = "◼"
                else:
                    if j % 2 == 0:
                        gamefield[i][j] = "◼"
                    else:
                        gamefield[i][j] = "◻"
        return gamefield
        #
        ################################################################# End: __fill_default_game ############################################################
    #
    #
    def __fill_game_field(self):
        """fills the printed_gamefield with pawns from logic_gamefield
        Arguments:
            logic_gamefield {[field]} -- contains the info from chess_logik.field
            printed_gamefield {[string[][]} -- string array wich represenets the printed chess field
        """
        ################################################################# __fill_game_field ###################################################################
        #
        for actual_pawn in self.__logic_gamefield.get_field():
            __actual_pos = actual_pawn.get_position()
            __actual_color = actual_pawn.get_color()
            __col = ord(__actual_pos.get_pos_char())-65
            __row = 8-__actual_pos.get_pos_number()
            #
            if __actual_color == consts.COLOR_BLACK:
                self.__printed_gamefield[__row][__col] = u"♟"
            elif __actual_color == consts.COLOR_WHITE:
                self.__printed_gamefield[__row][__col] = u"♙"
        #
        return self.__printed_gamefield
        #
        ################################################################# End: __fill_game_field ##############################################################
    #
    #
    def __print_game_all(self):
        """prints the complete game with header and footer
        """
        ################################################################# __print_game_all ####################################################################
        #
        self.__print_menu()
        self.__print_game()
        self.__print_footer()
        #
        ################################################################# End: __print_game_all ###############################################################
    #
    #
    def __print_menu(self):
        """Prints the Header of the game with options
        """
        ########################################################################## __print_menu ###############################################################
        #
        print("\n\t\t\t\t\t\tSchachautomat\t\t")
        print("\n\t\tNeues Spiel(N)\t\tSpeichern(S)\tLaden(L)\t\tSpiel Beenden(B)")
        print("\t\t________________________________________________________________________________")
        #
        #######################################################################################################################################################
    #
    #
    def __print_footer(self):
        """Prints the footer of the game
        """
        ######################################################################### __print_footer ##############################################################
        #
        print("\t\t________________________________________________________________________________")
        #
        ######################################################################### End: __print_footer #########################################################
    #
    #
    def __print_game(self):
        """Print the Chessgame with index and fields
        """
        ################################################################# __print_game ########################################################################
        #
        print("\n\t\t\t\t    A    B    C    D    E    F    G    H\n")
        for i in range(8):
            self.__print_game_line(i)
        print("\n\t\t\t\t    A    B    C    D    E    F    G    H\n")
        #
        ################################################################# End: __print_game ###################################################################
    #
    #
    def __print_game_line(self, line_number):
        """print a single line of the game field
        Arguments:
            line_number {int} -- number of the printed line needed for index
        """
        ################################################################# __print_game_line ###################################################################
        #
        print("\t\t\t       ", end="")
        print('\033[6;34;47m'+str(8-line_number)+"", end="\033[0;30;47m")
        for i in range(8):
            print("    "+str(self.__printed_gamefield[line_number][i])+"", end="")
        if line_number == 3:
            print("    \033[6;34;47m"+str(8-line_number)+"\033[0;30;47m\t\t"+self.__info_text+"", end="\033[0;30;47m\n")
        elif line_number == 4:
            print("    \033[6;34;47m"+str(8-line_number)+"\033[0;30;47m\t\t"+self.__error_text+"", end="\033[0;30;47m\n")
        else:
            print("    \033[6;34;47m"+str(8-line_number), end="\033[0;30;47m\n")
        #
        ################################################################# End: __print_game_line ##############################################################
    #
    #
    def __get_input(self):
        """Requests input from user and runs the needed code
        Returns:
            GAME_MODE["SAVE"] -- User wants to save a game
            GAME_MODE["LOAD"] -- User wants to Load a game
            GAME_MODE["QUIT"] -- User wants to Exit the Runnning game
            GAME_MODE["NEW_GAME"] -- User wants start a new Game
            ________________________________________________________________
            consts.ERROR_CODES["WRONG_INPUT"] -- User has done a wrong input
            ________________________________________________________________
            game_consts.WINNER_CODES["NoWinner"] -- No win Game still running
            game_consts.WINNER_CODES["WhiteWon"] -- White Player is winner
            game_consts.WINNER_CODES["BlackWon"] -- Black Player is winner
        """
        ################################################################## __get_input ########################################################################
        #
        if self.__bot is not None and self.__active_player == game_consts.COLOR_BLACK:
            time.sleep(2)
            __bot_move = self.__bot.bot_move(self.__logic_gamefield.get_field())
            __bot_old_position = Position(list(__bot_move[0])[0], int(list(__bot_move[0])[1]))
            __bot_new_position = Position(list(__bot_move[1])[0], int(list(__bot_move[1])[1]))
            __pos_moves = self.__logic_gamefield.get_possible_moves(__bot_old_position)
            __move_result = self.__logic_gamefield.do_move(__bot_old_position, __bot_new_position)
            self.__storage.log(self.__gamename, "Schwarzer Spieler bewegt Bauer von"+__bot_move[0]+" nach "+__bot_move[1]+"", True)
            self.__active_player = consts.COLOR_WHITE
            self.__print_game_all()
            return self.__logic_gamefield.check_win()
        else:
            print("\t\t\t\tBitte Menü Aktion eingeben oder Bauer wählen")###
            #
            desiccion = input("\t\t\t\t")
            desiccion = str.upper(desiccion)
            if desiccion == consts.GAME_MODE["LOAD"]:
                #
                return consts.GAME_MODE["LOAD"]
                #
            elif desiccion == consts.GAME_MODE["SAVE"]:
                #
                self.__error_text = "\033[0;32;47m__Spiel wurde erfolgreich gespeichert__\033[0;30;47m"
                return consts.GAME_MODE["SAVE"]
                #
            elif desiccion == consts.GAME_MODE["NEW_GAME"]:
                #
                return consts.GAME_MODE["NEW_GAME"]
                #
            elif desiccion == consts.GAME_MODE["QUIT"]:
                #
                return consts.GAME_MODE["QUIT"]
                #
            elif len(desiccion) == 2:
                #
                dec_char = list(desiccion)[0]
                dec_num = list(desiccion)[1]
                if dec_char.isalpha() and dec_num.isnumeric():
                    __pos = Position(str(list(desiccion)[0]), int(list(desiccion)[1]))
                    return self.__turn(__pos)
                else:
                    self.__error_text = "\033[0;31;47m__Falsches zeichen eingegeben__\033[0;30;47m"
                    return consts.ERROR_CODES["WRONG_INPUT"]
                #
            else:
                self.__error_text = "\033[0;31;47m__Falsche eingabe__\033[0;30;47m"
                return consts.ERROR_CODES["WRONG_INPUT"]
        #
        ################################################################### End: __get_input ##################################################################
    #
    #
    def __turn(self, selceted_position):
        """starts a new turn
        Arguments:
            selceted_position {Position} -- The Selected pawn wich should move this turn
        Returns:
            game_consts.WINNER_CODES["NoWinner"] -- No win Game still running
            game_consts.WINNER_CODES["WhiteWon"] -- White Player is winner
            game_consts.WINNER_CODES["BlackWon"] -- Black Player is winner
            ________________________________________________________________
            consts.ERROR_CODES["WRONG_INPUT"] -- User has done a wrong input
        """
        ################################################################## __turn #############################################################################
        #
        print_row = ord(selceted_position.get_pos_char()) - 65
        print_col = 8 - selceted_position.get_pos_number()
        self.__printed_gamefield[print_col][print_row] = '\033[3;32;47m'+ str(self.__printed_gamefield[(print_col)][print_row])+"\033[0;30;47m"
        #
        __moves = self.__logic_gamefield.get_possible_moves(selceted_position)
        #
        if not isinstance(__moves, list):
            self.__info_text = "\033[0;31;47mFalsches Feld ausgewählt\033[0;30;47m"
            if __moves == game_consts.ERROR_CODES["WrongColor"]:
                #
                self.__error_text = "\033[0;31;47m__Spielfigur hat falsche Farbe__\033[0;30;47m"
                #
            elif __moves == game_consts.ERROR_CODES["NoFigure"]:
                #
                self.__error_text = "\033[0;31;47m__Keine Figur auf diesem Feld__\033[0;30;47m"
                #
            elif __moves == game_consts.ERROR_CODES["NoPosMoves"]:
                #
                self.__error_text = "\033[0;31;47m__Keine Spielzüge für diese Figur möglich__\033[0;30;47m"
                #
            return consts.ERROR_CODES["WRONG_INPUT"]
        #
        self.__error_text = "\033[0;31;47m__\033[0;30;47m"
        #
        for move in __moves:
            move_row = ord(move.get_pos_char()) - 65
            move_col = 8 - move.get_pos_number()
            self.__printed_gamefield[move_col][move_row] = '\033[0;31;47m'+ str(self.__printed_gamefield[move_col][move_row])+"\033[0;30;47m"
        #
        self.__print_game_all()
        #
        __next_move = self.__get_input_move(__moves)
        __move_result = self.__logic_gamefield.do_move(selceted_position, __next_move)
        #
        str_selected_position = selceted_position.get_pos_char() + str(selceted_position.get_pos_number())
        str_new_position = __next_move.get_pos_char() + str(__next_move.get_pos_number())
        #
        if isinstance(__move_result, list):
            self.__successfull_turn = True
            if self.__active_player == consts.COLOR_WHITE:
                self.__active_player = consts.COLOR_BLACK
                self.__storage.log(self.__gamename, "Weiser Spieler bewegt Bauer von"+str_selected_position+" nach "+str_new_position+"", True)
            elif self.__active_player == consts.COLOR_BLACK:
                self.__storage.log(self.__gamename, "Schwarzer Spieler bewegt Bauer von"+str_selected_position+" nach "+str_new_position+"", True)
                self.__active_player = consts.COLOR_WHITE
            #
        #
        return self.__logic_gamefield.check_win()
        #
        ################################################################## End: __turn ########################################################################
    #
    #
    def __get_input_move(self, possible_moves):
        """Request User Input and reutrns the next move for the figure

        Arguments:
            possible_moves {Position[]} -- All possibile moves for the selcted figure

        Returns:
            position {Position} -- the new Position for the selected figure
        """
        ################################################################### __get_input_move ##################################################################
        #
        print("\t\t\t\tBitte einen der folgenden Züge auswählen:")
        print("\t\t\t\t\t", end="\033[0;31;47m")
        for move in possible_moves:
            print(""+str(move.get_pos_char())+""+str(move.get_pos_number())+"", end="\t")
        #
        while consts.FOREVER:
            __move = input("\033[0;30;47m\n\t\t\t\t")
            __move = str.upper(__move)
            if len(__move) == 2:
                for move in possible_moves:
                    __move_pos = Position(str(list(__move)[0]), int(list(__move)[1]))
                    if __move_pos.get_pos_number() == move.get_pos_number() and __move_pos.get_pos_char() == move.get_pos_char():
                        return __move_pos
                    else:
                        print("\t\t\t\t\033[0;31;47mFalsche eingabe bitte eine der Optionen eingeben\033[0;30;47m")
        #
        ################################################################### End:_ __get_input_move ############################################################
    #
    #
    def get_game_name(self):
        """get the game name

        Returns:
            gamename {string} -- name of the game
        """
        ################################################################# get_game_name #######################################################################
        #
        return self.__gamename
        #
        ################################################################# End: get_game_name ##################################################################
    #
    #
    def get_playername_one(self):
        """get the name of player one

        Returns:
            playername_one {string}  -- name of player one
        """
        ################################################################# get_playername_one ##################################################################
        #
        return self.__playername_one
        #
        ################################################################# End: get_playername_one #############################################################
    #
    #
    def get_playername_two(self):
        """get the name of player two

        Returns:
            playername_two {string}  -- name of player two
        """
        ################################################################# get_playername_one ##################################################################
        #
        return self.__playername_two
        #
        ################################################################# End: get_playername_one #############################################################
    #
    #
    def get_play_against_bot(self):
        """Returns value in field play against bot

        Returns:
            play_against_bot {bool} -- play_against_bot
        """
        ################################################################# get_play_against_bot ################################################################
        #
        if self.__bot is not None:
            return True
        else:
            return False
        #
        ################################################################# End: get_play_against_bot ###########################################################
    #
    #
    def set_game_name(self, new_game_name):
        """sets the new game Name
        Arguments:
            new_game_name {string} -- new game name
        Returns:
            success {bool} -- success of change
        """
        ################################################################# get_play_against_bot ################################################################
        #
        if isinstance(new_game_name, str):
            self.__gamename = new_game_name
            return True
        else:
            return False
        #
        ################################################################# End: get_play_against_bot ###########################################################
    #
    #
    ######################################################################### ActiveGame ######################################################################
