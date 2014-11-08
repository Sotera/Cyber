#!/usr/bin/python
# -*- coding: utf-8 -*-
# aggregate_digraphs.py
# Syntax:   aggregate_digraphs.py <keytimings_file>
#
# Input: output file from 'measure_keystrokes.py'
#
__author__ = 'rburactaon'
import sys
import csv

# Initilize Files
inputfile = ''
outputfile = ''
username = ''
filtfile = ''

# Process command line arguments
if len(sys.argv) != 4:
    print sys.argv
    print len(sys.argv)
    print "aggregate_digraphs.py <infile> <outfile> <username name>"
    exit()
else:
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    filtfile = "filt_" + outputfile
    username = sys.argv[3]
print 'Input file is: ', inputfile
print 'Output file is: ', outputfile
print 'Filtered Output is: ', filtfile
print 'User is: ', username

# Initialize Output
#infile = open(inputfile, "r")
outfile = open(outputfile, "w")
outfile.write("digraph\tdelta\tuser\n")

# Initial Variables
lastkey = None
laststamp = ""
lastmod = ""
data = dict()

# Process File
with open(inputfile, 'r') as csvfile:
    keyreader = csv.reader(csvfile, delimiter='\t', quotechar='\'')
    next(keyreader,None) # Skip Header
    for row in keyreader:
        (user, stamp, mods, key_symb, key_char, delta_t) = row
        key = mods + " " + key_symb
        if user!='unknown':
            username = user
        #if (key == '\\r' or key == ' '):
        #    continue
        if lastkey is None:
            lastmod = mods
            lastkey = key
            laststamp = stamp
            continue
        else:
            #digraph = "{ " + lastkey + " }-{ " + key_symb + " }"
            digraph = lastkey + " - " + key
            delta = float(stamp) - float(laststamp)
            if delta < 0.5:
                if digraph in data:
                    keyval = data[digraph]
                    n = keyval[0] + 1
                    key_min = min(keyval[1], delta)
                    key_max = max(keyval[3], delta)
                    key_avg = (keyval[2]*keyval[0] / n) + (delta / n)
                else:
                    n = 1
                    key_min = delta
                    key_avg = delta
                    key_max = delta
                val = [n, key_min, key_avg, key_max]
                data[digraph] = val
            outfile.write(digraph + "\t" + str(delta) + "\t" + username + "\n")
            lastkey = key
            laststamp = stamp
            lastmods = mods
csvfile.close()
outfile.close()

f = open(filtfile, 'w')
f.write("digraph\tcount\tdelta_min\tdelta_avg\tdelta_max\tuser\n")
for key in data:
    val = data[key]
    f.write(key + '\t' + str(val[0]) + '\t' + str(val[1]) + '\t' +
            str(val[2]) + '\t' + str(val[3]) + '\t' + username + '\n')

f.close()
