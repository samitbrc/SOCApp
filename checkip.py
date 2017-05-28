from tkinter import *
import dns.resolver
import dns.query



pwin1 = Tk()
pwin1.title("IP Reputation Check")
pwin1.geometry("400x500+300+2")
pwin1.configure(background="snow4")

Label(text="Enter the IP for Reputation Check", fg="honeydew", bg="snow4", font=("Helvetica", 10)).pack()
e = Entry(pwin1)
e.pack()
e.focus_set()


Label(text="Application Developed by Amiya and Samit", fg="honeydew", bg="snow4", font=("Helvetica", 9)).place(x=160, y=475)


def callback():
    checkip = e.get()
    listed = 0
    nlisted = 0
    Label(text="IP Address Check Completed").place(x=60, y=100)


    bls = ["zen.spamhaus.org", "spam.abuse.ch", "cbl.abuseat.org", "virbl.dnsbl.bit.nl", "dnsbl.inps.de",
           "ix.dnsbl.manitu.net", "dnsbl.sorbs.net", "bl.spamcannibal.org", "bl.spamcop.net",
           "xbl.spamhaus.org", "pbl.spamhaus.org", "dnsbl-1.uceprotect.net", "dnsbl-2.uceprotect.net",
           "dnsbl-3.uceprotect.net", "db.wpbl.info"]

    myIP = checkip


    for bl in bls:
        #Label(text="IP Address Check in Progress........").place(x=60, y=150)
        #Label(text="Reputation Check in Progress.......").place(x=90, y=75)
        try:

            my_resolver = dns.resolver.Resolver()
            query = '.'.join(reversed(str(myIP).split("."))) + "." + bl
            answers = my_resolver.query(query, "A")
            answer_txt = my_resolver.query(query, "TXT")

            print('IP: %s IS listed in %s (%s: %s)' % (myIP, bl, answers[0], answer_txt[0]))
            listed = listed + 1

        except dns.resolver.NXDOMAIN:
            print('IP: %s is NOT listed in %s' % (myIP, bl))
            nlisted = nlisted + 1

    if listed > 0:
        Label(text="Listed in "+str(listed) + "  Sites").place(x=60, y=130)
    if nlisted > 0:
        Label(text="Not Listed in " + str(nlisted) + "  Sites").place(x=60, y=160)


b = Button(pwin1, text = "Check", width = 10, command = callback)
b.pack()
b.place(x=160, y=50)


b = Button(pwin1, text = "Close", width = 10, command = quit)
b.pack()
b.place(x=10, y=460)

mainloop()