# Import the LCD class from the lcd1602 module
from lcd1602 import LCD

import time

# Create an instance of the LCD class and assign it to the lcd variable
lcd = LCD()
# Set the string " Hello!\n"
string = " Hello!\n"
# Display the string on the LCD screen
lcd.message(string)

time.sleep(2)
# Set the string "    Sunfounder!"
string = ["\xf0", "\xf1", "\xf2", "\xf3", "\xf4", "\xf5", "\xf6", "\xf7", "\xf8", "\xf9", "\xfa", "\xfb", "\xfc", "\xfd", "\xfe", "\xff"]
#string = "    Sunfounder!"
# Display the string on the LCD screen
lcd.message(string)

time.sleep(2)
# Clear the LCD screen
#lcd.clear()
