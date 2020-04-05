# Main

## main.py

>Menüführung.\
>Platform wird überprüft (Linux oder Windows).

* function main
    >Zentraler Startpunkt.\
    >Ruft alle Funktionen auf und Steuert den Programmablauf.
* function __print_welcome_screen
    >Es wird der Startseite im Terminal ausgegeben und zu einer Eingabe aufgefordert.
* function __get_load_game
    >Es wird eine übergebene Liste von vorhandenen Spielen ausgegeben.\
    >Über eine Eingabe wird entschieden welches Spiel geladen wird.
* function __check_new_game
    >Es wird eine Eingabeaufforderung im Terminal ausgegeben um zu entscheiden ob das Spiel neugestartet wird oder ein Neuesspiel erstellt wird.
* function __check_game_saved
    >Es wird mit einem Spiel und einem Spielnamen auufgerufen.\
    >Überprüfung ob das Spiel vorhanden ist.\
    >Nutzereingabe: Spiel speicher, überschreiben oder mit neuem Namen speichern.
* function __set_new_game
    >Nutzerabfrage für Spieldaten (Computergegner, Spielname, Spieler 1, Spieler 2).
* function __quit_game
    >Schließt das Programm und deinitialisiert es.

### Fehlende Zeilen in Coverage

* except für ImportError
    >Dieser kann nicht getestet werden. Wenn dieser Code ausgeführt wird, wird das Programm beendet.

## game.py

* class ActiveGame
    >Zentrale Spielsteuerung.\
    >Initialisierung mit: Spieler 1, Spieler 2, Spielname, class Oponent und class ChessStorage
    * run_game
        >Terminalausgabe von dem aktuellen Spiel.\
        >Aufruf self.__get_input\
        >Es wird eine Konstante (von GAME_MODE oder WINNER_CODES) zurückgegeben.
    * __update_game
        >Neues Spiel wird im Terminal Ausgegeben.\
        >Spielfigurenliste wird auf den aktuellen Stand gebracht.
    * __fill_default_game
        >Erzeugt das Schachfeld.
    * __fill_game_field
        >Füllt das Schachfeld mit Bauern.
    * __print_game_all
        >Aufruf von self.__print_menu, self.__print_game und self.__print_footer.
    * __print_menu 
        >Es wird das Menü im Terminal ausgegeben.
    * __print_footer
        >Es wird der Footer im Terminal ausgegeben.
    * __print_game
        >Es wird das aktuelle Spielfeld im Terminal ausgegeben.\
        >Aufruf von self.__print_game_line.
    * __print_game_line
        >Es wird eine Zeile des aktuelle Spielfeld im Terminal ausgegeben.
    * __get_input
        >Die konstante Nutzereingabe für jeden Spielzug oder Menüpunkt.
    * __turn
        >Wird nach dem Auswählen einer Figur ausgeführt.\
        >Aufruf von self.__get_input_move.\
        >Rückgabe von Konstanten (von ERROR_CODES oder WINNER_CODES)
    * __get_input_move
        >Es werden die möglichen Züge Ausgegeben und eine Auswahl von diesen Erwartet.\
        >Rückgabe von der neuen Position der Ausgewählten Figur.
    * get_game_name
        >Rückgabe vom Spielname
    * get_playername_one
        >Rückgabe vom Name des Spieler 1
    * get_playername_two
        >Rückgabe vom Name des Spieler 2
    * get_play_against_bot
        >Rückgabe ob gegen ein Computer gespielt wird oder nicht.

### Fehlende Zeilen in Coverage

* except für ImportError
    >Dieser kann nicht getestet werden. Wenn dieser Code ausgeführt wird, wird das Programm beendet.

## test_main.py

* 

### Fehlende Zeilen in Coverage

* except für ImportError
    >Dieser kann nicht getestet werden. Wenn dieser Code ausgeführt wird, wird das Programm beendet.
* os.removedirs für /games und //log
    >Zum löschen von dem Ordner in dem die Log und Spieldateien liegen. Dies wird nur ausgeführt, wenn dieser Leer ist. Damit vorhandene Spieldateien und Logs nicht vom Test gelöscht werden.

## test_game.py

* class GameTest
    >Nach dem Name test_ in den Methoden folgt eine Zahl für die Reihenfolge
    * test_000_init
        >Es wird die Initialisierung überprüft.
    * test_001_run_game
        >Es wird ein Set von Zügen und alle Menüpunkte abgeprüft.\
        >Es Gewinnt je inmal Weiß und Schwarz.
    * test_002_update_game
        >Die Terminal Ausgabe wird zweimal getestet
    * test_003_fill_default_game
        >Es wird getest ob eine Liste zurückgegeben wird.

### Fehlende Zeilen in Coverage

* except für ImportError
    >Dieser kann nicht getestet werden. Wenn dieser Code ausgeführt wird, wird das Programm beendet.
* os.removedirs für /games und //log
    >Zum löschen von dem Ordner in dem die Log und Spieldateien liegen. Dies wird nur ausgeführt, wenn dieser Leer ist. Damit vorhandene Spieldateien und Logs nicht vom Test gelöscht werden.