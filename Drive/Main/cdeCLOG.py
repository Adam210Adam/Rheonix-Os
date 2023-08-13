def main(code):
    import os
    os.mkdir("Crash Logs")
    with open("Crash Logs\Crash Log.txt", "w") as clog:
        clog.write(f"""
        Intelligente Crash Log


        This is a crash log with information about the latest bsce. It took 1:30 hours half past 1. The cause
        was ####################################. The Binary Output was ######################################.
        """)