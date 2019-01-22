#!/bin/env bash

# John Haggerty, BNL
# 2017.08.21

# 2018a
#cd /data0/phnxrc/fnal/logfiles
# 2018b
cd /data1/phnxrc/fnal/logfiles

source ~/root/root_v6.12.04/bin/thisroot.sh
~/calcon/bin/emcallogcron.py
