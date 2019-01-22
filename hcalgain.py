#!/home/phnxrc/anaconda2/bin/python

import sys
import telnetlib
import sqlite3
import datetime
import time

# Inner HCAL has switch high/normal gain

# John Haggerty, BNL, 2018.02.10

HOST = "192.168.100.120"
PORT = "9760"

if len(sys.argv) == 1:
    print "usage: hcalgain.py [high|normal]"
    sys.exit(0)

arg1 = str(sys.argv[1]).lower()

try:
    tn = telnetlib.Telnet(HOST,PORT)
except Exception as ex:
    print ex
    print "cannot connect to controller... give up"
    sys.exit()

tn.write( "\n\r")
tn.write( "\n\r")

if arg1 =="high":

    tn.write("$A0h")
    g = tn.read_until(">")
    print g
    tn.write( "\n\r")
    
    print "HCAL high gain enabled"

else:
    tn.write("$A0n")
    g = tn.read_until(">")
    print g
    tn.write( "\n\r")
    
    print "HCAL gain set to normal (low)"
