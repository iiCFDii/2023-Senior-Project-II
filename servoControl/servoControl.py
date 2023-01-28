import RPi.GPIO as GPIO
import time

def main():
	# set GPIO numbering mode
	GPIO.setmode(GPIO.BOARD)

	# setup servo's GPIO output pin
	GPIO.setup(32,GPIO.OUT)
	# setup device as PWM with 50Hz (20ms) period
	# GPIO.PWM(channel, frequency)
	servo = GPIO.PWM(32,50)

	# start PWM running with 0 pulse (OFF)
	# device.start(duty cycle)
	# duty cycle can range from 0.0-100.0
	print("Starting PWM")
	servo.start(0)
	print("Wait for 2 seconds")
	time.sleep(1)

	# Begin Moving Servo
	print("moving servo")
	for duty in range(1,5,1):
		servo.ChangeDutyCycle(duty)
		time.sleep(.3)
		# remove noise (jitter)
		servo.ChangeDutyCycle(0)
		time.sleep(.2)

	print("short delay before returning servo to starting position")
	time.sleep(2)

	# return servo to starting location
	print("returning servo to initial position")
	for duty in range(4,1,-1):
		servo.ChangeDutyCycle(duty)
		time.sleep(.3)
		# remove noise (jitter)
		servo.ChangeDutyCycle(0)
		time.sleep(.2)

	# stop PWM and cleanup
	servo.stop()
	GPIO.cleanup()
	print("Program Complete")

if __name__ == "__main__":
	main()
