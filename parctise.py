import time
import multiprocessing

try:
    def square(numbers):
        for n in numbers:
            print('square:' , str(n*n))

except Exception as e:
    print(e)

if __name__ == '__main__':
    try:
        t1 = time.time()
        array = [6,7,3,2]
        t = multiprocessing.Process(target=square , args=(array,))

        t.start()
        t.join()
        print('Time in took to complete the program' , time.time()-t1)
        
    except Exception as e:
        print('Error :', e)                