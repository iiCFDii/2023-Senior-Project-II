'''
This is a program to test the LV-MaxSonar-EZ ultrasonic sensors on a raspberry pi.

Program reads serial data and returns integer value representing distance to target in millimeters.

Wiring is as follows:
Sensor Pin 7 (GND) --- Pi Pin 6 (Ground) 
Sensor Pin 6 (VCC) --- Pi Pin 4 (5V supply) 
Sensor Pin 5 (TX)  --- Pi Pin 10 (GPIO 14, RXD) 
'''

from time import time
import serial

serialDevice = "/dev/ttyAMA0"
maxWait = 3 # seconds to try for good reading before quitting

def main():
	# setup serial port
	ser = serial.Serial(serialDevice, 9600, 8, 'N', 1, timeout = 1)

	# get current time
	timeStart = time()

	valueCount = 0

	# while within maxWait seconds
	while time() < timeStart + maxWait:
		if ser.inWaiting():
			bytesToRead = ser.inWaiting()
			valueCount += 1

			# 1st reading may be partial number, skip
			if valueCount < 2:
				continue

			testData = ser.read(bytesToRead)

			if not testData.startswith(b'R'):
				# test that data received begins with R (based on RS232 communication protocol)
				continue
			try:
				sensorData = testData.decode('utf-8').lstrip('R')
			except UnicodeDecodeError:
				# Data received could not be decoded properly
				continue
			try:
				mm = int(sensorData)
			except ValueError:
				# value is not a number
				continue

			ser.close()
			return(mm)

	ser.close()
	raise RuntimeError("Expected serial data not received.")

if __name__ == "__main__":
	main()
