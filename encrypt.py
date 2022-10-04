'''
https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Base.html


IMPLEMENT VIGENERE CIPHER
USING A Vigenere Tableau or Table
X = PLAINTEXT CHAR
Y = KEY CHAR

[MATCH KEY TO LENGTH OF EACH WORD]

MICHIGAN TECHNOLOGICAL UNIVERSITY
HOUGHTON HOUGHTONHOUGH TONHOUGNTO


[BROKEN DOWN INTO 5 LETTER BLOCKS]


MICHI GANTE CHNOL OGICA LUNIV ERSIT Y
HOUGH TONHO UGHTO NHOUG HTONH OUGHT O

[USING TABLE]
MICHI GANTE CHNOL OGICA LUNIV ERSIT Y
HOUGH TONHO UGHTO NHOUG HTONH OUGHT O
TWWNP ZOAAS WNUHZ BNWWG SNBVC SLYPM M

'''

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

    upper.rotate(key)
    lower.rotate(key)

    # # ROTATE BOTH UPPER AND LOWER
    upperRotatedString = ''.join(list(upper))
    lowerRotatedString = ''.join(list(lower))

    # # MAP EACH CHARACTER OF INPUT TO THE NEW CORRESPONDING CHARACTER
    encryptString = encryptString.translate(str.maketrans(
        string.ascii_uppercase, upperRotatedString))
    encryptString = encryptString.translate(str.maketrans(
        string.ascii_lowercase, lowerRotatedString))

    return encryptString


def decryptCesar(key: int):
    decryptString = ""
    return decryptString


def main():
    try:
        inputString = sys.argv[1]
        key = int(sys.argv[2])
        encryptedString = encryptCesar(inputString, key)
        print(encryptedString)
    except:
        print("usage: python encrypt.py <stringToEncrypt> <intKey>")


main()
