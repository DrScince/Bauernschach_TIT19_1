# Dateiverwaltung

Zum Laden, Speichern und durchsuchen von Dateien in /games

## chess_storage

* class ChessStorage
    * save_data
        >Speichert das Spiel\
        >Bekommt ein Spielfeld und ein String als Übergabeparameter
    * load_data
        >Läd eine Spiel\
        >Bekommt ein String als Übergabeparameter
    * get_all_games
        >Gibt alle Dateien im Pfad /games in einer Liste zurück
    * log_game
        >Speichert eine Variablen in einer txt Datei

## test_chessstorage

* class StorageTest
    >Nach dem Name test_ in den Methoden folgt eine Zahl für die Reihenfolge
    * test_1_save_data
        >Es wird drei mal mit dem selben Namen gespeichert um das überschreiben zu testen
    * test_2_load_data
        >Es wird einmal eine nicht vorhandene Datei und eine Vorhandene geladen sowie den Inhalt geprüft
    * test_3_get_all_games
        >Testet ob die Dateinamen korrekt gelesen werden
    * test_4_log_game
        >Es wird drei mal mit dem selben Namen ausgeführt um das erweitern zu testen\
        >Der Inhalt der Testdatei wird im Terminal ausgegeben
    * test_999_remove_testfiles
        >Muss als Letztes laufen!!!\
        >Löscht die erstellten Dateien und den Ordner "games" falls dieser leer ist.