from threading import time
import threading
import os

def startprgm(i):
    print ("Running thread %d" % i)
    if (i == 0):
        time.sleep(1)
        print('Running: shutdown.py')
        os.system("sudo python /home/pi/ZBA_Timelapse/shutdown.py")
    elif (i == 1):
        print('Running: ZBA_Timelapse.py')
        time.sleep(1)
        os.system("sudo python /home/pi/ZBA_Timelapse/ZBA_Timelapse.py")
    else:
        pass

for i in range(2):
    t = threading.Thread(target=startprgm, args=(i,))
    t.start()