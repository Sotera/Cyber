#!/bin/bash
strace -ttt -o strace_ssh_`date '+%Y%m%d_%H%M%S.%N'`.log -e read -s64 -x ssh -Y $1

