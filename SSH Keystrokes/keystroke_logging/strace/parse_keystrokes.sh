#!/bin/bash
cat $1 | grep " = 1$" > keystrokes_$1
