# process-management

Create a “daemon supervisor”. It should check that the process is running all the times and starts it if in case it is down.  

It should take as parameters:

• Seconds to wait between attempts to restart service 
• Number of attempts before giving up 
• Name of the process to supervise 
• Check interval in seconds 
• Generate logs in case of events.

Create threads for "daemon supervisor" using below six shell files and pass one file at a time as a input process:

• bash -c "sleep 1 && exit 0" 
• bash -c "sleep 5 && exit 0" 
• bash -c "sleep 1 && exit 1" 
• sh -c "sleep 10 && exit 1" 
• bash -c "if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1" 
• bash -c "if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1" (with 1 attempt only) 

Solution:

To Run DaemonSupervisor Code

run the code with below command

assign executable permission to shell script using below command 

chmod +x one_attaempt.sh
chmod +x  sleepfive_exitone.sh
chmod +x  sleepone_exitone.sh
chmod +x  sleepone_exitzero.sh
chmod +x  sleepten_exitone.sh
chmod +x  subproc.sh

python DaemonSupervisor.py (shell script program as argument 1) (attempts as argument 2)
eg. python DaemonSupervisor.py subproc 2

Please do not provide extension as .sh to shell script program as I have passed this extention in the code.

Pass shell script and attempts with DaemonSupervisor code as mentioned in above example. 
