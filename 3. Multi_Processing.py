import time
import multiprocessing


square_result =[]

def cal_square(numbers):

    global square_result 
    for n in numbers:
        print('Square is :' , str(n*n))
        print(square_result.append(str(n*n*n)))
        print('within a process result' + str(square_result))

def cal_cube(numbers):
    for n in numbers:
        print('Cube is ' , str(n*n*n))

if __name__ =="__main__":
     array = [2,5,7,9]

     t = time.time()

     p1 = multiprocessing.Process(target=cal_square , args=(array,))
     p2 = multiprocessing.Process(target=cal_cube , args=(array,))

     p1.start()
     p2.start()

     p1.join()
     p2.join()

     print('The time it took to complete the program is : ', time.time() - t )
     print('result' + str(square_result)) #   result will not be stored in this globl variable as process 
    #  don't allow it, bcauese process has it's own memory

    # process is child program
    # other is main program ( global variable is in main program)