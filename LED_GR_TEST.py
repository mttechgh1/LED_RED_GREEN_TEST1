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
sleep(3)
ledr.off()
ledg.off()
print ("END OF LOOP")
# RESULT:  Turns ON Green first, then red, when loop completes, both led's turn OFF
