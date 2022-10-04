def main():
	print(encryptVigenere("input"))

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

def encryptVigenere(input: str, key: str) -> str:
	return input

# FUNCTION WILL GET THE CORRESPONDING LETTER BASED ON THE VIGENERE TABLEAU
# USE TOENCRYPTCHAR FOR ROWS AND KEY FOR COLUMNS
def getEncryptLetter(toEncryptChar: str, keyChar: str) -> str:
	return toEncryptChar + keyChar % 26

# USE decryptChar for the column in the row to look for and keyChar as the row to use 
# FUNCTION WILL GET THE CORRESPONDING LETTER BASED ON THE VIGENERE TABLEAU
def getDecryptLetter(decryptChar: str, keyChar: str) -> str:
	return 

main()
