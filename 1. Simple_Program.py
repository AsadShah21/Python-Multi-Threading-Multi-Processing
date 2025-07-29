# simple program without multi threading

import time

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

cal_square(array)
cal_cube(array)

print('Done in :' , time.time()-t)
