from tkinter import *
from platform import version, system, release, processor
from psutil import sensors_battery
import re
import win10toast
import acaCLOG
import caoCLOG
import cdeCLOG
import dirCLOG
import driCLOG
import kerCLOG
import uuuCLOG
import BSCE
import random


battery = sensors_battery()
code = random.randint(0, 72898767876567829876256783643782987565748392017289876787656782987625678364378298756574839201)
_intsar = random.randint(1, 7)
_bscer = random.randint(0,1)

if _bscer == 1:
    
    if _intsar == 1:
        BSCE.bsce()
        acaCLOG.main(code=code)
    elif _intsar == 2:
        BSCE.bsce()
        caoCLOG.main(code=code)
    elif _intsar == 3:
        BSCE.bsce()
        cdeCLOG.main(code=code)
    elif _intsar == 4:
        BSCE.bsce()
        dirCLOG.main(code=code)
    elif _intsar == 5:
        BSCE.bsce()
        driCLOG.main(code=code)
    elif _intsar == 6:
        BSCE.bsce()
        kerCLOG.main(code=code)
    elif _intsar == 7:
        BSCE.bsce()
        uuuCLOG.main(code=code)
else:
    import random
    def c():
        import os
        os.system("cls")
    c()
    Username = input("Who Is gonna be using this computer?\n")
    c()
    Password = input("Enter a super rememberable password.\n")
    UserUserns = [Username]
    UserPasses = [Password]
    Users = list(zip(UserUserns, UserPasses))
    def load():
        import time
        def s(t):
            time.sleep(t)
        s(0.5)
        print("/ Loading")
        s(0.5)
        c()
        print("- Loading")
        s(0.5)
        c()
        print("\ Loading")
        s(0.5)
    for loading in range(random.randint(1,5)):
        load()
        main = Tk()
        main.title("Rheonix OS")
        main.state("zoomed")
        main.mainloop()