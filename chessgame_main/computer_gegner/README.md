# Computergegner

Fuer alleiniges Spiel muss Gegner seine Zuege automatisch ausfuehren.

## opponent_move

* class Opponent
    * bot_move
        >Zug des Computergegners fuer den Aufruf von aussen\
        >Bauern als Array uebergeben\
        >urspruengliches Feld und neues Feld als Liste zurueckgeben
    * diagonal_left
        >prueft ob diagonal links geschlagen werden kann\
        >ausgewaehlter Bauer als Uebergabeparameter\
        >gibt moeglichen Move zurueck
    * diagonal_right
        >prueft ob diagonal rechts geschlagen werden kann\
        >ausgewaehlter Bauer als Uebergabeparameter\
        >gibt moeglichen Move zurueck
    * select_pawn_move
        >prueft ob und wie ausgewaehlter Bauer bewegt werden kann\
        >Index des ausgewaehlten Bauers und Bauernarray als Uebergabeparameter\
        >gibt moeglichen Move zurueck

## test_opponent

* class OpponentTest
    * test_1_bot_move
        >testet Methode bot_move\
        >testet dreimal mit drei verschiedenen Arraygroessen\
        >da Random ausgewaehlt wird, wird geprueft, ob Rueckgabewerte zwischen 0 bzw. 1 und 8 liegen
    * test_2_diagonal_left
        >testet Methode diagonal_left\
        >es werden drei verschiedene Spielpositionen auf korrekten Rueckgabewert ueberprueft
    * test_3_diagonal_right
        >testet Methode diagonal_right\
        >es werden drei verschiedene Spielpositionen auf korrekten Rueckgabewert ueberprueft
    * test_4_select_pawn_move
        >testet Methode select_pawn_move\
        >prueft ueber Rueckgabewert, ob diagonal links geschlagen wird
    * test_5_select_pawn_move
        >testet Methode select_pawn_move\
        >prueft ueber Rueckgabewert, ob diagonal rechts geschlagen wird
    * test_6_select_pawn_move
        >testet Methode select_pawn_move\
        >prueft ueber Rueckgabewert, ob Figur um eins nach vorn bewegt wird
    * test_7_select_pawn_move
        >testet Methode select_pawn_move\
        >prueft ueber Rueckgabewert, ob erkannt wird, dass kein Spielzug durchgefuehrt werden kann