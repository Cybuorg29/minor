import threading 
import signal 
from time import sleep 

def exitThread(signum, frame): 
    raise SystemExit 

def worker(): 
    try: 
        signal.signal(signal.SIGALRM, exitThread) 
        signal.alarm(10) 
        while True: 
            print("Thread")  
            sleep(1) 

threads = [] 
for x in range(40): 
    t = threading.Thread(target=worker) 
    threads.append(t) 
    t.start()