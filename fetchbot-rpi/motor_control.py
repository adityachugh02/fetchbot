# Robot forward, left and right
import time  # Import the Time library
import gpiozero # Import the GPIO Zero Library

right_motor = gpiozero.Motor(9, 10)
left_motor = gpiozero.Motor(7, 8)
led = gpiozero.LED(14)

def ready():
    led.on()

def forward(speed=0.5, duration=0.1):

    # Forward: Turn both motors on with the speed "speed"
    left_motor.forward(speed)
    right_motor.forward(speed)

    # Wait for "duration" seconds
    time.sleep(duration)

    # Turn the motors off
    left_motor.stop()
    right_motor.stop()

def backward(speed=0.5, duration=0.1):

    # Backward: Turn both motors on for backward rotation with the speed "speed"
    left_motor.backward(speed)
    right_motor.backward(speed)

    # Wait for "duration" seconds
    time.sleep(duration)

    # Turn the motors off
    left_motor.stop()
    right_motor.stop()

def turn_right(speed=0.5, duration=0.1):

    # right: Turn on right motor backward and left motor forward with a speed of 0.5 
    right_motor.backward(speed)
    left_motor.forward(speed)

    # Wait for "duration" seconds
    time.sleep(duration)

    # Turn the motors off
    left_motor.stop()
    right_motor.stop()
    
def turn_left(speed=0.5, duration=0.1):

    # left: Turn on right motor foward and left motor backward with a speed of 0.5 
    right_motor.forward(speed)
    left_motor.backward(speed)

    # Wait for "duration" seconds
    time.sleep(duration)

    # Turn the motors off
    left_motor.stop()
    right_motor.stop()


