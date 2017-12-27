import threading
import time
import random

def executeThread(i):
    print("Thread {} sleeps at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))
    randSleepTime = random.randint(1, 5)
    time.sleep(randSleepTime)
    print("Thread stops sleeping at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))


    #creating some threads
for i in range(10):
    thread = threading.Thread(target=executeThread, args=(i,))
    #each time it goes through the loop, this threading
    #object is created
    thread.start()
    print("Active threads:", threading.activeCount())
    print("Thread Objects:", threading.enumerate())
        
