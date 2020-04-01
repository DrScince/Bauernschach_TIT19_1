"""Stores the class ActiveGame wich contains all functions to run a chessgame
"""

try:
    import sys
    import consts
    #
    # from chess_storage.chess_storage import ChessStorage
    #
    from chess_logik.position import Position
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
            print(error)
        
        self.__info_text = ""
        self.__info_text2 = ""
        self.__active_player = consts.COLOR_WHITE
        
        self.__playername_one = playername_one
        self.__playername_two = playername_two
        self.__gamename = gamename
        self.__play_against_bot = play_against_bot

        storage.log(self.__gamename, "Hallo", True)

        self.__logic_gamefield = Field()
        self.__printed_gamefield = self.__fill_default_game()
        self.__printed_gamefield = self.__fill_game_field(self.__logic_gamefield, self.__printed_gamefield)

    def run_game(self):
        if self.__active_player == consts.COLOR_WHITE:
            self.__info_text = "\033[0;30;47m"+self.__playername_one+" ist an der Reihe\033[0;30;47m"
        elif self.__active_player == consts.COLOR_BLACK:
            self.__info_text = "\033[0;37;40m"+self.__playername_two+" ist an der Reihe\033[0;30;47m"
            
        self.__printed_gamefield = self.__fill_default_game()
        self.__printed_gamefield = self.__fill_game_field(self.__logic_gamefield, self.__printed_gamefield)
        self.__print_game_all()
        __run_game = self.__get_input()
        return __run_game

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
        print("\n\t\t\t\t\033[6;34;47m    A    B    C    D    E    F    G    H\033[0;30;47m\n")
        for i in range(8):
            self.__print_game_line(i)
        print("\n\t\t\t\t\033[6;34;47m    A    B    C    D    E    F    G    H\033[0;30;47m\n")

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
        if __moves == 1:
            self.__info_text = "\033[0;31;47mFalsche Feld ausgewählt\033[0;30;47m"
            self.__info_text2 = "\033[0;31;47mKein Bauer auf dem Feld oder Falsche Spielfigur\033[0;30;47m"
            return True
        #
        for move in __moves:
            move_row = ord(move.get_pos_char()) - 65
            move_col = 8 - move.get_pos_number()
            self.__printed_gamefield[move_col][move_row] = '\033[0;31;47m'+ str(self.__printed_gamefield[move_col][move_row])+"\033[0;30;47m"
        self.__print_game_all()
        #TODO SARAH###################################################################################################################################
        # Computer Gegener Einbauen stattdessen#
        __next_move = self.__get_input_move(__moves)
        ###############################################################################################################################################
        self.__logic_gamefield.do_move(selceted_position, __next_move)
        return True

    def __get_input_move(self, possible_moves):
        print("\t\t\t\tBitte einen der folgenden Züge auswählen:")
        print("\t\t\t\t\t", end="\033[0;31;47m")
        for move in possible_moves:
            print(""+str(move.get_pos_char())+""+str(move.get_pos_number())+"", end="\t")
        __move = input("\033[0;30;47m\n\t\t\t\t")
        __move = str.upper(__move)
        __move_pos = Position(str(list(__move)[0]), int(list(__move)[1]))
        
        if self.__active_player == consts.COLOR_WHITE:
            self.__active_player = consts.COLOR_BLACK
        elif self.__active_player == consts.COLOR_BLACK:
            self.__active_player = consts.COLOR_WHITE
        return __move_pos

    def get_game_name(self):
        return self.__gamename
