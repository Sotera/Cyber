#!/usr/bin/python
# -*- coding: utf-8 -*-
# parse_wireshark.py
# Syntax: parse_wireshark.py <wireshark file> <output file>
#     Parses the filtered snort logs using wireshark
#(tcp.len == 48 or tcp.len==52) && !(_ws.expert) && (ssh)
__author__ = 'rburactaon'
import sys
import datetime
import time


# Check command line arguments
if len(sys.argv) != 3:
    print "Syntax:\tparse_wireshark <wireshark file> <output file>"
    sys.exit(2)
else:
    alerts = sys.argv[1]
    output = sys.argv[2]

print "Input File:\t", alerts
print "Output File:\t", output

# Write header to output file
fout = open(output, 'w')
fout.write("stamp\tmu\tdelta_t\tsrc_ip\tsrc_port\tdst_ip\tdst_port\n")

hist = dict()

with open(alerts, 'r') as fin:
    for line in fin:
        cols = line.strip().split(' ')

        # Reformat date time string
        (dtgpart, mu_sec) = cols[0].split('.')
        dtgpart2014 = "2014/"+dtgpart
        dtg = datetime.datetime.strptime(dtgpart2014, "%Y/%m/%d-%H:%M:%S")
        stamp = dtg.strftime("%Y-%m-%d %H:%M:%S")
        #t_sec = float(datetime.datetime.strptime(str(dtg), "%Y-%m-%d %H:%M:%S").strftime("%s"))+float(mu_sec)/1e6
        t_sec = float(time.mktime(time.strptime(stamp, "%Y-%m-%d %H:%M:%S")))+float(mu_sec)/1e6
        # Parse Source IP:PORT
        src = cols[9]
        (src_ip, src_port) = src.split(':')

        # Parse Destination IP:PORT
        dst = cols[11]
        (dst_ip, dst_port) = dst.split(':')

        if src in hist:
            delta_t = t_sec - hist[src]
        else:
            delta_t = 9.99e999

        #print stamp + "\t" + mu_sec + "\t" + src_ip + "\t" + src_port + "\t" + dst
        fout.write(stamp + "\t" + mu_sec + "\t" + str(delta_t) + "\t" + src_ip + "\t" + src_port +
                   "\t" + dst_ip + "\t" + dst_port + "\n")
        hist[src] = t_sec
fin.close()
fout.close()