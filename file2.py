from threading import *
import time
class Evennumbers:
    def printeven(self,num):
         self.num = num
         for i in range(1, num + 1):
            if (i % 2 == 0):
                    time.sleep(1)
                    print("Even number:",i)