import asyncio
from asyncio.subprocess import PIPE
import sys

'''
loggerOutput = await logger.stdout.readline()


'''


async def main():
    # CREATE TWO PROCESSES FOR LOGGER AND ENCRYPT
    logger = await asyncio.create_subprocess_exec(
        "python3", "logger.py", "output.txt", stdin=PIPE, stdout=PIPE)
    # WRITE THE INITIAL START

    # DEFINE USER INPUT
    userInput = ''

    while (userInput != 'QUIT'):
        print("Input: ", end='')
        userInput = input()
        if(userInput == 'QUIT'):
            logger.stdin.write(bytes('QUIT\n', 'utf-8'))
            sys.exit(0)
        else:
            logger.stdin.write(bytes(''+userInput+'\n', 'utf-8'))

        await logger.wait()

    

asyncio.run(main())
