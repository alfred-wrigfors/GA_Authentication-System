# Import classes/libraries
import datetime
import time
from gpiozero import LED, Button
import RPi.GPIO as gpiozero
from mfrc522 import SimpleMFRC5222

# Import custom classes/libraries


# Declaration of hardware
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# LEDs
error_LED = LED(21)
running_LED = LED(20)
status_LED = [LED(6), LED(5), LED(24), LED(25)]

# Buttons
exit_Butoon = Button(17)
deny_Button = Button(27)
allow_Button = Button(22)

# Setup
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# RFID-reader
rfid_reader = SimpleMFRC5222()

try:
	id, text = rfid_reader.read()
	print(id)
	print(text)
finally:
	GPIO.cleanup()
