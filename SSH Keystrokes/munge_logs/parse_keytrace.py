#!/usr/bin/python
# -*- coding: utf-8 -*-
# parse_keytrace.py
# Syntax: parse_keytraces.py <strace file> <output file>
#
__author__ = 'rburactaon'
import sys
import datetime
import re

# Check command line arguments
if len(sys.argv) != 5:
    print "Syntax:\tparse_keytrace.py <strace log> <output file> <user> <location>"
    sys.exit(2)
else:
    keys = sys.argv[1]
    output = sys.argv[2]
    user = sys.argv[3]
    location = sys.argv[4]

print "Input File:\t", keys
print "Output File:\t", output
print "Username:\t", user
print "Location:\t", location

fout = open(output, 'w')
fout.write("dtg\tstamp\tkeysymb\tuser\tlocation\n")

n = 0
with open(keys, 'r') as fin:
    for line in fin:
        n += 1
        if re.findall("read\(4, ", line.strip('\n')):
            cols = re.split('\s+',line.strip())
            if len(cols)== 6:
                stamp = cols[0]
                keysymb = cols[2]
            else:
                if re.findall("read\(4, \" \",",line.strip('\n')):
                    stamp = cols[0]
                    keysymb = '\"space\"'
                    print "Space found at line ", n
                    print line.strip('\n')
                else:
                    print "Unknown format at line ", n
                    print line.strip('\n')
                    continue
        else:
            continue
        # Reformat date time string
        dtg = datetime.datetime.fromtimestamp(float(stamp)).strftime("%Y-%m-%d %H:%M:%S")
        #fout.write("dtg\tstamp\tkeysymb\tuser\tlocation\n")
        fout.write(dtg + "\t" + stamp + "\t" + keysymb + "\t" + user + "\t" + location + "\n")
fin.close()
fout.close()