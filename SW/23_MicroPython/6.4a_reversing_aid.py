# import libraries
from machine import Pin
import time
from lcd1602 import LCD

# Define the pin of the buzzer
buzzer = Pin(14, Pin.OUT)

# Define the pins for the ultrasonic sensor
TRIG = Pin(26, Pin.OUT)
ECHO = Pin(25, Pin.IN)

# Initialize the LCD display
lcd = LCD()

# Initialize the interval variable
previousMillis = 0

# Beep function for the buzzer
def beep():
    buzzer.value(1)
    time.sleep_ms(100)
    buzzer.value(0)

# Function to read data from the ultrasonic sensor
def calc_distance() -> float:
    # Trigger a low signal before sending a high signal
    TRIG.off()
    time.sleep_us(2) # wait for 2 microseconds
    # Send a 10 microseconds high signal to the trigger pin
    TRIG.on()
    time.sleep_us(10)
    TRIG.off()
    # Wait for the echo pin to go high
    while not ECHO.value():
        pass
    # Record the time when the echo pin goes high
    time1 = time.ticks_us()
    # Wait for the echo pin to go low
    while ECHO.value():
        pass
    # Record the time when the echo pin goes low
    time2 = time.ticks_us()
    # Calculate the time difference
    during = time.ticks_diff(time2, time1)
    # Calculate the distance (in cm) using the speed of sound (340 m/s)
    distance = during * 340 / 2 / 10000
    # return the calculated distance
    return distance

# Main loop
while True:
    # calculate distance
    distance = calc_distance()
    # Update the distance on the LCD
    lcd.clear()
    lcd.write(0, 0, "Dis: {:6.2f} cm".format(distance))
    # Update intervals based on distance
    if distance <= 10:
        intervals = 300
    elif distance <= 20:
        intervals = 500
    elif distance <= 50:
        intervals = 1000
    else:
        intervals = 2000
    # Check if it's time to beep
    currentMillis = time.ticks_ms()
    if time.ticks_diff(currentMillis, previousMillis) >= intervals:
        beep()
        previousMillis = currentMillis
    else:
        # Sleep 100 ms
        time.sleep_ms(100)
