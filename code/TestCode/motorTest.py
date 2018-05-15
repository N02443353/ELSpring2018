import RPi.GPIO as GPIO
from time import sleep
from Line_Follower import Line_Follower

lf = Line_Follower()
 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
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

p1 = GPIO.PWM(Motor1E, 200)
p2 = GPIO.PWM(Motor2E, 200)
p3 = GPIO.PWM(Motor3E, 200)
p4 = GPIO.PWM(Motor4E, 200)

p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)
 
print "Left"

GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
#p1.ChangeDutyCycle(60)
#GPIO.output(Motor1E,GPIO.HIGH)
 
GPIO.output(Motor2A,GPIO.LOW)
GPIO.output(Motor2B,GPIO.HIGH)
#p2.ChangeDutyCycle(60)
#GPIO.output(Motor2E,GPIO.HIGH)

GPIO.output(Motor3A,GPIO.HIGH)
GPIO.output(Motor3B,GPIO.LOW)
#p3.ChangeDutyCycle(90)
#GPIO.output(Motor3E,GPIO.HIGH)


GPIO.output(Motor4A,GPIO.HIGH)
GPIO.output(Motor4B,GPIO.LOW)
#p4.ChangeDutyCycle(90)
#GPIO.output(Motor4E,GPIO.HIGH)

sleep(.5)

print "Forward"

GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
p1.ChangeDutyCycle(40)
 
GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
p2.ChangeDutyCycle(40)

GPIO.output(Motor3A,GPIO.LOW)
GPIO.output(Motor3B,GPIO.HIGH)
p3.ChangeDutyCycle(40)
#GPIO.output(Motor3E,GPIO.HIGH)

GPIO.output(Motor4A,GPIO.HIGH)
GPIO.output(Motor4B,GPIO.LOW)
p4.ChangeDutyCycle(40)
#GPIO.output(Motor4E,GPIO.HIGH)

sleep(1.5)
  
print "Right"

#GPIO.output(Motor1A,GPIO.HIGH)
#GPIO.output(Motor1B,GPIO.LOW)
#p1.ChangeDutyCycle(60)
#GPIO.output(Motor1E,GPIO.HIGH)
 
#GPIO.output(Motor2A,GPIO.HIGH)
#GPIO.output(Motor2B,GPIO.LOW)
#p2.ChangeDutyCycle(60)
#GPIO.output(Motor2E,GPIO.HIGH)

#GPIO.output(Motor3A,GPIO.LOW)
#GPIO.output(Motor3B,GPIO.HIGH)
#p3.ChangeDutyCycle(90)
#GPIO.output(Motor3E,GPIO.HIGH)

#GPIO.output(Motor4A,GPIO.LOW)
#GPIO.output(Motor4B,GPIO.HIGH)
#p4.ChangeDutyCycle(90)
#GPIO.output(Motor4E,GPIO.HIGH)

print lf.read_digital()[3:]

#sleep(0)
 
print "Now stop"

p1.stop()
p2.stop()
p3.stop()
p4.stop()

GPIO.cleanup()
