"""Contains the class ActiveGame wich contains all functions to run a chessgame
"""

try:
    import sys
    #
    # from chess_storage.chess_storage import ChessStorage
    #
    import time
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
    def __init__(self, playername_one, playername_two, gamename, play_against_bot, storage):
        """Inits a new game with all its parameters

        Arguments:
            playername_one {[string]} -- [Name of Player 1]
            playername_two {[string]} -- [Name of Player 2]
            gamename {[string]} -- [Game Name for Save and Log File]
            play_against_bot {[bool]} -- [Select if playing against a Bot]
            storage {[ChessStorage]} --[Instance of storage class to log and save game]
        """
        try:
            assert isinstance(playername_one, str), "playername_one ist nicht vom typ string"
            assert isinstance(playername_two, str), "playername_two ist nicht vom typ string"
            assert isinstance(gamename, str), "gamename ist nicht vom typ string"
            assert isinstance(play_against_bot, bool), "play_against_bot ist nicht vom typ bool"
            assert storage is not None, "Kein storage übegeben"
        except AssertionError as error:
            #TODO Richtiger error einbinden
            print(error)
        
        self.__info_text = ""
        self.__info_text2 = ""
        self.__successfull_turn = False
        self.__active_player = consts.COLOR_WHITE
        self.__storage = storage
        self.__playername_one = playername_one
        self.__playername_two = playername_two
        self.__gamename = gamename
        self.__play_against_bot = play_against_bot

        self.__storage.log(self.__gamename, "\t\t\t Neues Spiel erstellt "+gamename, True)

        self.__logic_gamefield = Field()
        self.__printed_gamefield = self.__fill_default_game()
        self.__printed_gamefield = self.__fill_game_field(self.__logic_gamefield, self.__printed_gamefield)

    def run_game(self):
        """Runs the actual game
        
        Returns:
            bool -- TRUE if game is not finished and should continue
            string --
        """
        if self.__active_player == consts.COLOR_WHITE:
            self.__info_text = "\033[0;30;47m "+self.__playername_one+" ist an der Reihe\033[0;30;47m"
        elif self.__active_player == consts.COLOR_BLACK:
            self.__info_text = "\033[0;37;40m "+self.__playername_two+" ist an der Reihe\033[0;30;47m"
            
        self.__printed_gamefield = self.__fill_default_game()
        self.__printed_gamefield = self.__fill_game_field(self.__logic_gamefield, self.__printed_gamefield)
        self.__print_game_all()

        if self.__play_against_bot:
            #TODO Bot Instanztieren
            # self.__bot = bot()
            pass
        else:
            self.__bot = None


        if self.__successfull_turn:
            self.__storage.log(self.__gamename, "________________________________________________________________________________", True)
            self.__storage.log(self.__gamename, self.__printed_gamefield, True)
            self.__storage.log(self.__gamename, "________________________________________________________________________________", True)
            self.__successfull_turn = False
        elif len(str.split(self.__info_text2, " ")) == 3:
            self.__storage.log(self.__gamename, str.split(self.__info_text2, " ")[1], True)
        __run_game = self.__get_input()
        if __run_game == game_consts.WINNER_CODES["NoWinner"]:
            return __run_game
        else:
            print("Gewonnen")
            return input("was möchten sie machen ("+consts.NEW_GAME+") oder ("+consts.QUIT+")")
           

    def __fill_default_game(self):
        """[summary]
        Returns:
            [string[][]] -- [A default chessfield without any figures]
        """
        #TODO docstring
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

    def __fill_game_field(self, logic_gamefield, printed_gamefield):
        """[fills the printed_gamefield with pawns from logic_gamefield]

        Arguments:
            logic_gamefield {[field]} -- [contains the info from chess_logik.field]
            printed_gamefield {[string[][]} -- [string array wich represenets the printed chess field]
        """
        #TODO Docstring
        for actual_pawn in logic_gamefield.get_field():
            __actual_pos = actual_pawn.get_position()
            __actual_color = actual_pawn.get_color()
            __col = ord(__actual_pos.get_pos_char())-65
            __row = 8-__actual_pos.get_pos_number()


            #
            if __actual_color == consts.COLOR_BLACK:
                printed_gamefield[__row][__col] = u"♟"
            elif __actual_color == consts.COLOR_WHITE:
                printed_gamefield[__row][__col] = u"♙"
        #
        return printed_gamefield

    def __print_game_all(self):
        self.__print_menu()
        self.__print_game()
        self.__print_footer()

    def __print_menu(self):
        print("\n\t\t\t\t\t\tSchachautomat\t\t")
        print("\n\t\tNeues Spiel(N)\t\tSpeichern(S)\tLaden(L)\t\tSpiel Beenden(B)")
        print("\t\t________________________________________________________________________________")
    
    def __print_footer(self):
        print("\t\t________________________________________________________________________________")

    def __print_game(self):
        print("\n\t\t\t\t    A    B    C    D    E    F    G    H\n")
        for i in range(8):
            self.__print_game_line(i)
        print("\n\t\t\t\t    A    B    C    D    E    F    G    H\n")

    def __print_game_line(self, line_number):
        print("\t\t\t       ", end="")
        print('\033[6;34;47m'+str(8-line_number)+"", end="\033[0;30;47m")
        for i in range(8):
            print("    "+str(self.__printed_gamefield[line_number][i])+"", end="")
        if line_number == 3:
            print("    \033[6;34;47m"+str(8-line_number)+"\033[0;30;47m\t\t"+self.__info_text+"", end="\033[0;30;47m\n")
        elif line_number == 4:
            print("    \033[6;34;47m"+str(8-line_number)+"\033[0;30;47m\t\t"+self.__info_text2+"", end="\033[0;30;47m\n")
        else:
            print("    \033[6;34;47m"+str(8-line_number), end="\033[0;30;47m\n")

    def __get_input(self):
        if self.__play_against_bot and self.__active_player == game_consts.COLOR_BLACK:
            #__sel_position = self.__bot.get_pawn_position()
            #__new_position = self.__bot.get_pawn_move()
            time.sleep(2)
            __sel_position = Position('A', 7)
            __new_position = Position('A', 5)
            self.__logic_gamefield.do_move(__sel_position, __new_position)
            self.__successfull_turn = True
            self.__active_player = consts.COLOR_WHITE
            self.__storage.log(self.__gamename, "Weiser Spieler bewegt Bauer von A7 nach A5", True)
            return True
        else:
            print("\t\t\t\tBitte Menü Aktion eingeben oder Bauer wählen")###
            #
            desiccion = input("\t\t\t\t")
            desiccion = str.upper(desiccion)
            #TODO falsche Eingabe Abfangen
            if desiccion == consts.LOAD:
                print("\t\t\t\tSpiel Laden")
                return consts.LOAD
            elif desiccion == consts.SAVE:
                return consts.SAVE
            elif desiccion == consts.NEW_GAME:
                return consts.NEW_GAME
            elif desiccion == consts.QUIT:
                return consts.QUIT
            elif len(desiccion) == 2:
                __pos = Position(str(list(desiccion)[0]), int(list(desiccion)[1]))
                return self.__turn(__pos)
            else:
                return True

    def __turn(self, selceted_position):

        row = ord(selceted_position.get_pos_char()) - 65
        print_col = 8 - selceted_position.get_pos_number()
        self.__printed_gamefield[print_col][row] = '\033[3;32;47m'+ str(self.__printed_gamefield[(print_col)][row])+"\033[0;30;47m"
        __moves = self.__logic_gamefield.get_possible_moves(selceted_position)
        if not isinstance(__moves, list):
            self.__info_text = "\033[0;31;47mFalsches Feld ausgewählt\033[0;30;47m"
            if __moves == game_consts.ERROR_CODES["WrongColor"]:
                self.__info_text2 = "\033[0;31;47m Spielfigur hat falsche Farbe \033[0;30;47m"
            elif __moves == game_consts.ERROR_CODES["NoFigure"]:
                self.__info_text2 = "\033[0;31;47m Keine Figur auf diesem Feld \033[0;30;47m"
            elif __moves == game_consts.ERROR_CODES["NoPosMoves"]:
                self.__info_text2 = "\033[0;31;47m Keine Spielzüge für diese Figur möglich \033[0;30;47m"
                
            return True
        #
        self.__info_text2 = "\033[0;31;47m \033[0;30;47m"
        for move in __moves:
            move_row = ord(move.get_pos_char()) - 65
            move_col = 8 - move.get_pos_number()
            self.__printed_gamefield[move_col][move_row] = '\033[0;31;47m'+ str(self.__printed_gamefield[move_col][move_row])+"\033[0;30;47m"
        self.__print_game_all()
        #TODO SARAH###################################################################################################################################
        # Computer Gegener Einbauen stattdessen#
        __next_move = self.__get_input_move(__moves)
        ###############################################################################################################################################
        __move_result = self.__logic_gamefield.do_move(selceted_position, __next_move)
        str_selected_position = selceted_position.get_pos_char() + str(selceted_position.get_pos_number())
        str_new_position = __next_move.get_pos_char() + str(__next_move.get_pos_number())
        if isinstance(__move_result, list):
            self.__successfull_turn = True
            if self.__active_player == consts.COLOR_WHITE:
                self.__active_player = consts.COLOR_BLACK
                self.__storage.log(self.__gamename, "Weiser Spieler bewegt Bauer von"+str_selected_position+" nach "+str_new_position+"", True)
            elif self.__active_player == consts.COLOR_BLACK:
                self.__storage.log(self.__gamename, "Schwarzer Spieler bewegt Bauer von"+str_selected_position+" nach "+str_new_position+"", True)
                self.__active_player = consts.COLOR_WHITE
       
        return self.__logic_gamefield.check_win()

    def __get_input_move(self, possible_moves):
        print("\t\t\t\tBitte einen der folgenden Züge auswählen:")
        print("\t\t\t\t\t", end="\033[0;31;47m")
        for move in possible_moves:
            print(""+str(move.get_pos_char())+""+str(move.get_pos_number())+"", end="\t")

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

    def get_game_name(self):
        return self.__gamename

    def get_playername_one(self):
        return self.__playername_one

    def get_playername_two(self):
        return self.__playername_one

    def get_play_against_bot(self):
        return self.__play_against_bot
