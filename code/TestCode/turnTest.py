#Code to test turning for robot, robot should turn left until middle sensor, index 2, is reached then stops
#This code will be used for left turns as well as turning the robot around


#Import code for program, ******shared with main****************************


import RPi.GPIO as GPIO
from time import sleep
from Line_Follower import Line_Follower

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#declare varibale to use methods from Line_Follower class

lf = Line_Follower()

#Set GPIO pin assignments for motor control
 
Motor1A = 16
Motor1B = 18
Motor1E = 22
 
Motor2A = 19
Motor2B = 21
Motor2E = 23

Motor3A = 36
Motor3B = 38
Motor3E = 40

Motor4A = 33
Motor4B = 35
Motor4E = 37

#Set all pins for GPIO output
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

GPIO.setup(Motor3A,GPIO.OUT)
GPIO.setup(Motor3B,GPIO.OUT)
GPIO.setup(Motor3E,GPIO.OUT)

GPIO.setup(Motor4A,GPIO.OUT)
GPIO.setup(Motor4B,GPIO.OUT)
GPIO.setup(Motor4E,GPIO.OUT)

#Declare variables for PWM control of enable lines, with frequency of 200 Hz

p1 = GPIO.PWM(Motor1E, 200)
p2 = GPIO.PWM(Motor2E, 200)
p3 = GPIO.PWM(Motor3E, 200)
p4 = GPIO.PWM(Motor4E, 200)

#Set initial PWM controls to 0 for no movement

p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)

#***********End of shared coding*********************

#Move robot forward from intersection to facilitate turning

GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
p1.ChangeDutyCycle(30)
 
GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
p2.ChangeDutyCycle(30)

GPIO.output(Motor3A,GPIO.LOW)
GPIO.output(Motor3B,GPIO.HIGH)
p3.ChangeDutyCycle(30)

GPIO.output(Motor4A,GPIO.HIGH)
GPIO.output(Motor4B,GPIO.LOW)
p4.ChangeDutyCycle(30)

sleep(1)

#halt robot before executing turn code

p1.stop()
p2.stop()
p3.stop()
p4.stop()


#if there is a straight path turn left until sensor index 2 shows value 0

left = lf.read_digital()

while left[2] == 1:

	left = lf.read_digital()

	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	p1.ChangeDutyCycle(30)


	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	p2.ChangeDutyCycle(30)

	GPIO.output(Motor3A,GPIO.HIGH)
	GPIO.output(Motor3B,GPIO.LOW)
	p3.ChangeDutyCycle(30)

	GPIO.output(Motor4A,GPIO.HIGH)
	GPIO.output(Motor4B,GPIO.LOW)
	p4.ChangeDutyCycle(30)

#Execute another while loop until middle sensor reads true

while left[2] != 1:

	left = lf.read_digital()

#Use a low duty cycle to not overshoot target line

	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	p1.ChangeDutyCycle(30)

	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	p2.ChangeDutyCycle(30)

	GPIO.output(Motor3A,GPIO.HIGH)
	GPIO.output(Motor3B,GPIO.LOW)
	p3.ChangeDutyCycle(30)

	GPIO.output(Motor4A,GPIO.HIGH)
	GPIO.output(Motor4B,GPIO.LOW)
	p4.ChangeDutyCycle(30)

#Stop Robot once new line path has been reached

p1.stop()
p2.stop()
p3.stop()
p4.stop()

GPIO.cleanup()
