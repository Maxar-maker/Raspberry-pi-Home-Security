import time
from gpiozero import Buzzer

buzzer = Buzzer(22)
buzzer.on()
time.sleep(10)
buzzer.off()
print ('Done')