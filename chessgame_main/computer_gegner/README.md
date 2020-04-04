# Computergegner

Fuer alleiniges Spiel muss Gegner seine Zuege automatisch ausfuehren.

## computer_gegner

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

## test

Bitte füllen @sarahsophie98

## Test Code Anzeigen

```python
def load_data(self, file_name):
    """load match from directory ../games
    Arguments:
        file_name {string} -- name frome file to load
    Returns:
        matchfield -- returns the loaded matchfield or None
    """
    __dir_load_game = os.path.join(self.__dir_game_saves, file_name)
    try:
        with open(__dir_load_game, 'rb') as new_game:
            new_matchfield = pickle.load(new_game)
            return new_matchfield
    except IOError:
        return None
```

## Test Link

[Selekro](https://selekro.de/)
