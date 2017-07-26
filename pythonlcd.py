from RPLCD import CharLCD
import RPi.GPIO as GPIO 
import time            

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(15,GPIO.IN)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)



lcd = CharLCD(cols = 16, rows = 2,pin_rs=15 , pin_e = 11,pins_data=[22,12,18,16])


lcd.write_string(u'Abheesh don!')
time.sleep(5)

