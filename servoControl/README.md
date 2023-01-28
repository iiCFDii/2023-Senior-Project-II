# MG995 Servo Motor 
[Datasheet](https://components101.com/sites/default/files/component_datasheet/MG995-Servo-Motor-Datasheet.pdf)

- Brown Wire: Ground
- Red Wire: VCC (Connect to 5V Power Supply)
- Orange Wire: PWM input
- **MUST BE PROGRAMMED TO 50HZ FREQUENCY

This python code currently programs the servo on a Raspberry Pi 3 Model B. The servo is connected to Pin 32 (GPIO Pin 12, PWM0). This program uses the servo to open the pin for dropoff/release, then closes it to reset the system. 

This was used to test functionality of the servo. Eventually the servo will be programmed on the Khadas Vim3 board.

## Additional resources
- [MG995 Servo Motor Additional Info](https://components101.com/motors/mg995-servo-motor)
- [YouTube: Raspberry Pi Servo Motor Control](https://www.youtube.com/watch?v=xHDT4CwjUQE&ab_channel=ExplainingComputers)
- [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html)
- [RPi.GPIO Documentation](https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/)
