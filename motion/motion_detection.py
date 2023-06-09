import RPi.GPIO as GPIO
import requests

# Set the GPIO pin connected to the PIR sensor
PIR_PIN = 14

# Set the URL of the server to receive notifications
SERVER_URL = "http://localhost:3000/notification"

# Initialize GPIO settings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

def send_notification():
    payload = {'message': 'Motion detected at home!'}
    requests.post(SERVER_URL, data=payload)

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion detected!")
            send_notification()
            # Add code here to trigger an alert (e.g., turn on an LED or sound a buzzer)
        else:
            print("No motion detected.")
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
