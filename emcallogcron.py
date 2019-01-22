#!/bin/env python

# Log EMCAL temperatures and currents from controller
# John Haggerty, BNL, 2017.08.21

import sys
import telnetlib
import time
from ROOT import TFile, TTree, TObject
from array import array
import datetime
import os.path

HOST = "192.168.100.110"
PORT = "9760"

try:
    tn = telnetlib.Telnet(HOST,PORT)
except Exception as ex:
    print ex
    print "cannot connect to controller... give up"
    sys.exit()

#rootfile = 'emcal_highbay.root'
rootfile = 'emcal_fermilab.root'
rootfile_exists = os.path.isfile(rootfile)

if rootfile_exists:
    print 'appending to ',rootfile
    f = TFile( rootfile, 'update' )
    TT = f.Get("TT")
else:
    print 'creating new ',rootfile
    f = TFile( rootfile, 'recreate' )
    TT = TTree( 'TT', 'EMCAL temperature and current' )

start = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

ntemperatures = 32
ncurrents = 64

t = array( 'd', [ 0.0 ] )
temperature = array( 'd', ntemperatures*[ 0 ] )
leakage = array( 'd', ncurrents*[ 0 ] )

if rootfile_exists:
    TT.SetBranchAddress('time',t);
    TT.SetBranchAddress('temperature',temperature);
    TT.SetBranchAddress('leakage',leakage);
else:
    TT.Branch( 'time', t, 'time/D' )  
    TT.Branch( 'temperature', temperature, 'temperature['+str(ntemperatures)+']/D' )  
    TT.Branch( 'leakage', leakage, 'leakage['+str(ncurrents)+']/D' ) 

tn.write("\n\r")

t[0] = time.time()
x = [0]
tn.write( "$T0\n\r")
x = tn.read_until(">").split()
#print x
    
for j in range(ntemperatures):
    temperature[j] = float(x[j])
    print 'T ',j,temperature[j]

y = [0]
tn.write( "$I0\n\r")
y = tn.read_until(">").split()
#print y                         

for j in range(ncurrents):
    leakage[j] = float(y[j])
    print 'I ',j,leakage[j]
        
TT.Fill()
           
f.Write("",TObject.kOverwrite)
f.Close()
