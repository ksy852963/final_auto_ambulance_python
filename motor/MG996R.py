from motor.Pca9685 import Pca9685
import time

class MG9665R:
    def __init__(self, pca9685, frequency=50):
        self.__pca9685 = pca9685

        pca9685.frequency = frequency
    def __map(self, angle):

        return int(164 + angle *((553-164)/180))

    def angle(self, channel, angle):
        self.__pca9685.write(channel, self.__map(angle))

if __name__ == '__main__':
    pca9685 = Pca9685()
    MG9665R = MG9665R(pca9685)

    channel = 1

    while True:

        MG9665R.angle(channel,0)
        time.sleep(1)

        MG9665R.angle(channel,90)
        time.sleep(1)

        MG9665R.angle(channel,180)
        time.sleep(1)

    print("progrem exit")