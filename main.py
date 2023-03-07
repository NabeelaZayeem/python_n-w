from threading import *
from multitasking.file1 import Oddnumbers
from multitasking.file2 import Evennumbers
odd_ob=Oddnumbers()
even_obj=Evennumbers()
t1=Thread(target=odd_ob.printodd,args=(25000,))
t2=Thread(target=even_obj.printeven,args=(2500,))
t1.start()
#t1.join()
t2.start()
t2.join()