# Computergegner

Fuer alleiniges Spiel muss Gegner seine Zuege automatisch ausfuehren.

## opponent_move.py

* class Opponent
    * bot_move
        >Zug des Computergegners fuer den Aufruf von aussen.\
        >Bauern als Array uebergeben.\
        >Urspruengliches Feld und neues Feld als Liste zurueckgeben.
    * diagonal_left
        >Prueft, ob diagonal links geschlagen werden kann.\
        >Ausgewaehlter Bauer als Uebergabeparameter.\
        >Gibt moeglichen Move zurueck.
    * diagonal_right
        >Prueft, ob diagonal rechts geschlagen werden kann.\
        >Ausgewaehlter Bauer als Uebergabeparameter.\
        >Gibt moeglichen Move zurueck.
    * select_pawn_move
        >Prueft, ob und wie ausgewaehlter Bauer bewegt werden kann.\
        >Index des ausgewaehlten Bauers und Bauernarray als Uebergabeparameter.\
        >Gibt moeglichen Move zurueck.

### Fehlende Zeilen im Unittest coverage

* except für ImportError
    >Dieser kann nicht getestet werden. Wenn dieser Code ausgeführt wird, wird das Programm beendet.

## test_opponent.py

* class OpponentTest
    * test_1_bot_move
        >Testet Methode bot_move.\
        >Testet viermal mit vier verschiedenen Arraygroessen.\
        >Da Random ausgewaehlt wird, wird geprueft, ob Rueckgabewerte zwischen 0 bzw. 1 und 8 liegen.
    * test_2_diagonal_left
        >Testet Methode diagonal_left.\
        >Es werden drei verschiedene Spielpositionen auf korrekten Rueckgabewert ueberprueft.
    * test_3_diagonal_right
        >Testet Methode diagonal_right.\
        >Es werden drei verschiedene Spielpositionen auf korrekten Rueckgabewert ueberprueft.
    * test_4_select_pawn_move
        >Testet Methode select_pawn_move.\
        >Folgende Faelle werden abgedeckt:
        * diagonal links schlagen
        * diagonal rechts schlagen
        * einfacher Spielzug
        * kein Spielzug moeglich

### Fehlende Zeilen im Unittest coverage

* except für ImportError
    >Dieser kann nicht getestet werden. Wenn dieser Code ausgeführt wird, wird das Programm beendet.
