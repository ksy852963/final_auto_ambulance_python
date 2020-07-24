import Jetson.GPIO as GPIO
from module.Pca9685 import  Pca9685
import time


class DCmotor:
    def __init__(self, out1, out2, pca9685, pwm):
        self.__out1 = out1
        self.__out2 = out2
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(out1, GPIO.OUT, initial= GPIO.LOW)
        GPIO.setup(out2, GPIO.OUT, initial=GPIO.LOW)
        self.__pca9685 = pca9685
        self.__pwm = pwm

    def setSpeed(self, step):
        self.__pca9685.write(self.__pwm, step)

    def forword(self):
        GPIO.output(self.__out1, GPIO.HIGH)
        GPIO.output(self.__out2, GPIO.LOW)
    def backword(self):
        GPIO.output(self.__out1,GPIO.LOW)
        GPIO.output(self.__out2,GPIO.HIGH)
    def stop(self):
        GPIO.output(self.__out1, GPIO.HIGH)
        GPIO.output(self.__out2, GPIO.HIGH)

# if __name__=="__main__":