#!/usr/bin/python
# -*- coding: utf-8 -*-
# reverse_time.py
# Syntax: reverse_time.py <user sessions file> <output file>
#       normalizes the time of each user session. T = Time - Max(Time) for each user.
#       would like to see the ?,"e","x","i","t","\n" sequence
__author__ = 'rburactaon'
import sys
import datetime
import numpy as np


# Check command line arguments
if len(sys.argv) != 3:
    print "Syntax:\treverse_time.py <user sessions file> <output file>"
    sys.exit(2)
else:
    usrsession = sys.argv[1]
    output = sys.argv[2]

print "Input File:\t", usrsession
print "Output File:\t", output

fout = open(output, 'w')
fout.write("source\tsource_port\tsource:port\tdtg\ttime\trev_time\trev_index\tdelta\tusername\n")

n = 0
lastsession = None
last_src = None
last_prt = None
last_usr = None
t_hist = list()

with open(usrsession, 'r') as fin:
    fin.readline()      # Skip Header
    for line in fin:
        n += 1
        (src, prt, srcprt, t, usr) = line.strip().split(',')
        if lastsession is None:
            t_hist.append(float(t))
        elif srcprt == lastsession:
            t_hist.append(float(t))
        else:
            TVEC = np.array(t_hist)
            TVEC.sort()
            RevTimes = TVEC-max(TVEC)
            RevTimes = RevTimes * (-1)
            DeltaT = np.ediff1d(TVEC, to_begin=999999999)
            NDX = range(0, len(RevTimes))
            for ii in range(0, len(TVEC)):
                dtg = datetime.datetime.fromtimestamp(TVEC[ii]).strftime('%Y-%m-%d %H:%M:%S')
                fout.write(last_src + '\t' + last_prt + '\t' + lastsession + '\t' + dtg + '\t' + str(TVEC[ii]) +
                           '\t' + str(RevTimes[ii]) + '\t' + str(NDX[-ii]) + '\t' + str(DeltaT[ii]) + '\t' +
                           last_usr + '\n')
            t_hist = list()
            t_hist.append(float(t))
        last_usr = usr
        last_src = src
        last_prt = prt
        lastsession = srcprt

    # Print last line
    TVEC = np.array(t_hist)
    TVEC.sort()
    RevTimes = TVEC-max(TVEC)
    RevTimes = RevTimes * (-1)
    DeltaT = np.ediff1d(TVEC, to_begin=999999999)
    NDX = range(0, len(RevTimes))
    for ii in range(0, len(TVEC)):
        dtg = datetime.datetime.fromtimestamp(TVEC[ii]).strftime('%Y-%m-%d %H:%M:%S')
        fout.write(last_src + '\t' + last_prt + '\t' + lastsession + '\t' + dtg + '\t' + str(TVEC[ii]) +
                   '\t' + str(RevTimes[ii]) + '\t' + str(NDX[-ii]) + '\t' + str(DeltaT[ii]) + '\t' +
                   last_usr + '\n')
fin.close()
fout.close()