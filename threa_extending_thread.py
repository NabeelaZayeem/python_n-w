from threading import *
class Myclass(Thread):
    def run(self):
        print("Hello from thread")
obj=Myclass()
obj.start()