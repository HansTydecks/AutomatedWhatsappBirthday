import pywhatkit as what
from datetime import date
from datetime import datetime
import random

def commaFinder(line):
    place=0
    for i in range(len(line)):
        if(line[i] == ","):
            place=i
    return place+6

def makeMessage(number, name):
    with open('BIRTHDAY_LIST.txt') as list:
        for line in list:
            if(line[0] == "#" and int(line[1]) == number):
                return "Hey " + name + line[2:]

if __name__ == '__main__':
    month=(date.today().strftime("%m"))
    day=(date.today().strftime("%d"))
    with open('BIRTHDAY_LIST.txt') as list:
        for line in list:
            if(line[0:2] == month ):
                if (line[3:5] == day):
                    number = line[6:commaFinder(line[6:])]
                    message = makeMessage(random.randint(0, 4), line[commaFinder(line[6:-1])+1:])
                    what.sendwhatmsg(number, message, int(datetime.now().strftime("%H")), int(datetime.now().strftime("%M"))+2, 10, True, 2)
    quit()