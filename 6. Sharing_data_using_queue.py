import time
import multiprocessing


def cal_square(numbers, q):
    for n in numbers:
        q.put(n*n)


if __name__ =="__main__":
     numbers = [2,5,7,9]

     q = multiprocessing.Queue()   # This is a new memory now known as shared memory,
    #  Now main prcess and child process can access this shared memory

     t = time.time()

    # Giving this shared memory to process 1 
     p1 = multiprocessing.Process(target=cal_square , args=(numbers, q)) 


     p1.start()
  

     p1.join()

     print('The time it took to complete the program is : ', time.time() - t )

    # process is child program
    # other is main program ( global variable is in main program)
     while q.empty is False:
         print(q.get())
