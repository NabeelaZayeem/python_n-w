from threading import *
import  time
class Oddnumbers:
    def printodd(self,num):
        self.num=num
        for i in range(1,num+1):
            if(i%2!=0):
                time.sleep(1)
                print("Odd number",i)



