#encoding:utf-8
import subprocess
from subprocess import Popen
import time
import logging
import os

#配置项
TIMEOUT   = 10
INTERVAL  = 60
LOGFILE   = r'pmonitor.log'
ETHNAME   = r'eth0'
FILTEREXP = r'host 192.168.1.110 and udp port 123'   #tcpdump -i enp2s0f1 -c 1 "host 192.168.1.110 and udp port 123"
CMD_RESTART = r'./stop.sh; ./start.sh'

def PopenWithTimeout(cmd,timeout=3600):
    proc = Popen(cmd, shell=False)
    #print(proc.pid)  #shell=True 的话，则proc.pid的pid为shell的pid
    
    bFlag = True
    while timeout>0:
        if proc.poll()!=None:
            bFlag = False
            break
        time.sleep(1)
        timeout = timeout-1
        
    if bFlag:
        proc.kill()

def main_loop():
    global TIMEOUT, INTERVAL, LOGFILE
    
    print('packet_monitor start')
    logging.basicConfig(level=logging.ERROR,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=LOGFILE,
                            filemode='w')
                            
    while 1:
        try:
            t0 = time.time()
            PopenWithTimeout(['tcpdump', '-i', ETHNAME, '-c', '1', FILTEREXP],timeout=TIMEOUT)
            t1 = time.time()
            dt = t1-t0
            if(dt>=TIMEOUT):
                os.system(CMD_RESTART)
                msg = 'restart: %s'%CMD_RESTART
                print(msg)
                logging.error(msg)
                
            time.sleep(INTERVAL-dt if INTERVAL-dt>0 else 0)
        except Exception as e:
            msg = 'error: %s'%e
            print(msg)
            logging.error(msg)
            time.sleep(INTERVAL)
        
def main():
    main_loop()
    
if '__main__'==__name__:
    main()
    