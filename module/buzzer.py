import Jetson.GPIO as GPIO
import time

class Buzzer:
    ON = "on"
    OFF = "off"

    def __init__(self, channel):
        self.__channel = channel
        self.state = Buzzer.OFF
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)

    def on(self):
        self.state = Buzzer.ON
        GPIO.output(self.__channel, GPIO.LOW)


    def off(self):
        self.state = Buzzer.OFF
        GPIO.output(self.__channel, GPIO.HIGH)


    def active(self):
        for i in range(8):
            GPIO.output(self.__channel, GPIO.LOW)
            self.state = Buzzer.ON
            time.sleep(0.5)
            self.state = Buzzer.OFF
            GPIO.output(self.__channel, GPIO.HIGH)
            time.sleep(1)


if __name__ == '__main__':


    try:
        buzzer = Buzzer(35)
        print(buzzer)
        buzzer.active()

    except KeyboardInterrupt:
        print()
    finally:
        buzzer.off()
        print("종료")

