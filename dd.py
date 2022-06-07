import os
import time
import sys
from datetime import datetime

print("do you want to do anything to the text file?")
print("- delete if you want to clear the diary")
print("- view if you want to read your diary")
print("- press enter if you would like to write in it")
answer = input()
os.system('cls')
if answer == "delete":
    file = open('diary.txt', 'w')
    file.write("")
    file.close()
    sys.exit()
if answer == "view":
    file = open('diary.txt', 'r')
    print(file.read())
    file.close()
else:
    os.system('cls')
    print("What would you like to write?")
    diary = input()
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    file = open("diary.txt", 'a')
    file.write(str(currentDay) + "/" + str(currentMonth) + "/" + str(currentYear) + " " +current_time + " - " + diary + "\n")
    file.close()
