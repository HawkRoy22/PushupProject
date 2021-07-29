from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import time
from threading import Timer


# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


# This is a copy of 1 to 100 Pushups
morning = ['Morning', 5, 6, 7, 8, 7, 6, 5]
DayOne = ['DayOne', 12, 13, 12, 14, 8, 7, 6, 5, 4, 3, 2, 1]
DayTwo = ['DayTwo', 13, 14, 15, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
DayThree = ['DayThree', 14, 15, 16, 14, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
DayFour = ['DayFour', 15, 16, 17, 15, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
DayFive = ['DayFive', 16, 17, 18, 16, 14, 12, 11, 10, 9, 8, 6, 5, 4, 3, 2, 1]
DaySix = ['DaySix', 17, 18, 19, 17, 15, 13, 12, 11, 10, 9, 8, 6, 5, 4, 3, 2, 1]
DaySeven = ['DaySeven', 18, 19, 20, 18, 16, 14, 13, 12, 11, 10, 9, 8, 6, 5, 4, 3, 2, 1]

checkDay = input("What day of the challenge are you on? ")


def theWorkout(arr):
    print("Take 30 seconds to Warm Up")
    countdown(30)
    print("Ok, Let's Get Started ")
    for x in range(1, len(arr)):
        print("Complete " + str(arr[x]) + " Pushups in 60 seconds -> ")
        print("BEGIN")
        countdown(60)
        print("TIMES UP")
        print("Take a break of 20 seconds")
        countdown(20)


def pushups(strings):
    if strings == DayOne[0]:
        theWorkout(DayOne)
    if strings == DayTwo[0]:
        theWorkout(DayOne)
    if strings == DayThree[0]:
        theWorkout(DayOne)
    if strings == DayFour[0]:
        theWorkout(DayOne)
    if strings == DayFive[0]:
        theWorkout(DayOne)
    if strings == DaySix[0]:
        theWorkout(DayOne)
    if strings == morning[0]:
        theWorkout(morning)


pushups(checkDay)
