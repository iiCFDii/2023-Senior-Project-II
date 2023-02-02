# Ultrasonic Sensors: LV-MaxSonar-EZ Series

This python code currently programs the sensors on a Raspberry Pi 3 Model B. Programming is currently in progress. Code does not function properly. Running into a serial port error. Unsure how to fix.

This was used to test functionality of the sensors. Eventually they will be programmed on the Khadas Vim3 board.

## Pinouts
- Pin 1 - BW: disconnect or set low for serial output from TX, otherwise if high, TX outputs pulse data
- Pin 2 - PW: Outputs pulse width range
  - distance calulated using scale factor of 147uS per in.
- Pin 3 - AN: Outputs analog voltage, scaling factor of (VCC/512) per in.
  - 5V supply yields 9.8 mV/in., 3.3V supply yields 6.4mV/in.
- Pin 4 - RX: default is high; disconnect or set high to continually measure and output range, otherwise if low, sensor stops ranging (requires 20uS to retrieve range)
- Pin 5 - TX: Output based on BW (pin 1)
  - RS232 Serial data output with voltages from 0 to VCC (see datasheet linked below)
    - Output format: "R" followed by 3 ASCII digits representing the range in inches (max of 255) followed by carriage return (ASCII 13)
    - 9600 Baud rate, 8 bits, no parity, with one stop bit
- Pin 6 - +5V: VCC 2.5-5.5V supply (3mA for 5V, 2mA for 3V)
- Pin 7 - GND 

## Additional Info
- Readings can occur up to every 50mS (20Hz rate)
- Range: 6-20 inches (anything within 6in. may read as 6in.)
- Using multiple sensors in a single system can cause interference between sensors (see page 5 of datasheet for methods to counteract this)

## Additional Resources
- [RS232 Serial Communication Protocol: Basics, Working & Specifications](https://circuitdigest.com/article/rs232-serial-communication-protocol-basics-specifications#:~:text=RS232%20is%20a%20standard%20protocol,data%20exchange%20between%20the%20devices.)
- [Using a MaxSonar with a Raspberry Pi](https://www.maxbotix.com/raspberry-pi-with-ultrasonic-sensors074.htm)
  - I followed these instructions to program the sensors

