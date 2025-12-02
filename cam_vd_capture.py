from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
#camera.resolution = (640, 480)
camera.resolution = (1280, 720)

camera.start_preview()
sleep(2)

camera.start_recording("my_rec.h264")
#time.sleep(3)
camera.wait_recording(5)
camera.stop_recording()
camera.stop_preview()
print("Done")