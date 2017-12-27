import threading
import time
import random

class CustThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        #in threading, when the start() method is called, this method run is also called
        #according to python online manual, run() here is overwritten, and only __init__ and the run() method should be overwritten in threading.
        
        getTime(self.name)
        print("Thread", self.name, "execution ends")


def getTime(name):
    print("Thread {} sleeps at {}".format(name, time.strftime("%H:%M:%S", time.gmtime())))
    randSleepTime = random.randint(1, 5)
    if name == "1":
        time.sleep(1)

    else:
        time.sleep(2)
        
thread1 = CustThread("1")
thread2 = CustThread("2")

thread1.start()
thread2.start()

print("Thread 1 Alive", thread1.is_alive())
print("Thread 2 Alive", thread2.is_alive())

print("Thread 1 Name", thread1.getName())
print("Thread 2 Name", thread2.getName())

thread1.join()
#The code under here will only be executed after thread1 has ended.
#can put in a time at which the code underneath will run but putting (timeout=2) etc

print("Thread 1 Alive", thread1.is_alive())                                         
print("Thread 2 Alive", thread2.is_alive())                                         
thread2.join()
print("Thread 1 Alive", thread1.is_alive())                                         
print("Thread 2 Alive", thread2.is_alive())    
print("Execution ends")

