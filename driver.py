import asyncio
from asyncio.subprocess import PIPE
import datetime
import sys
import time


def getCurrentTime() -> str:
    currentTime = datetime.datetime.now()
    currentTime = "%s-%s-%s %s:%s" % (currentTime.year, currentTime.month,
                                      currentTime.day, currentTime.hour, currentTime.minute)

    return currentTime


def getLogString(action: str, message: str) -> str:

    return getCurrentTime() + ' ['+action+'] ' + message + '\n'


async def main():
    # KEEP TRACK OF ENCRYPTED AND UNENCRYPTED STRINGS
    toEncryptHistory = ()
    encryptedHistory = ()

    # PRINT USAGE
    usage = "usage: \n\tpassword <message> " + "\n\tencrypt <message> " + "\n\tdecrypt <message> " + \
        "\n\thistory <password | encrypt | decrypt>" + "\n\tquit"

    print(usage)

    # WRITE TO LOG FILE THAT THE DRIVER PROGRAM HAS STARTED
    with open(sys.argv[1], 'a') as logFile:
        # CREATE TWO PROCESSES FOR LOGGER AND ENCRYPT
        logger = await asyncio.create_subprocess_exec(
            "python3", "logger.py", sys.argv[1], stdin=PIPE, stdout=PIPE)

        # CREATE TWO PROCESSES FOR LOGGER AND ENCRYPT
        encrypt = await asyncio.create_subprocess_exec(
            "python3", "encrypt.py", sys.argv[1], stdin=PIPE, stdout=PIPE)

        logger.stdin.write(bytes('STOP\n Driver Started\n.', 'utf-8'))

        # DEFINE USER INPUT
        userInput = ''

        # DEFINE LIST OF COMMANDS
        availableCommands = set(
            ['password', 'encrypt', 'decrypt', 'history', 'quit'])

        while (userInput != 'quit'):
            # GET USER INPUT
            print("Input: ", end='')
            userInput = input()
            userInputList = userInput.split(' ')
            if (len(userInputList) == 2 and userInput != 'quit'):

                command = userInputList[0]
                message = userInputList[1]

                if (command == 'password'):
                    pass
                if (command == 'encrypt'):
                    pass
                if (command == 'decrypt'):
                    pass
                if (command == 'history'):
                    pass

                logger.stdin.write(bytes(command+'\n'+message+'\n', 'utf-8'))
                encrypt.stdin.write(bytes(command+'\n'+message+'\n', 'utf-8'))

                result = bytes.decode(await encrypt.stdout.readline()).rstrip()
                message = bytes.decode(await encrypt.stdout.readline()).rstrip()

                logger.stdin.write(bytes(result+'\n'+message+'\n', 'utf-8'))

                print("Output: %s %s" % (result, message))
            else:
                pass
        logger.stdin.write(bytes('STOP\n Driver Stopped\n.', 'utf-8'))
        logger.stdin.write(bytes('QUIT\n', 'utf-8'))
        encrypt.stdin.write(bytes('QUIT\n', 'utf-8'))
        logFile.write(getLogString('STOP', 'Driver Stopped.'))

if (len(sys.argv) != 2):
    print("usage: driver.py <output.txt>")
    sys.exit(1)

asyncio.run(main())
