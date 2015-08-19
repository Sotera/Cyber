#!/usr/bin/python
# -*- coding: utf-8 -*-
# measure_keystrokes.py
# Syntax:   measure_keystrokes.py <username>
#
# Modified from: http://stackoverflow.com/questions/9130521/implementing-a-keystroke-time-measurement-function-in-python

__author__ = 'rburactaon'
from Tkinter import *
from time import time
import sys
import datetime

# Set User Name
if len(sys.argv) != 2:
    username = "unknown"
else:
    username = sys.argv[1]

# Initialize Output File
filename = "results/keytiming_" + username + "_" + str(int(time())) + ".csv"
f = open(filename, "w")
f.write("username\ttimestamp\tmodifiers\tkey_symbol\tkey_char\tdelta_t\n")

MAX_WPM = 0
prev_time = None
#start_time = end_time = 0
master = Tk()
e = Text(master)
e.pack()
e.focus_set()


def key(event):
    global MAX_WPM
    global prev_time
    modifiers = []
    del modifiers[:]

    # Decipher modifiers
    if event.state & 0x0001:
            modifiers.append('Shift')
    if event.state & 0x0002:
            modifiers.append('Caps Lock')
    if event.state & 0x0004:
            modifiers.append('Control')
    if event.state & 0x0008:
            modifiers.append('LeftAlt')
    if event.state & 0x0010:
            modifiers.append('NumLock')
    if event.state & 0x0080:
            modifiers.append('RightAlt')
    # if event.state & 0x0100:
    #         modifiers.append('Mouse 1')
    # if event.state & 0x0200:
    #         modifiers.append('Mouse 2')
    # if event.state & 0x0400:
    #         modifiers.append('Mouse 3')

    #if event.char == '\r':
    # if event.keysym == 'Control_R':
    #     e.unbind("<Key>")
    #     f.close()
    #     return
    #print "pressed", repr(event.char)

    end_time = datetime.datetime.now()
    delta_t = end_time.microsecond - start_time.microsecond
    # Write to File
    # Columns:  username  timestamp   modifiers   key_symbol  key_char delta_t
    f.write(username + '\t' + str(end_time) + '\t' + '-'.join(modifiers[:-1]) + '\t' +
            repr(event.keysym) + '\t' + repr(event.char) + '\t' + str(delta_t) + '\n')
    # FOR DEBUG
    if prev_time is None:
        prev_time = start_time
    key_interval = (end_time - prev_time).microseconds / 1e6
    wpm = (1 / key_interval) * 5
    if wpm > MAX_WPM:
        MAX_WPM = wpm
    prev_time = end_time
    print username + '\t' + str(end_time) + '\t' + '-'.join(modifiers[:-1]) + '\t' + \
          repr(event.keysym) + '\t' + repr(event.char) + '\t' + str(key_interval) + '\twpm: ' +\
          str(wpm) + '\tWPM_max: ' + str(MAX_WPM)

    modifiers[:] = []
    del modifiers[:]
# Main Loop
wpm_max = 0
e.bind("<Key>", key)
start_time = datetime.datetime.now()
mainloop()