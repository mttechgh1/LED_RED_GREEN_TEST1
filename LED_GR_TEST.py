# LED test program for raspberry pi 400
from  gpiozero import LED
from time import sleep
I=0
ledg=LED(25)
ledr = LED(12)
#input statement
ledg.on()
sleep(3)
ledr.on()
speep = 10
print ("END OF LOOP")
