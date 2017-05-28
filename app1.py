import subprocess
from tkinter import *

pwin = Tk()
pwin.title("SOC Application")
pwin.geometry("500x500+200+20")
pwin.configure(background='snow4')


Label(text="SOC Daily Activity Application", fg="honeydew", bg="snow4", font=("Helvetica", 16)).pack()
separator = Frame(height=4, bd=2, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

separator = Frame(height=3, bd=2, relief=SUNKEN).place(x=5, y=10)
#separator.pack(fill=X, padx=5, pady=5)
Label(text="Application Developed by Amiya and Samit", fg="honeydew", bg="snow4", font=("Helvetica", 9)).place(x=260, y=475)

def callback():
    subprocess.call('checkip.py 1', shell=True)



def callback2():
    print("\nFuture Development\n")
    Label(text="Future Development").place(x=160, y=175)

def callback3():
    print("\nFuture Development\n")
    Label(text="Future Development").place(x=160, y=175)


Label(text="IP Reputation",fg="white", bg="black").place(x=10, y=50)
b = Button(pwin, text="Check IP", command=callback)
b.pack(side = LEFT, pady=5, padx=0)
b.place(x=10,y=80)

b = Button(pwin, text="Quit", command=pwin.quit)
b.pack(side = LEFT, pady=5, padx=0)
b.place(x=10,y=460)

Label(text="Port Reputation",fg="white", bg="black").place(x=110, y=50)
b = Button(pwin, text="Port Reputation", command=callback2)
b.pack(side = LEFT, pady=5, padx=0)
b.place(x=110,y=80)

Label(text="Port Scan",fg="white", bg="black").place(x=230, y=50)
b = Button(pwin, text="Port Scan", command=callback3)
b.pack(side = LEFT, pady=5, padx=0)
b.place(x=230,y=80)


mainloop()