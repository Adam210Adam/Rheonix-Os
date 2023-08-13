import sys
import time
import os


def cls():
    os.system("cls")
lange = sys.argv[1]

cls()
print(f"Applying Update {lange}")
time.sleep(3)
for NUM in range(101):
    cls()
    print("\n\n\n\n\n\n\n\n\n")
    print("                    Hicap             ")
    print("          _______________________________")
    print(f"         | Applying Patch {NUM} of 100           |")
    print("         | Please wait!                |")
    print("         | ⚠️  Do not close your PC    |")
    print("         _______________________________")
    time.sleep(0.3)