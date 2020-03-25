# Dokumentation vom Projekt

*Bitte füllen*

## Ausgabe von Möbius

* [Bewertung.docx](https://github.com/DrScince/Bauernschach_TIT19_1/blob/Chess-Storage/Doku/Bewertung.docx)
* [Bewertung.xls](https://github.com/DrScince/Bauernschach_TIT19_1/blob/Chess-Storage/Doku/Bewertung.xlsx)
* [Python - Prüfungsaufgabe.pdf](https://github.com/DrScince/Bauernschach_TIT19_1/blob/Chess-Storage/Doku/Python%20-%20Pr%C3%BCfungsaufgabe.pdf)

## Dokumentation

Bitte füllen

### Test Code Anzeigen

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

### Test Link

[Selekro](https://selekro.de/)
