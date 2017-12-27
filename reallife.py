import threading
import time
import random

#Three different people who can access one account
#All the accounts will be locked when one user withdraws funds, just so
#people are always withdrawing money which exists in the account and never go to 0

#creating a class which is a subclass of thread
#https://www.youtube.com/watch?v=Bs7vPNbB9JM

threadLock = threading.Lock()
class BankAccount(threading.Thread):   
    acctBalance = 100
    def __init__(self, name, moneyRequest):
        threading.Thread.__init__(self)
        self.name = name
        self.moneyRequest = moneyRequest

    def run(self):
        threadLock.acquire()
        BankAccount.getMoney(self)
        threadLock.release()
        #keep other threads from being able to access our account

    @staticmethod
    def getMoney(customer):
        print("{} tried to withdraw ${} at {}".format(customer.name, customer.moneyRequest, time.strftime("%H:%M:%S", time.gmtime())))

        if BankAccount.acctBalance - customer.moneyRequest > 0:
            BankAccount.acctBalance -=customer.moneyRequest
            print("New account balance: ${}".format(BankAccount.acctBalance))
        else:
            print("Not enough money in account")
            print("current balance : ${}".format(BankAccount.acctBalance))
        time.sleep(3)

        
doug =BankAccount("Doug", 1)
paul = BankAccount("Paul", 100)
sally = BankAccount("Sally",50)

doug.start()
paul.start()
sally.start()

#doug.join()
#paul.join()
#sally.join()
#join() waits for current thread to stop executing before starting a new thread
#sounds like your defeating the point of threads


print("execution ends")
