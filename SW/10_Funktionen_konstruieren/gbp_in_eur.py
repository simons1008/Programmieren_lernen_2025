# Das Programm soll GPB in EUR umrechnen und eine Tabelle ausgeben

# Kurzbeschreibung
# Die Funktion rechnet GPB in EUR um

# Datenanalyse
# Input der Funktion ist eine Dezimalzahl in der Einheit GBP
# Output der Funktion ist eine Dezimalzahl in der Einheit EUR
# Umrechnungsfaktor 1 GBP = 1.17 EUR

# Funktion definieren
def gbp_in_eur(gbp: float) -> float:
    eur = gbp * 1.17
    return eur

# Ergebnisse prüfen
# Input Liste anlegen und füllen
gbp_liste = []
for i in range(21):
    gbp_liste.append(i * 0.5)
# Output Liste (leer) anlegen
eur_liste = []

# Funktion aufrufen 
for x in gbp_liste:
    eur_liste.append(gbp_in_eur(x))

# Ergebnisse drucken
print("gbp    eur")
for x, y in zip(gbp_liste, eur_liste):
    print("{:5.2f} {:5.2f}".format(x, y))

# Bibliothek importieren 
import unittest

# Testfunktion definieren
class My_unittest(unittest.TestCase):

    def test_gbp_in_eur(self):
        self.assertAlmostEqual(gbp_in_eur(0), 0, 2)
        self.assertAlmostEqual(gbp_in_eur(1), 1.17, 2)
        self.assertAlmostEqual(gbp_in_eur(6.5), 7.6, 2)
        self.assertAlmostEqual(gbp_in_eur(7.5), 8.77, 2)
        self.assertAlmostEqual(gbp_in_eur(9.5), 11.11, 2)
        self.assertAlmostEqual(gbp_in_eur(10), 11.7, 2)
        self.assertAlmostEqual(gbp_in_eur(50), 58.5, 2)
        self.assertAlmostEqual(gbp_in_eur(100), 117, 2)
        self.assertAlmostEqual(gbp_in_eur(-1), -1.17, 2)

# Unittest ausführen
if __name__ == '__main__':
    unittest.main()
