# https://www.youtube.com/watch?v=POL7n754JTc
# in summary, when using a shared variable, use the shared variable object
# balance = multiprocessing.Value('type', value)
# to get is value at any given point use .value. balance.value
# to operate on the shared variable, lock it, operate on it, then unlock it
# lock.acquire()
# balance.value = balance.value + 1
# lock.release()

import time
import multiprocessing

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        #without this line, balance.value will be different every time it is run
        balance.value = balance.value - 1
        lock.release()

if __name__ == '__main__':
    balance = multiprocessing.Value('i', 200)
    # a value object is created, where a shared value can be kept. methods include .value, to obtain the final value,
    # Value(a,b) a is the type of data, here it is interger, d is a double precision float i.e. 3141592" 
    lock = multiprocessing.Lock()
    # without the lock, balance.value will come out to be different values everytime is is run. 
    thread1 = multiprocessing.Process(target=deposit, args=(balance,lock))
    # In multiprocessing, processes are spawned by creating a Process object and then calling its start() method.
    # Process follows the API of threading.Thread. So this line is basically starting a thread.
    thread2 = multiprocessing.Process(target=withdraw, args=(balance,lock))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    # when thread1 and thread2 have completed, print balance.value. If the joins were not in here, it will print balance.value
    # once when and the value will be that value at the time of execution of the print statement. Rather than the final
    # value when the threads have ended
    print(balance.value)
