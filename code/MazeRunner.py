import RPi.GPIO as GPIO
from time import sleep
from Line_Follower import Line_Follower

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# declare varibale to use methods from Line_Follower class

lf = Line_Follower()

# Set GPIO pin assignments for motor control

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

# Set all pins for GPIO output
 
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)
 
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)

GPIO.setup(Motor3A, GPIO.OUT)
GPIO.setup(Motor3B, GPIO.OUT)
GPIO.setup(Motor3E, GPIO.OUT)

GPIO.setup(Motor4A, GPIO.OUT)
GPIO.setup(Motor4B, GPIO.OUT)
GPIO.setup(Motor4E, GPIO.OUT)

# Declare variables for PWM control of enable lines, with frequency of 200 Hz

p1 = GPIO.PWM(Motor1E, 1000)
p2 = GPIO.PWM(Motor2E, 1000)
p3 = GPIO.PWM(Motor3E, 1000)
p4 = GPIO.PWM(Motor4E, 1000)

#declare duty cycles used for PWM control

slow_speed = 5
base_speed = 20
new_speed = 85
turn_speed = 47


# Set initial PWM controls to 0 for no movement

p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)

# Define initial variables:

# turns acts as a stack to track the movements made by our robot
# decision interprets the data from the IR sensor allowing the next turn decision to be made

turns = []
decision = []
turnAround = False
notAtEnd = True

delay = 0.4

# Define Movement functions

def turnLeft():
# code to have motors turn left until valid line path detected on middle sensor, codes left turn and turn around decisions

	print "Turning Left"

# Move robot forward from intersection to facilitate turning

	GPIO.output(Motor1A, GPIO.LOW)
	GPIO.output(Motor1B, GPIO.HIGH)
	p1.ChangeDutyCycle(30)
 
	GPIO.output(Motor2A, GPIO.HIGH)
	GPIO.output(Motor2B, GPIO.LOW)
	p2.ChangeDutyCycle(30)

	GPIO.output(Motor3A, GPIO.LOW)
	GPIO.output(Motor3B, GPIO.HIGH)
	p3.ChangeDutyCycle(30)

	GPIO.output(Motor4A, GPIO.HIGH)
	GPIO.output(Motor4B, GPIO.LOW)
	p4.ChangeDutyCycle(30)

	sleep(delay)

# halt robot before executing turn code

	p1.ChangeDutyCycle(0)
	p2.ChangeDutyCycle(0)
	p3.ChangeDutyCycle(0)
	p4.ChangeDutyCycle(0)


# if there is a straight path turn left until sensor index 2 shows value 0

	left = lf.read_digital()

	while left[2] == 1:

# Continue to read line sensor data so that exit condition can be detected

		left = lf.read_digital()

		GPIO.output(Motor1A, GPIO.LOW)
		GPIO.output(Motor1B, GPIO.HIGH)
		p1.ChangeDutyCycle(30)

		GPIO.output(Motor2A, GPIO.LOW)
		GPIO.output(Motor2B, GPIO.HIGH)
		p2.ChangeDutyCycle(30)

		GPIO.output(Motor3A, GPIO.HIGH)
		GPIO.output(Motor3B, GPIO.LOW)
		p3.ChangeDutyCycle(30)

		GPIO.output(Motor4A, GPIO.HIGH)
		GPIO.output(Motor4B, GPIO.LOW)
		p4.ChangeDutyCycle(30)

# Execute another while loop until middle sensor reads true

	while left[2] != 1:

# Continue to read line sensor data so that exit condition can be detected

		left = lf.read_digital()

# Use a low duty cycle to not overshoot target line

		GPIO.output(Motor1A, GPIO.LOW)
		GPIO.output(Motor1B, GPIO.HIGH)
		p1.ChangeDutyCycle(turn_speed)

		GPIO.output(Motor2A, GPIO.LOW)
		GPIO.output(Motor2B, GPIO.HIGH)
		p2.ChangeDutyCycle(turn_speed)

		GPIO.output(Motor3A, GPIO.HIGH)
		GPIO.output(Motor3B, GPIO.LOW)
		p3.ChangeDutyCycle(turn_speed)

		GPIO.output(Motor4A, GPIO.HIGH)
		GPIO.output(Motor4B, GPIO.LOW)
		p4.ChangeDutyCycle(turn_speed)

# Stop Robot once new line path has been reached

	print "Turning Completed"

	p1.ChangeDutyCycle(0)
	p2.ChangeDutyCycle(0)
	p3.ChangeDutyCycle(0)
	p4.ChangeDutyCycle(0)

def turnRight():
# code to have motors turn right until valid line path detected

	print "Turning Right"

