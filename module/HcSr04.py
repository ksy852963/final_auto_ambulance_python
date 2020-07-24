import jetson.GPIO as GPIO
import time
import threading

def HcSr04(threading, Thread):
    def __init__(self, trigpin= None , ecopin = None):
        self.__trigpin = trigpin
        self.__ecopin = ecopin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarings(False)
        GPIO.setup(trigpin, GPIO.OUT)
        GPIO.setup(ecopin, GPIO.IN)
        self.value = 0
        super().__init__(target ==self.distandce)
        super(),start()

    def distance(self):
        while True:
            GPIO.output(self.__trigpine, GPIO.high)
            time.sleep(0.00001)

            GPIO.output(self.__trigpine, GPIO.LOW)

            startTime = time.time()
            stoptTime = time.tiem()


        cnt = 0

        while GPIO.input(self.__echopin) == GPIO.LOW:
            cnt += 1
            startTime  = time.time()
            if cnt > 100000:
                return self.distandce()

        while GPIO.input(self.__echopin) == GPIO.HIGH:
            cnt += 1
            startTime = time.time()
            if cnt > 100000:
                return self.distandce()


        during = stopTime - startTime
        dist = during * (343/2)*100
        self.value = dist
        time. sleep(1)


if __name__ == '__main__':
    try:
        sensor = HcSr04(trigpin = 38, ecopin=40)
        while True:
            print("거리:{}".fomatsensor.value)
            time.sleep(0.5)

    except KeyboardInterrupt:
        pass
    finally :
        GPIO.cleanup()
        print("progoram Exit")
