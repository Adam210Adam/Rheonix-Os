from tkinter import *
from os import startfile
def bsce():
    rtt = Tk()
    rtt.title("Render BSCE Moment")
    rtt.state("zoomed")
    rtt.configure(bg="blue")
    sadface = Label(rtt, text="(:", font=("Arial", 140), bg="blue", fg="white").place(x=10, y=10)
    Label(rtt, text="Your Computer Crashed", bg="blue", fg="white", font=("Arial", 30)).place(x=10, y=220)
    prc=Label(text=f"100%", bg="blue", fg="white", font=("Arial", 30)).place(x=10, y=266)
    
        
    
    rtt.mainloop()
bsce()