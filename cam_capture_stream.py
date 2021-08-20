from picamera import PiCamera
from time import sleep
import io

camera = PiCamera()
camera.rotation = 180

camera.start_preview()
sleep(5)
for filename in camera.capture_continuous('img{counter:03d}.jpg'):
    sleep(10)