# Move robot forward from intersection to facilitate turning

	GPIO.output(Motor1A, GPIO.LOW)
	GPIO.output(Motor1B, GPIO.HIGH)
	p1.ChangeDutyCycle(turn_speed)
 
	GPIO.output(Motor2A, GPIO.HIGH)
	GPIO.output(Motor2B, GPIO.LOW)
	p2.ChangeDutyCycle(turn_speed)

	GPIO.output(Motor3A, GPIO.LOW)
	GPIO.output(Motor3B, GPIO.HIGH)
	p3.ChangeDutyCycle(turn_speed)

	GPIO.output(Motor4A, GPIO.HIGH)
	GPIO.output(Motor4B, GPIO.LOW)
	p4.ChangeDutyCycle(turn_speed)

	sleep(delay)

# halt robot before executing turn code

	p1.ChangeDutyCycle(0)
	p2.ChangeDutyCycle(0)
	p3.ChangeDutyCycle(0)
	p4.ChangeDutyCycle(0)


# if there is a straight path turn right until sensor index 2 shows value 0

	right = lf.read_digital()

	while right[2] == 1:

# Continue to read line sensor data so that exit condition can be detected
	
		right = lf.read_digital()

		GPIO.output(Motor1A, GPIO.HIGH)
		GPIO.output(Motor1B, GPIO.LOW)
		p1.ChangeDutyCycle(turn_speed)


		GPIO.output(Motor2A, GPIO.HIGH)
		GPIO.output(Motor2B, GPIO.LOW)
		p2.ChangeDutyCycle(turn_speed)

		GPIO.output(Motor3A, GPIO.LOW)
		GPIO.output(Motor3B, GPIO.HIGH)
		p3.ChangeDutyCycle(turn_speed)

		GPIO.output(Motor4A, GPIO.LOW)
		GPIO.output(Motor4B, GPIO.HIGH)
		p4.ChangeDutyCycle(turn_speed)

# Execute another while loop until middle sensor reads true

	while right[2] != 1:

# Continue to read line sensor data so that exit condition can be detected

		right = lf.read_digital()

# Use a low duty cycle to not overshoot target line

		GPIO.output(Motor1A, GPIO.HIGH)
		GPIO.output(Motor1B, GPIO.LOW)
		p1.ChangeDutyCycle(turn_speed)

		GPIO.output(Motor2A, GPIO.HIGH)
		GPIO.output(Motor2B, GPIO.LOW)
		p2.ChangeDutyCycle(turn_speed)

		GPIO.output(Motor3A, GPIO.LOW)
		GPIO.output(Motor3B, GPIO.HIGH)
		p3.ChangeDutyCycle(turn_speed)

		GPIO.output(Motor4A, GPIO.LOW)
		GPIO.output(Motor4B, GPIO.HIGH)
		p4.ChangeDutyCycle(turn_speed)

	print "Turning Complete"

# Stop Robot once new line path has been reached

	p1.ChangeDutyCycle(0)
	p2.ChangeDutyCycle(0)
	p3.ChangeDutyCycle(0)
	p4.ChangeDutyCycle(0)

def move():

# Code that allows vehicle to traverse the maze, continues forward correcting path until an intersection,
# or dead end is detected

# Assign boolean operators for Left and Right turns

	LeftT = False
	RightT = False


# loop movement until intersection of dead end is reached

	while True:

# Set initial forward movement conditions

		GPIO.output(Motor1A, GPIO.LOW)
		GPIO.output(Motor1B, GPIO.HIGH)
		p1.ChangeDutyCycle(base_speed)
 
		GPIO.output(Motor2A, GPIO.HIGH)
		GPIO.output(Motor2B, GPIO.LOW)
		p2.ChangeDutyCycle(base_speed)
	
		GPIO.output(Motor3A, GPIO.LOW)
		GPIO.output(Motor3B, GPIO.HIGH)
		p3.ChangeDutyCycle(base_speed)

		GPIO.output(Motor4A, GPIO.HIGH)
		GPIO.output(Motor4B,  GPIO.LOW)
		p4.ChangeDutyCycle(base_speed)

# Use test to read data from IR sensor

		test = lf.read_digital()


# increase PWM for left side and decrease for right to correct path
	
		count = 0
	
		while test[1]:

			test = lf.read_digital()
		
			p1.ChangeDutyCycle(new_speed)
			p2.ChangeDutyCycle(slow_speed)
			p3.ChangeDutyCycle(slow_speed)
			p4.ChangeDutyCycle(new_speed)

# check for intersections, counts used to avoid false positives

# check for left hand turn

			if test[0] == 1:

				count = count + 1

				LeftT = True

