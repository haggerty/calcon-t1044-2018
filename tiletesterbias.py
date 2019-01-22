#!/home/phnxrc/anaconda2/bin/python

import sys
import telnetlib
import sqlite3
import datetime

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

prefix = "$GS2"
# tile mapper 2018--offsets from 65.5 (Keithley or Wiener) + 2.5 (DAC) = 68V
vd = [400,420,430,440,440,510,1310,1310,1320,1320,1320,1320]

#Preamp SiPM Vop Gain
#1  1288 68.40 2.32E+05
#2  1307 68.42 2.30E+05
#3  1516 68.43 2.31E+05
#4  1517 68.44 2.29E+05
#5  1518 68.44 2.30E+05
#6  1287 68.51 2.28E+05
#   1303 68.51 2.29E+05
#7  1558 69.31 2.29E+05
#8  1620 69.31 2.29E+05
#9  1454 69.32 2.29E+05
#10 1575 69.32 2.30E+05
#11 1617 69.32 2.29E+05
#12 1691 69.32 2.30E+05
#   1485 69.33 2.31E+05
      
i = 0
for v in vd:
    s = '%s%02d%d\n\r' % (prefix,i,v)
    print s
    tn.write(s)
    print "reading..."
    g = tn.read_until(">")
    print g
    i+=1 

tn.write( "\n\r")
