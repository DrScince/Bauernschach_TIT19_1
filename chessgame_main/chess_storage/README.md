# Dateiverwaltung

Die Dateien müssen vom Ordner darüber ausgeführt werden.\
Zum Laden, Speichern, Durchsuchen und Loggen von Dateien in /games

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
    * log
        >Die Datei wird in UTF-8 coodiert\
        >Speichert eine Variablen in einer txt Datei\
        >Falls es eine Liste ist wird Zeile für Zeile Gespeichert
    * __write_file
        >Schreibt die übergebene Datei mit den Infos
    * __log_append
        >Erweitert die übergebene Datei mit den Infos

### Fehlende Zeilen im Unittest coverage

* except für ImportError
    >Dieser kann nicht getestet werden. Wenn dieser Code ausgeführt wird, wird das Programm beendet. Except fällt wenn die Datei: consts.py fehlt.
* os.mkdir für /games und //log
    >Zum Erstellen von dem Ordner in dem die Log und Spieldateien liegen. Dies wird nur ausgeführt, wenn dieser nicht existiert. Damit Spieldateien und Logs gespeichert werden können.

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
        >Es wird eine Liste und ein String je drei mal mit dem selben Namen ausgeführt um das erweitern zu testen\
        >Der Inhalt der Testdatei wird im Terminal ausgegeben
    * test_999_remove_testfiles
        >Muss als Letztes laufen!!!\
        >Löscht die erstellten Dateien und den Ordner "games" falls dieser leer ist.

### Fehlende Zeilen im Unittest coverage

* except für ImportError
    >Dieser kann nicht getestet werden. Wenn dieser Code ausgeführt wird, wird das Programm beendet. Except fällt wenn die Dateien: chess_storage.py und consts.py fehlen.
* os.removedirs für /games und //log
    >Zum löschen von dem Ordner in dem die Log und Spieldateien liegen. Dies wird nur ausgeführt, wenn dieser Leer ist. Damit vorhandene Spieldateien und Logs nicht vom Test gelöscht werden.