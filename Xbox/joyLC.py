import os
import time
import xbox
#import wiringpi
#import serial
#serial = wiringpi.serialOpen('/dev/ttyUSB0',38400)
#serial = serial.Serial(
#	port = '/dev/ttyUSB0',
#	baudrate = 38400,
#	parity = serial.PARITY_NONE,
#	stopbits = serial.STOPBITS_ONE,
#	bytesize = serial.EIGHTBITS,
#	timeout = 1
#	)

GAMEPADBUTTONA = 0
GAMEPADBUTTONB = 0
GAMEPADLEFTX   = 0
GAMEPADLEFTY   = 0
GAMEPADRIGHTX = 0
GAMEPADRIGHTY = 0
GAMEPADTRIGGERLEFT = 0
GAMEPADTRIGGERRIGHT = 0

START_BYTE = 227	

#Defining bit positions to send through UART
#for GAMEPADBUTTONA
BUTTON_X 		= 0
BUTTON_Y		= 1
BUTTON_A		= 2
BUTTON_B		= 3
BUTTON_BACK		= 4
BUTTON_START		= 5
BUTTON_RIGHTSHOULDER	= 6
#for GAMEPADBUTTONB
BUTTON_LEFTSHOULDER	= 0
BUTTON_RIGHTSTICK	= 1
BUTTON_LEFTSTICK	= 2
BUTTON_DPADUP		= 3
BUTTON_DPADDOWN		= 4
BUTTON_DPADLEFT		= 5
BUTTON_DPADRIGHT	= 6

joy = xbox.Joystick()
#print joy
#def senddata():
#	wiringpi.serialPutchar(serial,



while True:
	#wiringpi.serialPutchar(serial,66)
	#serial = wiringpi.serialOpen('/dev/ttyUSB0',38400)	
	#print "LX =",GAMEPADLEFTX
	#print "LY=", GAMEPADLEFTY
	#print "RY = ",GAMEPADRIGHTY
	#print "RX = " , GAMEPADRIGHTX
	
	GAMEPADLEFTX =  ((1+joy.leftX())*100)
	GAMEPADLEFTY = ((1+joy.leftY())*100)
	GAMEPADRIGHTX = ((1+joy.rightX())*100)
	GAMEPADRIGHTY = ((1+joy.rightY())*100)
	GAMEPADTRIGGERRIGHT = (joy.rightTrigger()*100)
	GAMEPADTRIGGERLEFT = (joy.leftTrigger()*100)
	#wiringpi.serialPutchar(serial,67)
	if joy.connected():
		if joy.A() :		
			GAMEPADBUTTONB |= (1<<BUTTON_A)
		if joy.B():
			GAMEPADBUTTONB |= (1<<BUTTON_B)
			#print "B"
		if joy.X():
			GAMEPADBUTTONB |= (1<<BUTTON_X)
			#print "x"
		if joy.Y():
			GAMEPADBUTTONB |= (1<<BUTTON_Y)
			#print "Y"
		if joy.Back():
			GAMEPADBUTTONB |= (1<<BUTTON_BACK)
			#print "back"
		if joy.Start():
			GAMEPADBUTTONB |= (1<<BUTTON_START)
			#print "start"
		if joy.rightBumper():
			GAMEPADBUTTONB |= (1<<BUTTON_RIGHTSHOULDER)
			#print"rt"
		if joy.leftBumper():
			GAMEPADBUTTONA |= (1<<BUTTON_LEFTSHOULDER)
			#print"lt"
		if joy.rightThumbstick():
			GAMEPADBUTTONA |= (1<<BUTTON_RIGHTSTICK)
			#print"rst"
		if joy.leftThumbstick():
			GAMEPADBUTTONA |= (1<<BUTTON_LEFTSTICK)
			#print"lst"
		if joy.dpadUp():
			GAMEPADBUTTONA |= (1<<BUTTON_DPADUP)
			#print"up"
		if joy.dpadDown():
			GAMEPADBUTTONA |= (1<<BUTTON_DPADDOWN)
			#print"down"
		if joy.dpadLeft():
			GAMEPADBUTTONA |= (1<<BUTTON_DPADLEFT)
			#print"left"
		if joy.dpadRight():
			GAMEPADBUTTONA |= (1<<BUTTON_DPADRIGHT)
			#print"right"
	else:
		GAMEPADLEFTX = 100
		GAMEPADLEFTY = 100
		GAMEPADRIGHTX = 100
		GAMEPADRIGHTY = 100
		GAMEPADTRIGGERLEFT = 0
		GAMEPADTRIGGERRIGHT = 0
	
	#serial.write
	#serial = wiringpi.serialOpen('/dev/ttyUSB0',38400)
	#wiringpi.serialFlush(serial)
	#serial.write('65')
	#wiringpi.serialPutchar(serial,START_BYTE)
	#wiringpi.serialPutchar(serial,START_BYTE)
	#wiringpi.serialClose(serial)
	#wiringpi.serialPutchar(serial,GAMEPADBUTTONA)
	#wiringpi.serialPutchar(serial,GAMEPADBUTTONB)
	#wiringpi.serialPutchar(serial,GAMEPADLEFTX)
	#wiringpi.serialPutchar(serial,GAMEPADLEFTY)
	#wiringpi.serialPutchar(serial,GAMEPADRIGHTX)
	#wiringpi.serialPutchar(serial,GAMEPADRIGHTY)
	#wiringpi.serialPutchar(serial,GAMEPADTRIGGERLEFT)
	print (GAMEPADLEFTX)
	print (GAMEPADLEFTY)
	print (GAMEPADRIGHTX)
	print (GAMEPADRIGHTY)
	print (GAMEPADTRIGGERLEFT)
	print (GAMEPADTRIGGERRIGHT)
	print GAMEPADBUTTONA
	print GAMEPADBUTTONB
		
	#serial.write(chr(int(START_BYTE)))
	#time.sleep(0.001)
	#serial.write(chr(int(GAMEPADBUTTONA)))
	#time.sleep(0.001)
	#serial.write(chr(int(GAMEPADBUTTONB)))
	#time.sleep(0.001)
	#serial.write(chr(int(GAMEPADLEFTX)))
	#time.sleep(0.001)
	#serial.write(chr(int(GAMEPADLEFTY)))
	#time.sleep(0.001)
	#serial.write(chr(int(GAMEPADRIGHTX)))
	#time.sleep(0.001)
	#serial.write(chr(int(GAMEPADRIGHTY)))
	#time.sleep(0.001)
	#serial.write(chr(int(GAMEPADTRIGGERLEFT)))
	#time.sleep(0.001)
	#serial.write(chr(int(GAMEPADTRIGGERRIGHT)))
	#time.sleep(0.001)
	
#	wiringpi.serialPutchar(serial,(GAMEPADTRIGGERRIGHT))
	
	
	
	GAMEPADBUTTONA = 0
	GAMEPADBUTTONB = 0
		
	time.sleep(0.01)
	os.system("clear")
	
	#s = wiringpi.serialGetchar(serial)
	#print s
	#time.sleep(1)
	#wiringpi.delay(20)	
