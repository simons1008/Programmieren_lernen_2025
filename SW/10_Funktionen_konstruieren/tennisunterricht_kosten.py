# Programm vergleicht die Kosten von zwei Angeboten für Tennisunterricht 

# 1. Angebot: Input der Funktion ist eine Integerzahl in der Einheit Stunde
#             Output der Funktion ist eine Dezimalzahl in der Einheit EUR

# Funktion mit Datentyp 
def tennis_pro(trainerstunden: int) -> float:
    kosten = (20 + 30) * trainerstunden
    return kosten

# 2. Angebot: Input der Funktion ist eine Integerzahl in der Einheit Stunde
#             Output der Funktion ist eine Dezimalzahl in der Einheit EUR

# Funktion mit Datentyp
def go_tennis(trainerstunden: int) -> float:
    kosten = 260 + 25 * trainerstunden
    return kosten

# Input Liste anlegen
trainerstunden_liste = range(0, 13)
# 1. Angebot: Output Liste (leer) anlegen
kosten_liste1 = []
# 2. Angebot: Output Liste (leer) anlegen
kosten_liste2 = []

# Funktionen aufrufen
for x in trainerstunden_liste:
    kosten_liste1.append(tennis_pro(x))
    kosten_liste2.append(go_tennis(x))

# Ergebnisse drucken
print("Trainerstunden  Tennis Pro  Go-Tennis")
for x, y, z in zip(trainerstunden_liste, kosten_liste1, kosten_liste2):
    print("{:14.2f}  {:10.2f}  {:9.2f}".format(x, y, z))

# Modul für das Plotten von Graphen importieren
import matplotlib.pyplot as plt

# Ergebnisse plotten
plt.plot(trainerstunden_liste, kosten_liste1)
plt.plot(trainerstunden_liste, kosten_liste2)
plt.xlabel("Trainerstunden")
plt.ylabel("Kosten")
plt.show()
