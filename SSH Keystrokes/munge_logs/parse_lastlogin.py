#!/usr/bin/python
# -*- coding: utf-8 -*-
# parse_lastlogin.py
# Syntax: parse_lastlogins.py <login file> <output file>
#     login file obtained via the "last" command in linux.
#     $> last -a -d -F -w > login_file.txt
__author__ = 'rburactaon'
import sys
import datetime
import re

# Check command line arguments
if len(sys.argv) != 3:
    print "Syntax:\tparse_lastlogin.py <login file> <output file>"
    sys.exit(2)
else:
    logins = sys.argv[1]
    output = sys.argv[2]

print "Input File:\t", logins
print "Output File:\t", output

fout = open(output, 'w')
fout.write("username\tterminal\tstarttime\tendtime\tduration_sec\tlocation\n")

n = 0
with open(logins, 'r') as fin:
    for line in fin:
        n += 1
        cols = re.split('\s+',line.strip())
        if  len(cols)== 15:
            user = cols[0]
            terminal = cols[1]
            start_str = ' '.join(cols[2:7])
            #print "start_str:\t", start_str
            end_str = ' '.join(cols[8:13])
            #print "end_str:\t", end_str
            durstr = cols[13]
            #print "durstr:\t", durstr
            location = cols[14]

        elif len(cols)== 11:
            print "User still logged in on line ", n
            print line.strip('\n')
            continue
        else:
            print "No user login info on line ", n
            print line.strip('\n')
            continue

        # Reformat date time string
        t0 = datetime.datetime.strptime(start_str, "%a %b %d %H:%M:%S %Y")
        t1 = datetime.datetime.strptime(end_str, "%a %b %d %H:%M:%S %Y")
        starttime = t0.strftime("%Y-%m-%d %H:%M:%S")
        endtime = t1.strftime("%Y-%m-%d %H:%M:%S")

        # Reformat duration from 00:00 to seconds
        #print "Hour:\t", durstr[1:3]
        #print "Min:\t", durstr[4:6]
        try:
            duration = str(int(durstr[1:3])*3600 + (int(durstr[4:6])*60))
        except:
            print "durstr:\t", durstr
            # Duration overlaps a day: i.e. (1+00:47)
            durstr = re.sub('[()]','',durstr)
            print "durstr:\t", durstr
            (days,hrsmins) = re.split('\+',durstr)
            duration = str(24*3600*int(days) + (int(hrsmins[0:2])*3600) + (int(hrsmins[3:5])*60))
            print "Duration over a day:\t",duration
            pass

        #fout.write("username\tterminal\tstarttime\tendtime\tduration\tlocation\n")
        #print user + "\t" + terminal + "\t" + starttime + "\t" + endtime + "\t" + duration + "\t" + location
        fout.write(user + "\t" + terminal + "\t" + starttime + "\t" + endtime + "\t" + duration + "\t" + location + "\n")
fin.close()
fout.close()