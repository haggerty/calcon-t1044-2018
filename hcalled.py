#!/home/phnxrc/anaconda2/bin/python

import sys
import telnetlib
import sqlite3
import datetime
import time

# Turn on or off LED's in Inner and Outer HCAL, mask all on or off

# John Haggerty, BNL, 2016.03.18

HOST = "192.168.100.120"
PORT = "9760"

try:
    tn = telnetlib.Telnet(HOST,PORT)
except Exception as ex:
    print ex
    print "cannot connect to controller... give up"
    sys.exit()

tn.write( "\n\r")
tn.write( "\n\r")

if len(sys.argv) == 1:
    print "usage: hcalled.py [on|off]"
    sys.exit(0)

arg1 = str(sys.argv[1]).lower()

if arg1 =="on":
    
    dac_inner = 2000
    dac_outer = 2000

    nleds = 5
    print "Setting IHCAL DAC to "+str(dac_inner)+" OHCAL DAC to "+str(dac_outer)
    for i in range(nleds):
# inner
        setdac = "$LS0"+str(i)+str(dac_inner)
        print setdac
        tn.write(setdac+"\n\r")
        z = tn.read_until(">").split()
# outer
        setdac = "$LS1"+str(i)+str(dac_outer)
        print setdac
        tn.write(setdac+"\n\r")
        z = tn.read_until(">").split()
    tn.write( "\n\r")
                        

    tn.write("$LM0FFFF")
    g = tn.read_until(">")
#    print g
    tn.write( "\n\r")

    tn.write("$LM1FFFF")
    g = tn.read_until(">")
#    print g
    tn.write( "\n\r")

    print "LED mask = FFFF (all on)"

else:
    nleds = 5
    dac = "0000"
    print "Setting DAC to "+str(dac)
    for i in range(nleds):
# inner
        setdac = "$LS0"+str(i)+str(dac)
        print setdac
        tn.write(setdac+"\n\r")
        z = tn.read_until(">").split()
# outer
        setdac = "$LS1"+str(i)+str(dac)
        print setdac
        tn.write(setdac+"\n\r")
        z = tn.read_until(">").split()
    tn.write( "\n\r")

    tn.write("$LM00000")
    g = tn.read_until(">")
#    print g
    tn.write( "\n\r")

    tn.write("$LM10000")
    g = tn.read_until(">")
#    print g
    tn.write( "\n\r")

    print "LED masks = 0 (all off)"
    
