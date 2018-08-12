import sys
import commands
import time

# Taking the process name, the script for restart path and the script name from console arguments

process = sys.argv[1]
path = sys.argv[2]
script = sys.argv[3]
secs = sys.argv[4]

print "Process control enable for " + process

while(1):
    # Running command ps -A for all active process names

    print 'running ps -A'
    output = commands.getoutput('ps -A')

    # If the process is alive: NOTHING TO DO

    if process in output:
        print  process + " is alive"

    # If the process is not alive: there will be a navigation to the script path and then a call to that script

    else:
        print process + " is dead -> PROCEDURE:"
        print "\t\tnavigating into " + path
        output = commands.getoutput('cd ' + path)
        print "\t\texecute " + script
        output = commands.getoutput('./' + script)

    time.sleep(int(secs))