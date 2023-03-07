from threading import *
import time
def cube(num):
    for i in num:
        time.sleep(2)
        print(i**3)
numbers=[i for i in range(15)]
t1=Thread(target=cube,args=(numbers,))
t1.start()
t1.join()
print("Hello from main thread")