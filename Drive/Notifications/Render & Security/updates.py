import sys
import win10toast as w10t
import time
import random
import dddcccvvv
import playsound



if int(sys.argv[1]) > dddcccvvv.End:
    raise Exception("Update Does Not exist")
elif int(sys.argv[1]) < 1:
    raise Exception("Update Does Not exist")
else:
    print(f"Applying Update {sys.argv[1]}")
    time.sleep(2)
    wwws = w10t.ToastNotifier()
    www = "www."
    webs = ["render", "intelligente"]
    com = ".com"
    website = "".join([www, random.choice(webs), com])
    print(f"Shutout to {website}")
    wwws.show_toast(
        "Render & Security",
        f"Update {sys.argv[1]} Applied"
    )
    with open(f"Update {sys.argv[1]}.update", "w") as fsrc:
        fsrc.write("""
        What's New?

        Parent     Object
        _________  __________________
        Bug Fixes: Settings App not working properly
        Addingness: Clock App
        Addingness: New GUIs
        """)
    # In progress