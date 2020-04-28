from time import sleep


class Time:
    @staticmethod
    def sleepUntilMinuteDivisibleBy5():
        seconds_left = Time.calculateSecondsLeft()
        minutes_left = Time.calculateMinutesLeft()
        sleep(minutes_left * 60 + seconds_left)

    @staticmethod
    def calculateMinutesLeft():
        return 1

    @staticmethod
    def calculateSecondsLeft():
        return 40
