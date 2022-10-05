# YYYY-MM-DD HH:MM [ACTION] MESSAGE
import datetime
import sys


def getCurrentTime() -> str:
    currentTime = datetime.datetime.now()
    currentTime = "%s-%s-%s %s:%s" % (currentTime.year, currentTime.month,
                                      currentTime.day, currentTime.hour, currentTime.minute)

    return currentTime


def getLogString(action: str, message: str) -> str:

    return getCurrentTime() + ' ['+action+'] ' + message + '\n'


# ENSURE CORRECT USAGE
if (len(sys.argv) != 2):
    print("usage: logger.py <output.txt>")
    sys.exit(1)

# OPEN FILE FOR APPEND MODE
with open(sys.argv[1], 'a') as logFile:
    command = sys.stdin.readline().rstrip()
    while (command != 'QUIT'):
        message = sys.stdin.readline().rstrip()
        logFile.write(getLogString(command, message))
        command = sys.stdin.readline().rstrip()
