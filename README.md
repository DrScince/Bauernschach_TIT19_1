# Bauernschach

Projektarbeit für Python von Frank Rübenkönig, Sarah Stebich, Tobias Spohn und Florian Veit

## Projektaufteilung

*Frank: UI
*Sarah: Computergegner
*Tobias: Logik
*Florian: Speichern

# Test Code Anzeigen

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

# Test Link

[Selekro](https://selekro.de/)