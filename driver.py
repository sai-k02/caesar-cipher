import asyncio
from asyncio.subprocess import PIPE
import datetime
import sys
import time

# DEFINE LIST OF AVAILABLE COMMANDS TO DRIVE PROGRAM
availableCommands = set(
    ['password', 'encrypt', 'decrypt', 'history', 'quit'])

# HISTORY DICT
history = {}
history['password'] = []
history['encrypt'] = []
history['decrypt'] = []


def processHistory(message: str):
    print("Previous " + message + "s: ")
    for index, element in enumerate(history[message]):
        print("\t[%s] - %s" % (index, element))

    print("Input selection [type 'QUIT' to exit]: ", end="")
    userInput = input()

    if (str(userInput).upper() != 'QUIT'):
        returnItem = (history[message])[int(userInput)]
    else:
        returnItem = 'QUIT'

    return returnItem


async def main():
    # PRINT USAGE
    usage = "Python program which will allow encryption/decryption with Cesar Cipher using subprocesses\nusage: \n\tpassword <message> or no command for history of password " + \
        "\n\tencrypt <message> or no command for history of password" + \
        "\n\tdecrypt <message> or no command for history of password" + \
        "\n\thistory <password | encrypt | decrypt>" + "\n\tquit"

    print(usage)

    # WRITE TO LOG FILE THAT THE DRIVER PROGRAM HAS STARTED

    # CREATE TWO PROCESSES FOR LOGGER AND ENCRYPT
    logger = await asyncio.create_subprocess_exec(
        "python3", "logger.py", sys.argv[1], stdin=PIPE, stdout=PIPE)

    # CREATE TWO PROCESSES FOR LOGGER AND ENCRYPT
    encrypt = await asyncio.create_subprocess_exec(
        "python3", "encrypt.py", sys.argv[1], stdin=PIPE, stdout=PIPE)

    logger.stdin.write(bytes('START\n Driver Started.\n', 'utf-8'))

    # DEFINE USER INPUT
    userInput = ''

    # DEFINE COMMAND
    command = ""
    message = ""

    # DEFINE LIST OF COMMANDS

    while (userInput != 'quit'):
        # GET USER INPUT
        print("\nInput: ", end='')
        userInput = input().lower().strip()
        userInputList = ['']

        if (userInput.find(' ') != -1):
            userInputList = userInput.split(' ')
        else:
            userInputList[0] = userInput

        if (len(userInputList) == 1 and userInputList[0] != 'quit'):
            # SET THE SECOND ELEMENT OF THE USERINPUTLIST TO BE THE HISTORY ITEM
            userInputList.append(processHistory(userInputList[0]))

        # ASK USER AGAIN
        if (len(userInputList) == 2):
            if (userInputList[1] == 'QUIT'):
                print("\nInput: ", end='')
                userInput = input().lower()
                userInputList = userInput.split(' ')

        if (len(userInputList) == 2 and userInput != 'quit'):

            command = userInputList[0]
            message = userInputList[1]

            if (command == 'password'):
                # ASK USER FOR HISTORY

                logger.stdin.write(
                    bytes(command.upper()+'\n'+message+'\n', 'utf-8'))
                encrypt.stdin.write(
                    bytes('PASSKEY\n'+message+'\n', 'utf-8'))
                result = bytes.decode(await encrypt.stdout.readline()).rstrip()
                if result != 'ERROR':
                    history[command].append(message)
                message = bytes.decode(await encrypt.stdout.readline()).rstrip()
                logger.stdin.write(
                    bytes(result+'\n'+message+'\n', 'utf-8'))

            if (command == 'encrypt'):

                logger.stdin.write(
                    bytes(command.upper()+'\n'+message+'\n', 'utf-8'))

                encrypt.stdin.write(
                    bytes('ENCRYPT\n'+message+'\n', 'utf-8'))

                result = bytes.decode(await encrypt.stdout.readline()).rstrip()

                if result != 'ERROR':
                    history[command].append(message)
                message = bytes.decode(await encrypt.stdout.readline()).rstrip()

                logger.stdin.write(
                    bytes(result+'\n'+message+'\n', 'utf-8'))

                logger.stdin.write(
                    bytes(result+'\n'+message+'\n', 'utf-8'))
            if (command == 'decrypt'):
                logger.stdin.write(
                    bytes(command.upper()+'\n'+message+'\n', 'utf-8'))
                encrypt.stdin.write(
                    bytes('DECRYPT\n'+message+'\n', 'utf-8'))
                result = bytes.decode(await encrypt.stdout.readline()).rstrip()
                if result != 'ERROR':
                    history[command].append(message)
                message = bytes.decode(await encrypt.stdout.readline()).rstrip()

                logger.stdin.write(
                    bytes(result+'\n'+message+'\n', 'utf-8'))

                logger.stdin.write(
                    bytes(result+'\n'+message+'\n', 'utf-8'))
            if (command == 'history'):
                if (message in availableCommands):
                    logger.stdin.write(
                        bytes(command.upper()+'\n'+message+'\n', 'utf-8'))
                    print("Previous " + message + "s: ")
                    for index, element in enumerate(history[message]):
                        print("\t[%s] - %s" % (index, element))

                else:
                    print("usage: <command> <message>")

            if (command != 'history'):
                print("Output: %s %s" % (result, message))
        elif userInputList[0] == 'quit':
            logger.stdin.write(bytes('STOP\n Driver STOP.\n', 'utf-8'))
            logger.stdin.write(bytes('QUIT\n', 'utf-8'))
            encrypt.stdin.write(bytes('QUIT\n', 'utf-8'))
        else:
            print(command, message)

        # logger.kill()
        # encrypt.kill()

if (len(sys.argv) != 2):
    print("usage: driver.py <output.txt>")
    sys.exit(1)

asyncio.run(main())
