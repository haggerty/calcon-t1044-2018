#!/home/phnxrc/anaconda2/bin/python

# This is a little menu to run shell commands from a gui

# John Haggerty, BNL
# Originally appearing in phenix now for t1044
# 2016.03.20

from Tkinter import *
import os
import sys

# list of button names and their associated shell commands

emcalcommands = [
    ["EMCAL bias tweaks(g = 2.3E5)","~/calcon/bin/emcalbias.py &"],
    ["EMCAL LED ON","~/calcon/bin/emcalled.py on &"],
    ["EMCAL LED OFF","~/calcon/bin/emcalled.py off &"],
    ["EMCAL TP ON","~/calcon/bin/emcaltp.py on &"],
    ["EMCAL TP OFF","~/calcon/bin/emcaltp.py off &"],
    ["EMCAL gain stabilizer ON","~/calcon/bin/emcalstabilizer.py on &"],
    ["EMCAL gain stabilizer OFF","~/calcon/bin/emcalstabilizer.py off &"],
    ["EMCAL high gain","~/calcon/bin/emcalgain.py high &"],
    ["EMCAL normal gain","~/calcon/bin/emcalgain.py normal &"],
    ["EMCAL temperatures","~/calcon/bin/emcaltemp.py 0 4&"]
     ]

hcalcommands = [
    ["HCAL bias tweaks (g = 2.3E5)","~/calcon/bin/hcalbias.py &"],
    ["HCAL LED ON","~/calcon/bin/hcalled.py on &"],
    ["HCAL LED OFF","~/calcon/bin/hcalled.py off &"],
    ["HCAL TP ON","~/calcon/bin/hcaltp.py on &"],
    ["HCAL TP OFF","~/calcon/bin/hcaltp.py off &"],
    ["IHCAL normal gain","~/calcon/bin/hcalgain.py normal &"],
    ["IHCAL high gain","~/calcon/bin/hcalgain.py high &"],
    ["HCAL gain stabilizer ON","~/calcon/bin/hcalstabilizer.py on &"],
    ["HCAL gain stabilizer OFF","~/calcon/bin/hcalstabilizer.py off &"],
    ["HCAL temperatures","~/calcon/bin/hcaltemp.py 1 &"],
    ["Tile tester LED on","~/calcon/bin/tiletesterled.py on &"],
    ["Tile tester LED off","~/calcon/bin/tiletesterled.py off &"]
     ]

class App:

    def __init__(self, master):
        
        frame = Frame(master)
        frame.pack()
        
        homedir = os.getenv('HOME','/')
        logo_image = homedir + "/calcon/sPHENIX.gif"
        print logo_image
        
        try:
            f = open( logo_image )
            f.close()
            logo = PhotoImage(file=logo_image)
            self.lbl = Label( frame, image=logo, text="sPHENIX"  ) 
            self.lbl.logo = logo
        except IOError:
            print 'error opening ',logo_image,', ignoring'
            self.lbl = Label( frame, text="sPHENIX"  )
            
        self.lbl.configure(background='white')
        self.lbl.pack(side=TOP,fill=X)

        button_frame = Frame(frame)
        exit_frame = Frame(frame)

        button_frame.pack(side=TOP,fill=X)
        exit_frame.pack(side=TOP,fill=X)

        left_frame = Frame(button_frame)
        middle_frame = Frame(button_frame)
        right_frame = Frame(button_frame)

        left_frame.pack(side=LEFT,fill=BOTH)
        middle_frame.pack(side=LEFT,fill=BOTH)
        right_frame.pack(side=RIGHT,fill=BOTH)

        for c in emcalcommands:
          self.sh = Button( left_frame, text=c[0],
                            command=lambda arg1=c[1]: self.shell(arg1),
                            anchor=W ) 
          self.sh.pack(side=TOP,fill=X)

        for c in hcalcommands:
          self.sh = Button( right_frame, text=c[0],
                            command=lambda arg1=c[1]: self.shell(arg1),
                            anchor=W ) 
          self.sh.pack(side=TOP,fill=X)

        self.quit = Button(exit_frame, text="Exit", command=frame.quit, anchor=CENTER)
        self.quit.pack(side=TOP,fill=X)
        
# this executes the shell command "x" and prints the result
    def shell(self,x):
        result = os.system( x )
            
# down here is the main program

root = Tk()
root.title("T1044-2017a")            
app = App(root)
            
root.mainloop()
