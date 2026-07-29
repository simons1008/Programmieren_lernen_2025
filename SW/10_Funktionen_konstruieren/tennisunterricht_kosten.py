# Programm vergleicht die Kosten von zwei Angeboten für Tennisunterricht 

# Kurzbeschreibung
# Funktion berechnet die Kosten für das Angebot Tennis Pro

# Datenanalyse
# Input der Funktion ist eine Dezimalzahl in der Einheit Stunde
# Output der Funktion ist eine Dezimalzahl in der Einheit EUR
# Trainer: 30 EUR/Stunde   Platzmiete: 20 EUR/Stunde

# Funktion definieren
def tennis_pro(trainerstunden: float) -> float:
    kosten = (20 + 30) * trainerstunden
    return kosten

# Kurzbeschreibung
# Funktion berechnet die Kosten für das Angebot Go-Tennis 

# Datenanalyse
# Input der Funktion ist eine Dezimalzahl in der Einheit Stunde
# Output der Funktion ist eine Dezimalzahl in der Einheit EUR
# Trainer: 25 EUR/Stunde   Platzmiete: 260 EUR/Saison

# Funktion definieren
def go_tennis(trainerstunden: float) -> float:
    kosten = 260 + 25 * trainerstunden
    return kosten

# Ergebnisse prüfen
# Input Liste anlegen
trainerstunden_liste = range(0, 13)
# Output Liste (leer) von Tennis Pro anlegen
tennis_pro_kosten_liste = []
# Output Liste (leer) von Go-Tennis anlegen
go_tennis_kosten_liste = []

# Funktionen aufrufen
for x in trainerstunden_liste:
    tennis_pro_kosten_liste.append(tennis_pro(x))
    go_tennis_kosten_liste.append(go_tennis(x))

# Ergebnisse drucken
print("Trainerstunden  Tennis Pro  Go-Tennis")
for x, y, z in zip(trainerstunden_liste, tennis_pro_kosten_liste, go_tennis_kosten_liste):
    print("{:14.2f}  {:10.2f}  {:9.2f}".format(x, y, z))

# Bibliothek importieren
import matplotlib.pyplot as plt

# Ergebnisse plotten
plt.plot(trainerstunden_liste, tennis_pro_kosten_liste)
plt.plot(trainerstunden_liste, go_tennis_kosten_liste)
plt.xlabel("Trainerstunden")
plt.ylabel("Kosten")
plt.show()
