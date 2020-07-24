import Jetson.GPIO as GPIO
import time

class RGB:
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

    def __init__(self, redpin = None, greenpin = None, bluepin = None):
        self.__redpin = redpin
        self.__greenpin = greenpin
        self.__bluepin = bluepin
        self.state = "OFF"
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        if redpin is not None :
            GPIO.setup(self.__redpin, GPIO.OUT, initial=GPIO.HIGH)
        if greenpin is not None :
            GPIO.setup(self.__greenpin, GPIO.OUT, initial=GPIO.HIGH)
        if bluepin is not None :
            GPIO.setup(self.__bluepin, GPIO.OUT, initial=GPIO.HIGH)


    def red(self):
        self.state = RGB.RED
        if self.__redpin is not None:
            GPIO.output(self.__redpin, GPIO.LOW)
        if self.__greenpin is not None:
            GPIO.output(self.__greenpin, GPIO.HIGH)
        if self.__bluepin is not None:
            GPIO.output(self.__bluepin, GPIO.HIGH)

    def green(self):
        self.state = RGB.GREEN
        if self.__redpin is not None:
            GPIO.output(self.__redpin, GPIO.HIGH)
        if self.__greenpin is not None:
            GPIO.output(self.__greenpin, GPIO.LOW)
        if self.__bluepin is not None:
            GPIO.output(self.__bluepin, GPIO.HIGH)

    def blue(self):
        self.state = RGB.BLUE
        if self.__redpin is not None:
            GPIO.output(self.__redpin, GPIO.HIGH)
        if self.__greenpin is not None:
            GPIO.output(self.__greenpin, GPIO.HIGH)
        if self.__bluepin is not None:
            GPIO.output(self.__bluepin, GPIO.LOW)
    def off(self):
        self.state = "OFF"
        if self.__redpin is not None:
            GPIO.output(self.__redpin, GPIO.HIGH)
        if self.__greenpin is not None:
            GPIO.output(self.__greenpin, GPIO.HIGH)
        if self.__bluepin is not None:
            GPIO.output(self.__bluepin, GPIO.HIGH)

if __name__ == '__main__':
    try:
        rgb = RGB(12,13,15)

        rgb.red()
        time.sleep(2)
        rgb.off()

        rgb.blue()
        time.sleep(2)
        rgb.off()

        rgb.green()
        time.sleep(2)
        rgb.off()

    except KeyboardInterrupt:
        print()

    finally:
        rgb.off()
        print("종료")