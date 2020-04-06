# Computergegner

Fuer alleiniges Spiel muss Gegner seine Zuege automatisch ausfuehren.

## opponent_move

* class Opponent
    * bot_move
        >Zug des Computergegners fuer den Aufruf von aussen\
        >Bauern als Array uebergeben (0-7 schwarz, 8-15 weiss)\
        >urspruengliches Feld und neues Feld als Liste zurueckgeben
    * diagonal_left
        >prueft ob diagonal links geschlagen werden kann\
        >ausgewaehlter Bauer als Uebergabeparameter
    * diagonal_right
        >prueft ob diagonal rechts geschlagen werden kann\
        >ausgewaehlter Bauer als Uebergabeparameter
    * select_pawn_move
        >prueft ob und wie ausgewaehlter Bauer bewegt werden kann\
        >Index des ausgewaehlten Bauers und Bauernarray als Uebergabeparameter

## test_opponent

* class OpponentTest