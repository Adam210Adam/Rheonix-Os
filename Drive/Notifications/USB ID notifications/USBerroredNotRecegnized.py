from win10toast import ToastNotifier

nots = ToastNotifier()
nots.show_toast(
    "System",
    """Cannot Connect To USB
Failed To Connect
USB Unrecognized""",
)