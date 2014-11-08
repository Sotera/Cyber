# keystroke_logging
Generation of truth data. Truth during live capture can be optained using strace. Detailed typing statistics can be obtained for each user by having he/she run the measure_keystrokes.py application in the typing_metrics folder. 

## strace
- ssh_keycapture.sh can be used in lieu of the ssh command in linux. This will create a logfile of your ssh session recording all of the keystrokes entered into the terminal window. 
- parse_keystrokes.sh: filters the created log file for only the keystrokes


## typing_metrics
A modified Tkinter application was created to timing each keystroke entered into a input gui. Original code described in http://stackoverflow.com/questions/9130521/implementing-a-keystroke-time-measurement-function-in-python

- measure_keystrokes.py: opens an input window to capture typing sample
- aggregate_digraphs.py: parses the results file for digraphs and computes the delta time between each key press
