# ENCRYPT FUNCTION
import collections
import string
import sys


def encryptCesar(input: str, key: int) -> str:
    # DEFINE STRING TO CONTAIN ENCRYPTED STRING
    encryptString = input

    # DEFINE CHARACTERS TO ROTATE BY
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(key*-1)
    lower.rotate(key*-1)

    # # ROTATE BOTH UPPER AND LOWER
    upperRotatedString = ''.join(list(upper))
    lowerRotatedString = ''.join(list(lower))

    # # MAP EACH CHARACTER OF INPUT TO THE NEW CORRESPONDING CHARACTER
    encryptString = encryptString.translate(str.maketrans(
        string.ascii_uppercase, upperRotatedString))
    encryptString = encryptString.translate(str.maketrans(
        string.ascii_lowercase, lowerRotatedString))

    return encryptString


def decryptCesar(input: str, key: int):
    # DEFINE STRING TO CONTAIN ENCRYPTED STRING
    decryptString = input

    # DEFINE CHARACTERS TO ROTATE BY
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(key)
    lower.rotate(key)

    # # ROTATE BOTH UPPER AND LOWER
    upperRotatedString = ''.join(list(upper))
    lowerRotatedString = ''.join(list(lower))

    # # MAP EACH CHARACTER OF INPUT TO THE NEW CORRESPONDING CHARACTER
    decryptString = decryptString.translate(str.maketrans(
        string.ascii_uppercase, upperRotatedString))
    decryptString = decryptString.translate(str.maketrans(
        string.ascii_lowercase, lowerRotatedString))

    return decryptString


def process(passKey: dict, command: str, message: str, availableCommands: set):
    # HANDLE INCORRECT COMMAND

    # DEFINE RETURN DICTIONARY
    returnDict = {}
    if command in availableCommands:
        if passKey['key'] != '' or command == "PASSKEY":
            if command == 'ENCRYPT':
                returnDict['RESULT'] = 'RESULT'
                returnDict['MESSAGE'] = encryptCesar(
                    message, len(passKey['key']))
            elif command == 'DECRYPT':
                returnDict['RESULT'] = 'RESULT'
                returnDict['MESSAGE'] = decryptCesar(
                    message, len(passKey['key']))
            elif command == 'PASSKEY':
                passKey['key'] = message
                returnDict['RESULT'] = 'RESULT'
                returnDict['MESSAGE'] = 'Password set to ' + message + '.'
            else:
                returnDict['RESULT'] = 'ERROR'
                returnDict['MESSAGE'] = 'INCORRECT COMMAND'
        else:
            returnDict['RESULT'] = 'ERROR'
            returnDict['MESSAGE'] = 'Password not set.'
    else:
        returnDict['RESULT'] = 'ERROR'
        returnDict['MESSAGE'] = 'Incorrect command.'

    return returnDict


# MUST USE A MUTABLE OBJECT DUE TO STRING BEING IMMUTABLE
passKey = {'key': ''}
availableCommands = set(['ENCRYPT', 'PASSKEY', 'DECRYPT'])
command = sys.stdin.readline().rstrip()
while (command != 'QUIT'):

    message = sys.stdin.readline().rstrip()
    output = process(passKey=passKey, command=command,
                     message=message, availableCommands=availableCommands)
    result = output['RESULT']
    message = output['MESSAGE']
    print(result)
    sys.stdout.flush()
    print(message)
    sys.stdout.flush()
    command = sys.stdin.readline().rstrip()
