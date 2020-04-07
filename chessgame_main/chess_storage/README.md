# Dateiverwaltung

Die Dateien müssen vom Ordner darüber ausgeführt werden.\
Zum Laden, Speichern, Durchsuchen und Loggen von Dateien in /games

## chess_storage.py

* class ChessStorage
    >Bei der Initialisierung werden die Ordner: "\games" und "\games\log" angelegt, falls diese nicht vorhanden sind.
    * save_data
        >Speichert das Spiel\
        >Bekommt ein Spielfeld, ein String, einen bool zum überschreiben und einen bool zum Namen ändern als Übergabeparameter
    * load_data
        >Lädt ein Spiel\
        >Bekommt ein String als Übergabeparameter
    * get_all_games
        >Gibt alle Dateien im Pfad /games in einer Liste zurück
    * log
        >Die Datei wird in UTF-8 codiert\
        >Speichert eine Variablen in einer txt-Datei\
        >Falls es eine Liste ist, wird Zeile für Zeile gespeichert
    * __write_file
        >Schreibt die übergebene Datei mit den Infos
    * __log_append
        >Erweitert die übergebene Datei mit den Infos

### Fehlende Zeilen im Unittest coverage

* except für ImportError
    >Dieser kann nicht getestet werden. Wenn dieser Code ausgeführt wird, wird das Programm beendet. Exception fällt wenn die Datei: consts.py fehlt.
* os.mkdir für /games und //log
    >Zum Erstellen vom Ordner, in dem die Log und Spieldateien liegen. Dies wird nur ausgeführt, wenn diese nicht existieren. Dadurch können Spieldateien und Logs darin gespeichert werden.

## test_chessstorage.py

* class StorageTest
    >Nach dem Name test_ in den Methoden folgt eine Zahl für die Reihenfolge
    * test_001_save_data
        >Es wird drei mal mit dem selben Namen gespeichert, um das überschreiben zu testen. Und drei Mal, um die Namenserweiterung zu testen.
    * test_002_load_data
        >Es wird einmal eine nicht vorhandene Datei und eine Vorhandene geladen, sowie der Inhalt geprüft.
    * test_3_get_all_games
        >Testet, ob die Dateinamen korrekt gelesen werden.
    * test_004_log_game
        >Es wird eine Liste und ein String je drei Mal mit dem selben Namen ausgeführt, um das Erweitern zu testen.\
        >Der Inhalt der Testdatei wird im Terminal ausgegeben.
    * test_005_write_file
        >Es wird einmal eine Datei geschrieben.
    * test_006_log_append
        >Es wird einmal eine Datei erweitert.
    * test_999_remove_testfiles
        >Muss als letztes laufen!!!\
        >Löscht die erstellten Dateien und den Ordner "\games" und "\games\log", falls diese leer sind.

### Fehlende Zeilen im Unittest coverage

* except für ImportError
    >Dieser kann nicht getestet werden. Wenn dieser Code ausgeführt wird, wird das Programm beendet. Exception fällt, wenn die Dateien chess_storage.py und consts.py fehlen.
* os.removedirs für /games und //log
    >Zum Löschen vom Ordner in dem die Log und Spieldateien liegen. Dies wird nur ausgeführt, wenn diese leer sind. Dadurch können Spieldateien und Logs darin gespeichert werden.