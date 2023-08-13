import time
import json
from pprint import pprint
cd = r"C:\Users\Adam\Desktop\Render\Drive"
Main = r"\Main"
Notifs = r"\Notifications"
Program = r"\ProgramFilesX86"

for number in range(122):
    print(cd + "Execute ", str(number))
    time.sleep(0.05)
    print(cd + Main + "Execute ", str(number))
    time.sleep(0.05)
    print(cd + Program + "Execute ", str(number))
    time.sleep(0.05)
print(open("config.json").readlines())
