#Linux System Health Monitor 
This is a Python-based system health monitoring script I created and deployed on an AWS EC2 instance running Ubuntu. It checks CPU, memory, and disk usage every 5 minutes, logs them to a file, and alerts if any threshold is breached.
I used ‘psutil’ for system metrics, ‘cron’ to automate it every 5 minutes, and wrote everything in Python running inside a virtual environment.

#Features
•	Monitors CPU, Memory, and Disk Usage
•	Logs output to a file with timestamp
•	Sends alerts when usage exceeds threshold
•	Automatically runs every 5 minutes using cron
•	Built and tested inside a live AWS EC2 instance

#File Structure
1.	monitor.py (Main monitoring script)
2.	run-monitor.sh (Shell script for cron to execute)
3.	sample_log.txt (Output log file with system status)
4.	cron_output.log (Captures output/errors from cron runs)
5.	README.md (This file)
   
#Technologies Used
•	Python 3
•	psutil
•	Cron
•	Virtualenv
•	AWS EC2 (Ubuntu)

#How I Set This Up
1. Created an EC2 instance with Ubuntu
2. Installed Python3 and pip
3. Set up a virtual environment and installed ‘psutil’
4. Wrote a Python script to check system health
5. Wrote a shell script to activate the venv and run the monitor
6. Scheduled it with `cron` to run every 5 minutes
   
#How to Run
Bash
source venv/bin/activate
python monitor.py
# To run it automatically:
crontab -e
# Add this line:
*/5 * * * * /home/ubuntu/linux-health-monitor/run-monitor.sh >> /home/ubuntu/linux-health-monitor/cron_output.log 2>&1

