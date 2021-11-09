#FILE:      A06.PY
#COURSE:    SENG3030 - A06
#DATE:      2021-11-09
#PURPOSE:   Runs the main for the client application that sends messages using Amazon's SNS
import os
import datetime
import time

from backend import Backend

#Makes while loop work
runProgram = True

#PURPOSE:   Gets the date and time and returns it.
#RETURNS:   The date and time.
def getTime():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return st


def main():
    while runProgram:
        userInput = input("Enter a message (q to quit): ")
        if userInput == 'q' or userInput == 'Q':
            break
        else:
            userInput = getTime() + " " + userInput
            print(Backend.SendMsg(Backend, userInput))

main()