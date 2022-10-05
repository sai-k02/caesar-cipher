import sys

# THE ARBITRARY MEMORY LOCATION (AKA SOME INTEGER BRO)
memloc = 0

#
mode = sys.stdin.readline().rstrip()

while mode != "halt":
    if mode == "read":
        # PRINTING EVALUATES TO THE STANDARD OUTPUT OF THE PROCESS CALLED "MEMORY"
        print(memloc)
        sys.stdout.flush()
    elif mode == "write":
        memloc = sys.stdin.readline().rstrip()

    mode = sys.stdin.readline().rstrip()
