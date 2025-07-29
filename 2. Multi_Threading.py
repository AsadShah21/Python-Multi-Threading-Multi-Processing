import time
import threading

def cal_square(numbers):
    for n in numbers:
        time.sleep(0.2)  # at this time CPU does not do anything for 0.2 seconds it just holds
        print('square : ' , n*n)

def cal_cube(numbers):
    for n in numbers: 
        time.sleep(0.2)   # at this time CPU does not do anything for 0.2 seconds it just holds
        print('cube : ' , n*n*n)


array = [2,4,5,7]

t = time.time()

t1 = threading.Thread(target=cal_square , args=(array,))
t2 = threading.Thread(target=cal_cube , args=(array,))

t1.start()
t2.start()

# means join back to the thread ( main program after both multi tasks end )
t1.join()  
t2.join()

print('Program completed in :' , time.time()-t)