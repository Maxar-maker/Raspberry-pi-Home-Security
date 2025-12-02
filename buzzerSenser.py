import RPi.GPIO as GPIO
import time

Buzzer = 4

def setup(pin):
    global BuzzerPin
    BuzzerPin = pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BuzzerPin, GPIO.OUT)
    GPIO.output(BuzzerPin, GPIO.HIGH)
def on():
    GPIO.output(BuzzerPin, GPIO.HIGH)
    
def off():
    GPIO.output(BuzzerPin, GPIO.HIGH)
    
def beep(x):
    on(1)
    time.sleep(2)
    
def loop():
    while True:
        beep(10)