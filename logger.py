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
    print("usage: driver.py <output.txt>")
    sys.exit(1)

# OPEN FILE FOR APPEND MODE
logFile = open(sys.argv[1], 'a')

# LOG INITIAL
logFile.write(getLogString("START", "Logging Started."))

# DEFINE MODE
stdin = sys.stdin.readline().rstrip()

while (stdin != 'QUIT'):
    if (stdin == 'QUIT'):
        sys.exit(1)
    logFile.write(stdin+'\n')
    stdin = sys.stdin.readline().rstrip()
