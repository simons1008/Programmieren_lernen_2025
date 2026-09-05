# Programm zur Bildung eines Strings mit LCD Module Fonts
# LCD Font Table: https://www.waveshare.com/datasheet/LCD_en_PDF/LCD1602.pdf
# Anleitung:
# 1) gewünschte Bitfolge angeben                             (Zeile 11)
# 2) Programm starten, Hexadezimal-Darstellung lesen         (Zeile 20)
# 3) Hexadezimal-Darstellung als Escape-Code codieren        (Zeile 23)
# 4) Programm starten, String zur gewünschen Bitfolge testen (Zeile 31)
#    -> der String auf dem LCD Display sieht meistens anders aus!

# Bitfolge des gewünschten Fonts angeben
bit_sequence = "11110110"

# Bitfolge in Integer umwandeln (Basis 2)
integer = int(bit_sequence, 2)

# Integer in Hexadezimal-Darstellung umwandeln
hex_number = hex(integer)

# Hexadezimal-Darstellung des Fonts ausgeben
print("Hexadezimal-Darstellung des Fonts", hex_number)

# Escape-Code codieren
esc_code = "\xf6"

# Die Hexadezimal-Darstellung des Fonts 4 mal in den String schreiben
string = 4 * esc_code

# Den String ausgeben. Achtung:
# - print() gibt Zeichen der ASCII Table aus
# - lcd.message() gibt Zeichen der LCD Font Table aus
print(string)
