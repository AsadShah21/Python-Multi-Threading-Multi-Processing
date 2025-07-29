import multiprocessing.process
import time
import multiprocessing

def deposit(balance, lock):

    for i in range(100):

        time.sleep(0.1)

        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdraw(balance, lock):
    for i in range(100):

        time.sleep(0.1)

        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

if __name__ == "__main__":

    t = time.time()

    balance = multiprocessing.Value('i' , 200)

    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit , args=(balance,lock) )
    w = multiprocessing.Process(target=withdraw , args=(balance,lock) )


    d.start()
    w.start()

    d.join()
    w.join()

    print('The time taken to complete this program is ' , time.time() - t)

    print(balance.value)