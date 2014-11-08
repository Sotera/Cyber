SSH Keystrokes
==============

This project records the keystroke events from a SSH terminal session.

## Keystroke SSH Packet Recording
Snort was used to capture the keystroke events. Details of the installation and setup can be found in the snort directory.
<p> Snort Rule:
```
    alert tcp any any -> 192.168.0.10/32 22 \
      (msg: "keystroke"; fragbits: D; flags: AP; dsize: 32<>192; gid:x; sid:x; rev:x)
```

This produces the following alerts (/var/log/snort/alert):<p>
```
      11/07-13:27:48.929174  [**] [1:1:1] keystroke [**] [Priority: 0] {TCP} 192.168.1.23:19490 -> 192.168.0.10:22
      11/07-13:27:49.173180  [**] [1:1:1] keystroke [**] [Priority: 0] {TCP} 192.168.1.23:19490 -> 192.168.0.10:22
```

## Truth Data
Two different keystroke logging methods were used.

- Validating SSH keystroke packets: logged with strace of an SSH terminal session
- Timing of different user typing patters (digraph/trigraph timing, backspace/delete use, etc.): python program

### Keystroke logging with strace
Validating the packets are indeed those of keystrokes a method for recording the timing of key entry was needed. This was accomplished using the "Poor man's SSH keylogger" described by Diogo Monica (@diogomonica) in his blog https://diogomonica.com/poor-man-s-ssh-keylogger/.
<p> **_WARNING_** if you do not have your ssh keys set for passwordless login your password will be captured! <p>
```
    strace -ttt -e read -s 64 -x -o keystroke_ssh_truth_`date '+%Y%m%d_%H%M%S.%N'`.log ssh -Y 192.168.0.10
```
<P> With this log the keystrokes traces can be filtered using grep:<p>
```
    cat keystroke_ssh_truth_20141107_132525.123456789.log | grep " = 1$" > keystrokes_strace.log
```
<p> This produces output such as the following:
```
    1415399448.844153 read(4, "e", 16384)   = 1
    1415399449.346695 read(4, "x", 16384)   = 1
    1415399449.511329 read(4, "i", 16384)   = 1
    1415399449.638320 read(4, "t", 16384)   = 1
    1415399449.863464 read(4, "\r", 16384)  = 1
```
