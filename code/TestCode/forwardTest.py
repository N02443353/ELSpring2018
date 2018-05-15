import RPi.GPIO as GPIO
from time import sleep
from Line_Follower import Line_Follower 

lf = Line_Follower()
test = []

#declare duty cycles used for PWM control

slow_speed = 0
base_speed = 40
new_speed = 55
 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

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

#Declare variables for PWM control of enable lines

p1 = GPIO.PWM(Motor1E, 200)
p2 = GPIO.PWM(Motor2E, 200)
p3 = GPIO.PWM(Motor3E, 200)
p4 = GPIO.PWM(Motor4E, 200)

#Set initial PWM controls to 0 for no movement

p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)

#loop movement until intersection of dead end is reached

while True:

#Set initial forward movement conditions

	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	p1.ChangeDutyCycle(base_speed)
 
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	p2.ChangeDutyCycle(base_speed)

	GPIO.output(Motor3A,GPIO.LOW)
	GPIO.output(Motor3B,GPIO.HIGH)
	p3.ChangeDutyCycle(base_speed)

	GPIO.output(Motor4A,GPIO.HIGH)
	GPIO.output(Motor4B,GPIO.LOW)
	p4.ChangeDutyCycle(base_speed)

#Use test to read data from IR sensor

	test = lf.read_digital()


#increase PWM for left side and decrease for right to correct path
	
	count = 0
	
	while test[1]:

		test = lf.read_digital()
		
		p1.ChangeDutyCycle(new_speed)

		p2.ChangeDutyCycle(slow_speed)

		p3.ChangeDutyCycle(slow_speed)

		p4.ChangeDutyCycle(new_speed)

#check for intersections, counts used to avoid false positives

#check for left hand turn

		if test[0] == 1:

			count = count + 1

			print "Left"


#check for right hand turn

		if test[4] == 1:
			
			count = count +1

			print "right"

		if count > 15:

			break

#return to base_speed

	p1.ChangeDutyCycle(base_speed)

	p2.ChangeDutyCycle(base_speed)

	p3.ChangeDutyCycle(base_speed)

	p4.ChangeDutyCycle(base_speed)

	if count > 10:

		break

	count = 0

#increase PWM for right side and decrease left side to correct straight path
	
	while test[3]:

		test = lf.read_digital()

		p1.ChangeDutyCycle(slow_speed)

		p2.ChangeDutyCycle(new_speed)

		p3.ChangeDutyCycle(new_speed)

		p4.ChangeDutyCycle(slow_speed)

#check for intersections, counts used to avoid false positives

#check for left hand turn

		if test[0] == 1:

			count = count + 1

			print "Left"


#check for right hand turn

		if test[4] == 1:
			
			count = count +1

			print "right"

		if count > 15:

			break

#Return to base speeds

	p1.ChangeDutyCycle(base_speed)

	p2.ChangeDutyCycle(base_speed)

	p3.ChangeDutyCycle(base_speed)

	p4.ChangeDutyCycle(base_speed)

	if count > 10:

		break

#check for intersections if path is currently not being corrected

	if test[0] == 1:

		test = lf.read_digital()

		print "Left"

		break

#check for right hand turn

#	test = lf.read_digital()

	count = 0

	if test[4] != 0:

		test = lf.read_digital()

		print "right"

		break


	count = 0

#check for desd end

	while test[2] != 1:
		
		count = count + 1
		test = lf.read_digital()

		if count == 20:

			break
	if count == 20:
		break

#stop motor

p1.stop()
p2.stop()
p3.stop()
p4.stop()

# wait 1 sec to take additional reading to determine path

sleep(1)

print test

test1 = lf.read_digital()
print test1

#cleanup pin assignments

GPIO.cleanup()