# check for right hand turn

			if test[4] == 1:
			
				count = count + 1

				RightT = True

			if count > 15:

				break

# return to base_speed

		p1.ChangeDutyCycle(base_speed)
		p2.ChangeDutyCycle(base_speed)
		p3.ChangeDutyCycle(base_speed)
		p4.ChangeDutyCycle(base_speed)

		if count > 15:

			break

		count = 0

# increase PWM for right side and decrease left side to correct straight path
	
		while test[3]:

			test = lf.read_digital()

			p1.ChangeDutyCycle(slow_speed)
			p2.ChangeDutyCycle(new_speed)
			p3.ChangeDutyCycle(new_speed)
			p4.ChangeDutyCycle(slow_speed)

# check for intersections, counts used to avoid false positives

# check for left hand turn

			if test[0] == 1:

				count = count + 1

				LeftT = True

# check for right hand turn

			if test[4] == 1:
			
				count = count + 1

				RightT = True

			if count > 15:

				break

# Return to base speeds

		p1.ChangeDutyCycle(base_speed)
		p2.ChangeDutyCycle(base_speed)
		p3.ChangeDutyCycle(base_speed)
		p4.ChangeDutyCycle(base_speed)

		if count > 15:

			break

# reset count to test for intersection while path is not being corrected

		count = 0

# check for intersections if path is currently not being corrected

		while test[0] == 1 or test[4] == 1:

			test = lf.read_digital()

			if test[0] == 1:

				count = count + 1

				LeftT = True

# check for right hand turn

			if test[4] == 1:
			
				count = count + 1

				RightT = True
	
			if count > 15:

				break

		if count > 15:

			break

		count = 0

# check for dead end

		while test[2] != 1:
		
			count = count + 1
			test = lf.read_digital()

			if count == 20:

				break
		if count == 20:
			break

# stop motor

	p1.ChangeDutyCycle(0)
	p2.ChangeDutyCycle(0)
	p3.ChangeDutyCycle(0)
	p4.ChangeDutyCycle(0)

# wait 0.5 sec to take additional reading to determine path

	sleep(0.5)

	test1 = lf.read_digital()

# Check line sensor reading to send back list to main program

	if all(test1):

		test = test1

	elif LeftT:

		test = [1, 0, 0, 0, 0]

	elif test1[1] == 1 or test1[2] == 1 or test1[3] == 1:

		test = [0, 1, 1, 1, 0]

	elif RightT:

		test = [0, 0, 0, 0, 1]

	else:

		test = [0, 0, 0, 0, 0]

	return test

while notAtEnd:

# Move Robot forward until an intersection is detected return IR sensor readings to decision  
  
	decision = move()

# Check if Robot has reached end of maze if not execute next turn decision
	
	if all(decision):
		notAtEnd = False
		print "End Reached"
	  
# Left turn has priority, then straight, then right turn lastly if not turns detected robot will turn around 
   
	else:

#check for left path priority

		if decision[0] == 1:
			turns.append(1)
			current = 1
			turnLeft()
			print "Left"

# check for straight path priority, if left path isn't present

		elif decision[2] == 1 and decision[0] == 0:
	  		turns.append(2)
			current = 2
			print "Straight"

# Check if right path is available
		
		elif decision[4] == 1:
			turns.append(3)
			current = 3
			turnRight()
			print "Right"
		
# if no other paths detected the vehicle is prompted to turn around

		else:
			turns.append(4)
			turnLeft()
			turnAround = True
			print "Turn Around"

# If Robot turns around previous turns will be removed while backtracking maze
		
	if turnAround:
		check = turns.pop()
	  
# turn around value will be discarded from list, if value is not 4 turn decision is checked for backtracking	

		if check != 4:
			check = check + turns.pop()
		
# If check value equals 4 means that turn is being backtracked by robot and will be discarded from list
# Else the new value is appended to list resulting in new path being tracked

		if check != 4:
			turns.append(check)
			turnAround = False

# Once end of maze is reached, robot will turn around and return to start of maze using best path taken

sleep(3)

print "Backtracking"		  

turnLeft()

# Move through maze along optimal path traversed using length of turns list as stopping point
    
while len(turns)>0:

	if len(turns) == 0:

		break
  
	decision = move()
	
	nextMove = turns.pop()
	
	if nextMove == 1:
		
		turnRight()
		print "Right"

# move forward by doing nothing, allowing program to loop
  	
	elif nextMove == 3:

		turnLeft()
		print "Left"

	else:

		print "Straight"


# Clean up GPIO pins and close program

p1.stop()
p2.stop()
p3.stop()
p4.stop()

GPIO.cleanup()
