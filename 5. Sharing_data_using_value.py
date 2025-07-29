import time
import multiprocessing


def cal_square(numbers, result):

    for idx, n in enumerate(numbers):
        result[idx] = n*n

def cal_cube(numbers, v):
    v.value = 5.67
    for n in numbers:
        print('Cube is ' , str(n*n*n))

if __name__ =="__main__":
     numbers = [2,5,7,9]

     result = multiprocessing.Array('i',3)   # This is a new memory now known as shared memory,
    #  Now main prcess and child process can access this shared memory

     v = multiprocessing.Value('d', 0.0)

     t = time.time()

    # Giving this shared memory to process 1 
     p1 = multiprocessing.Process(target=cal_square , args=(numbers, result)) 
     p2 = multiprocessing.Process(target=cal_cube , args=(numbers, v))

     p1.start()
     p2.start()

     p1.join()
     p2.join()

     print('The time it took to complete the program is : ', time.time() - t )
     print(result[:]) #   result will not be stored in this globl variable as process 
    #  don't allow it, bcauese process has it's own memory

    # process is child program
    # other is main program ( global variable is in main program)

     print(v.value)