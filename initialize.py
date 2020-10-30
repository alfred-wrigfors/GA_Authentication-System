# Import classes/libraries
from gpiozero import LED, LEDBoard
import RPi.GPIO as GPIO

from mfrc522 import SimpleMFRC522

import time
import atexit
import requests
import json

# Import custom classes/libraries
from classes.API import API_class

# Declaration of variables
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Read data from config.json
with open('config.json') as json_file:
	# API
	json_data = json.load(json_file)
	API = API_class(json_data['device_id'], json_data['api_domain'], json_data['username'], json_data['password'])

# Declaration of hardware
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# LEDs
error_LED = LED("GPIO27")
allowed_LED = LEDBoard("GPIO17")
armed_LED = LED("GPIO22")

# Defone functions
# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# When the user is authorized
def access_allowed():
	allowed_LED.on()

# When the user isn't authorized
def access_denied():
	error_LED.on()

# Restore parameters to ready-state
def access_restore():
	time.sleep(0.5)
	error_LED.off()
	allowed_LED.off()


# Setup
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# RFID-reader
rfid_reader = SimpleMFRC522()
armed_LED.on()
GPIO.setmode(GPIO.BCM)

while True:

	try:
		id, text = rfid_reader.read()

	finally:
		pass

	if API.authenticate(id):
		access_allowed()

	else:
		access_denied()


	access_restore()

# Upon exit, send-offline-state to API
atexit.register(API.send_offline_state)
