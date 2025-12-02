from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

pir = MotionSensor(4)
camera = PiCamera()
camera.rotation = 180

while True:
    pir.wait_for_motion()
    print("Motion Detected")
    camera.start_recording("my_rec.h264")
    #time.sleep(3)
    camera.wait_recording(10)
    pir.wait_for_no_motion()
    camera.stop_recording()
    print("No Motion")