# Computergegner

Fuer alleiniges Spiel muss Gegner seine Zuege automatisch ausfuehren.

## opponent_move

* class Opponent
    * bot_move
        >Zug des Computergegners fuer den Aufruf von aussen.\
        >Bauern als Array uebergeben.\
        >Urspruengliches Feld und neues Feld als Liste zurueckgeben.
    * diagonal_left
        >Prueft ob diagonal links geschlagen werden kann.\
        >Ausgewaehlter Bauer als Uebergabeparameter.\
        >Gibt moeglichen Move zurueck.
    * diagonal_right
        >Prueft ob diagonal rechts geschlagen werden kann.\
        >Ausgewaehlter Bauer als Uebergabeparameter.\
        >Gibt moeglichen Move zurueck.
    * select_pawn_move
        >Prueft ob und wie ausgewaehlter Bauer bewegt werden kann.\
        >Index des ausgewaehlten Bauers und Bauernarray als Uebergabeparameter.\
        >Gibt moeglichen Move zurueck.

## test_opponent

* class OpponentTest
    * test_1_bot_move
        >Testet Methode bot_move.\
        >Testet dreimal mit drei verschiedenen Arraygroessen.\
        >Da Random ausgewaehlt wird, wird geprueft, ob Rueckgabewerte zwischen 0 bzw. 1 und 8 liegen.
    * test_2_diagonal_left
        >Testet Methode diagonal_left.\
        >Es werden drei verschiedene Spielpositionen auf korrekten Rueckgabewert ueberprueft.
    * test_3_diagonal_right
        >Testet Methode diagonal_right.\
        >Es werden drei verschiedene Spielpositionen auf korrekten Rueckgabewert ueberprueft.
    * test_4_select_pawn_move
        >Testet Methode select_pawn_move.\
        >Prueft ueber Rueckgabewert, ob diagonal links geschlagen wird.
    * test_5_select_pawn_move
        >Testet Methode select_pawn_move.\
        >Prueft ueber Rueckgabewert, ob diagonal rechts geschlagen wird.
    * test_6_select_pawn_move
        >Testet Methode select_pawn_move.\
        >Prueft ueber Rueckgabewert, ob Figur um eins nach vorn bewegt wird.
    * test_7_select_pawn_move
        >Testet Methode select_pawn_move.\
        >Prueft ueber Rueckgabewert, ob erkannt wird, dass kein Spielzug durchgefuehrt werden kann.