# Das Programm soll zufällige Sätze ausgeben

# Bibliothek importieren
import random

# Listen
subjekt = ["Der Hund", "Die Journalistin", "Der Maler"] 
prädikat = ["vergräbt", "interviewt", "malt"]	
objekt = ["den Knochen", "den Bürgermeister", "ein Bild"]

# Kurzbeschreibung
# Die Funktion soll Subjekt, Prädikat, Objekt aus Listen zufällig auswählen
# und einen Satz bauen

# Datenanalyse
# Input der Funktion sind die (globalen) Listen Subjekt, Prädikat und Objekt 
# Output der Funktion ist der Satz

# Funktion definieren
def bau_den_satz() -> str:
    # Funktionsrumpf
    # zufälliges Element der Liste wählen
    mein_subjekt = random.choice(subjekt)
    mein_prädikat = random.choice(prädikat)
    mein_objekt = random.choice(objekt)
    # Satz bauen
    mein_satz = mein_subjekt + " " + mein_prädikat + " " + mein_objekt
    return mein_satz	

# Ergebnisse prüfen
for i in range(5):
    # Satz bauen
    mein_satz = bau_den_satz()
    # Ergebnis drucken
    print(mein_satz)
