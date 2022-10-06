## CS 4348.502 - Operating Systems Project 1 - Caesar Cipher(Python)

### This is CLI program which implements Caesar Cipher in a simple fashion. You can save passwords, encrypts, decrypts. The communication between each program is done through subprocesses via asyncio.

### RUNNING INSTRUCTIONS
1. Ensure you have Python3
2. Run 'python3 driver.py log.txt'

### USAGE
> driver.py 'logfilename.txt'


STDIN:

password 'message'

encrypt 'message'

decrypt 'message'

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
