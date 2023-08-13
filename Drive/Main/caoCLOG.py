def main(code):
    import os
    os.mkdir("Crash Logs")
    with open("Crash Logs\Crash Log.txt", "w") as clog:
        clog.write(f"""
        Intelligente Crash Log


        This is a crash log with information about the latest bsce. It took 1:30 hours half past 1. The cause
        was DRIVER_POWER_NOT_GREATER_OR_LESS was true. The Binary Output was {bin(code)}.
        """)