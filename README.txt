## CS 4348.502 - Operating Systems Project 1 - Vigenere Cipher(Python)

### This is CLI program which implements Vigenere Cipher in a simple fashion. You can save passwords, encrypts, decrypts. The communication between each subprocess is done through pipes via asyncio.

### RUNNING INSTRUCTIONS
1. Ensure you have Python3
2. Run 'python3 driver.py log.txt'

### USAGE
> driver.py 'logfilename.txt'

IMPORTANT:
- IF YOU DON'T PUT ANY MESSAGE FOR 'password | encrypt | decrypt', program **will** prompt history menu
- TO VIEW HISTORY (not select), you can use the history command.

STDIN:

[SET A PASSWORD]
password 'message' |  (no argument will prompt history menu)

[ENCRYPT A WORD]
encrypt 'message' |  (no argument will prompt history menu)

[DECRYPT A WORD]
decrypt 'message' |  (no argument will prompt history menu)

history 'password | encrypt | decrypt' 

quit - exit program

> encrypt.py

STDIN:

ENCRYPT 'SOMETHING'

PASSKEY 'SOMETHING'

DECRYPT 'SOMETHING'

> logger.py 'logfilename.txt'

STDIN:

'COMMAND' 'COMMAND'

## FILE DIRECTORY
- README.md
- WRITE-UP.pdf
- driver.py
- encrypt.py
- logger.py
  
## OTHER
You can name the log file anyway you want. 
When running each individual program make sure you use each word on a seperate line.
