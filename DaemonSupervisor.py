import time
import logging
import os
import sys
import subprocess
from threading import Thread

# Create and configure logger
logging.basicConfig(filename='logs.log',level=logging.DEBUG)

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

def checkIfProcessRunning(name):
        output = []
        cmd = "ps -aef | grep -i '%s' | grep -v 'grep' | awk '{ print $2 }' > /tmp/out"
        os.system(cmd % name)
        with open('/tmp/out', 'r') as f:
            line = f.readline()
            while line:
                output.append(line.strip())
                line = f.readline()
                if line.strip():
                    output.append(line.strip())

        if (len(output)>0):
            return True
        else:
            return False

def proc_start(processname):
        logger.info("Going to start process {0}".format(processname))
        thread1 = Thread(target=start_process)
        thread1.start()


def start_process():
        subprocess.call(['./' +proc_name])


def daemonsupervisor(maxattempts,attemptDuration,processname,checkinterval):
        attempts=1
        while True:
            if checkIfProcessRunning(processname):
                logger.info("Yes a {0} process was running".format(processname))
                time.sleep(checkinterval)
            else:
                logger.info("No {0} process was running".format(processname))
                attempts=attempts+1
                time.sleep(attemptDuration)
                if(attempts>maxattempts):
                    logger.info("Tried more than {0} attempts, going to restart the process again".format(maxattempts))
                    proc_start(processname)
                    attempts=0


if __name__ == '__main__':

    proc_name = sys.argv[1]+'.sh'
    attempts = sys.argv[2]
    daemonsupervisor(maxattempts=int(attempts),attemptDuration=1,processname=proc_name,checkinterval=2)
