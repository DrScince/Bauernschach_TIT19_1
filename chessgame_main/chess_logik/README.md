# Klassen aller Spielfiguren

Spiellogik von Bauernschach

## consts.py

>Beinhaltet sämtliche Konstanten welche für die Spiellogik benötigt werden.

## position.py

* class Position
    >Speichert die Einzelnen Positionen auf dem Spielfeld.
    * function get_pos_number
        >Gibt den numerischen Anteil der Position zurück.
    * function get_pos_char
        >Gibt den alphabetischen Anteil er Position zurück.

### Fehlende Zeilen in Coverage

* except für ImportError
    >Dieser kann nicht getestet werden. Wenn dieser Code ausgeführt wird, wird das Programm beendet.

## figure.py

* class Figure
    >Im grunde abstract um die Vorlage für alle Figuren zu bilden.
    * function get_color
        >Gibt die Farbe der Figur zurück.
    * function get_position
        >Gibt die Position der Figur zurück.
    * function do_move
        >Ändert die Position der Figur auf die neue Position.

### Fehlende Zeilen in Coverage

* except für ImportError
    >Dieser kann nicht getestet werden. Wenn dieser Code ausgeführt wird, wird das Programm beendet.

## pawn.py

* class Pawn
    >Spielfigur Bauer, mit seine speziellen Funktionen.
    * function get_double_move
        >Gibt zurück ob als letztes der doppelte Zug gemacht wurde.
    * function get_possible_moves
        >Gibt die möglichen Züge des Bauern zurück.
    * function do_move
        >Ändert die Positon des Bauern zu der neuen Position, wenn es möglich ist.
    * function en_passant_timed_out
        >Sagt dem Bauern das der en passant bei im nicht mehr möglich ist.

### Fehlende Zeilen in Coverage

* except für ImportError
    >Dieser kann nicht getestet werden. Wenn dieser Code ausgeführt wird, wird das Programm beendet.

## field.py

* class Field
    >Repräsentiert das Spielfeld und hat alle Methoden um damit zu interagieren.
    * function get_possible_moves
        >Gibt die möglichen Züge der ausgewählten Position zurück.
    * function get_field
        >Gibt das Spielfeld zurück.
    * function do_move
        >Bewegt die ausgewählte Figur zur neuen Position, wenn möglich.
    * function check_win
        >Prüft ob jemand gewonnen hat und gibt das Ergebnis zurück.

### Fehlende Zeilen in Coverage

* except für ImportError
    >Dieser kann nicht getestet werden. Wenn dieser Code ausgeführt wird, wird das Programm beendet.

## test_position.py

* class TestPosition
    >Testet die Klasse Position.
    * function test_normal_init_and_getter
        >Testet die normale Initialisierung und getter Methoden, welche funktionieren sollten.
    * function test_error_codes
        >Testet die Error Codes ab welche zurückgegeben werden bei einer Fehlerhaften eingabe.
    * function test_wrong_argument_types
        >Testet den Abfang von Argument Typen.
### Fehlende Zeilen in Coverage

* except für ImportError
    >Dieser kann nicht getestet werden. Wenn dieser Code ausgeführt wird, wird das Programm beendet.

## test_figure.py

* class TestFigure
    >Testet die Klasse Figure
    * function test_normal_init_and_getter
        >Testet die normale Initialisierung und getter Methoden, welche funktionieren sollten.
    * function test_error_codes
        >Testet die Error Codes ab welche zurückgegeben werden bei einer Fehlerhaften eingabe.
    * function test_wrong_argument_types
        >Testet den Abfang von Argument Typen.

### Fehlende Zeilen in Coverage

* except für ImportError
    >Dieser kann nicht getestet werden. Wenn dieser Code ausgeführt wird, wird das Programm beendet.

## test_pawn.py

* class TestPawn
    >Testet die Klasse Pawn
    * function test_get_pos
        >Testet die Vererbte Funktion get_position.
    * function test_wrong_argument_types
        >Testet den Abfang von Argument Typen.
    * function test_moves
        >Testet sämtliche bewegungen vom Bauern

### Fehlende Zeilen in Coverage

* except für ImportError
    >Dieser kann nicht getestet werden. Wenn dieser Code ausgeführt wird, wird das Programm beendet.

## test_field.py

* class TestField
    >Testet die Klasse Field
    * function test_game_all_black_hit
        >Testet ein Spiel durch bis alle Schwarzen figuren geschlagen wurden und Weiß gewonnen hat.
    * function test_game_all_white_hit
        >Testet ein Spiel durch bis alle Weißen figuren geschlagen wurden und Schwarz gewonnen hat.
    * function test_game_black_back_line
        >Testet ein Spiel durch bis ein Weißer Bauer die Schwarze Linie erreicht hat.
    * function test_game_white_back_line
        >Testet ein Spiel durch bis ein Schwarzer Bauer die Weiße Linie erreicht hat.
    * function test_error_codes
        >Testet die Error Codes ab welche zurückgegeben werden bei einer Fehlerhaften eingabe.
    * function test_wrong_argument_types
        >Testet den Abfang von Argument Typen.

### Fehlende Zeilen in Coverage

* except für ImportError
    >Dieser kann nicht getestet werden. Wenn dieser Code ausgeführt wird, wird das Programm beendet.
