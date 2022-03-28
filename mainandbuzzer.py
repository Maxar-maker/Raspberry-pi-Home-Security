from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
import time
from gpiozero import Buzzer

pir = MotionSensor(4)
camera = PiCamera()
camera.rotation = 180
buzzer = Buzzer(22)

while True:
    pir.wait_for_motion()
    print("Motion Detected")
    camera.start_recording("my_rec.h264")
    #time.sleep(3)
    camera.wait_recording(10)
    buzzer.on()
    time.sleep(10)
    pir.wait_for_no_motion()
    camera.stop_recording()
    buzzer.off()
    print("No Motion")