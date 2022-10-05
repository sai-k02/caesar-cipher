import asyncio
from asyncio.subprocess import PIPE
import sys

'''
loggerOutput = await logger.stdout.readline()


'''

# PASSKEY – Sets the current password to use when encrypting or decrypting.
# ENCRYPT – Using a Vigen`ere cypher with the current password, encrypt the argument and output the result. If no password is set output an error.
# DECRYPT – Using a Vigen`ere cypher with the current password, decrypt the argument and output the result. If no password is set output an error.
# QUIT – Exit the program.
# The encryption program has the following response types:

# ENSURE CORRECT USAGE
if (len(sys.argv) != 2):
    print("usage: driver.py <output.txt>")
    sys.exit(1)


async def main():
    # PRINT USAGE
    print("usage: <COMMAND> <MESSAGE>")
    # CREATE TWO PROCESSES FOR LOGGER AND ENCRYPT
    logger = await asyncio.create_subprocess_exec(
        "python3", "logger.py", sys.argv[1], stdin=PIPE, stdout=PIPE)

    # CREATE TWO PROCESSES FOR LOGGER AND ENCRYPT
    encrypt = await asyncio.create_subprocess_exec(
        "python3", "encrypt.py", sys.argv[1], stdin=PIPE, stdout=PIPE)

    # LOG START OF LOGGER
    logger.stdin.write(bytes("START\nLogging Started.\n", 'utf-8'))

    # DEFINE USER INPUT
    userInput = ''

    # DEFINE LIST OF COMMANDS
    availableCommands = set(['ENCRYPT', 'DECRYPT', 'PASSKEY'])

    while (userInput != 'QUIT'):
        # GET USER INPUT
        print("Input: ", end='')
        userInput = input()
        userInputList = userInput.split(' ')
        if (len(userInputList) == 2):

            command = userInputList[0]
            message = userInputList[1]

            logger.stdin.write(bytes(command+'\n'+message+'\n', 'utf-8'))
            encrypt.stdin.write(bytes(command+'\n'+message+'\n', 'utf-8'))

            result = bytes.decode(await encrypt.stdout.readline()).rstrip()
            message = bytes.decode(await encrypt.stdout.readline()).rstrip()

            logger.stdin.write(bytes(result+'\n'+message+'\n', 'utf-8'))

            print("Output: %s %s" % (result, message))
        else:
            print("usage: <COMMAND> <MESSAGE>")

    logger.stdin.write(bytes('QUIT\n', 'utf-8'))
    encrypt.stdin.write(bytes('QUIT\n', 'utf-8'))


asyncio.run(main())
