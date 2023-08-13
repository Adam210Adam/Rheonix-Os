import win10toast
import random

threatValues = [True, False]

threatValue = random.choice(threatValues)

if threatValue:
    main = win10toast.ToastNotifier()
    main.show_toast(
        "Render & Security",
        """After 1 scan, Threats Found
It is recommended to check The Render & Security Tab In the Settings And Remove the Risk of the major detected virus."""
    )
else:
    exit()
    