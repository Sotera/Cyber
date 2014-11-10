#!/usr/bin/python
# -*- coding: utf-8 -*-
# parse_alerts.py
# Syntax: parse_alerts.py <alerts file> <output file>
#     Parses the snort log "alerts" and creates a CSV file for ETL
#
__author__ = 'rburactaon'
import sys
import datetime


# Check command line arguments
if len(sys.argv) != 3:
    print "Syntax:\tparse_alerts <alerts file> <output file>"
    sys.exit(2)
else:
    alerts = sys.argv[1]
    output = sys.argv[2]

print "Input File:\t", alerts
print "Output File:\t", output

fout = open(output, 'w')
fout.write("stamp\tmu\tsrc_ip\tsrc_port\tdst_ip\tdst_port\n")

with open(alerts, 'r') as fin:
    for line in fin:
        cols = line.strip().split(' ')

        # Reformat date time string
        (dtgpart, mu_sec) = cols[0].split('.')
        dtgpart2014 = "2014/"+dtgpart
        dtg = datetime.datetime.strptime(dtgpart2014, "%Y/%m/%d-%H:%M:%S")
        stamp = dtg.strftime("%Y-%m-%d %H:%M:%S")

        # Parse Source IP:PORT
        src = cols[9]
        (src_ip, src_port) = src.split(':')

        # Parse Destination IP:PORT
        dst = cols[11]
        (dst_ip, dst_port) = dst.split(':')

        print stamp + "\t" + mu_sec + "\t" + src_ip + "\t" + src_port + "\t" + dst
        fout.write(stamp + "\t" + mu_sec + "\t" + src_ip + "\t" + src_port + "\t" + dst_ip + "\t" + dst_port + "\n")
fin.close()
fout.close()