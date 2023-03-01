'''
This is a program to test the LV-MaxSonar-EZ ultrasonic sensors on a raspberry pi.

Program reads serial data and returns integer value representing distance to target in millimeters.

Wiring PI is as follows:
Sensor Pin 7 (GND) --- Pi Pin 6 (Ground) 
Sensor Pin 6 (VCC) --- Pi Pin 4 (5V supply) 
Sensor Pin 5 (TX)  --- Pi Pin 10 (GPIO 14, RXD) 

Wiring Khadas Vim3 is as follows:
Sensor Pin 7 (GND) --- Vim3 Pin 21 (Ground) 
Sensor Pin 6 (VCC) --- Vim3 Pin 1 (5V supply) 
Sensor Pin 5 (TX)  --- Vim3 Pin 15 (UARTC_RX)
	--> produces data on the Khadas, but unsure what the data means; might have to rewire for RS232 protocol?
'''




from time import time
import serial
import struct

# initialize serial
ser = serial.Serial("/dev/ttyS3", 9600, 8, 'N', 1, timeout = 1)

maxWait = 3 # seconds to try for good reading before quitting


def main(): 
	print("Serial Port initialized\n")
	
	while True:
		recData = ser.read()
		#print(recData)
		#print("Reading Serial Data")
		recData = struct.unpack('B', recData)
		#print("unpacking serial data")
		recData = recData[0]
		print("data: ", recData)#, "\tser.in_waiting: ", ser.in_waiting)


'''
def main():
	# get current time
	timeStart = time()
	valueCount = 0
	print("Begin while")

	# while within maxWait seconds
	while time() < timeStart + maxWait:
		if ser.inWaiting():
			#bytesToRead = ser.read()
			#print(bytesToRead.decode('utf-8'))
			#valueCount += 1

			# 1st reading may be partial number, skip
			#if valueCount < 2:
			#	continue

			#packet = []
			testData = ser.read(8)
			print(testData.hex())
			

			if not testData.startswith(b'R'):
				# test that data received begins with R (based on RS232 communication protocol)
				continuepython
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
'''

if __name__ == "__main__":
	main()

