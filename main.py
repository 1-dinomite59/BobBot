from gpiozero import Robot
from gpiozero.pins.pigpio import PiGPIOFactory
from sense_hat import SenseHat
from signal import pause

factory = PiGPIOFactory(host='192.168.')

sense = SenseHat()
robot = Robot(left=(9, 10), right=(4, 5), pin_factory=factory)

sense.stick.direction_up = robot.forward
sense.stick.direction_down = robot.backward
sense.stick.direction_left = robot.left
sense.stick.direction_right = robot.right
sense.stick.direction_middle = robot.stop

pause()