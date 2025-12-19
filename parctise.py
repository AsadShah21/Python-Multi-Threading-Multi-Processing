import time
import multiprocessing

result = []

def square_cube(number):
    for n in number:
        print(f'square is {n*n}')
        print(result.append(n*n*n))
        print('he cube is: ', result)



if __name__=="__main__":

    try:
        t = time.time()
        array = [2,3,4,5]
        m1 = multiprocessing.Process(target=square_cube , args=(array,))

        m1.start()
        m1.join()

        print(result)
        print(f'Time it took to complete the program:  {time.time() - t}')

    except Exception as e:
        print(e)    
