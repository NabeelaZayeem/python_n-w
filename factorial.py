from threading import *
class Myclass(Thread):
    def fact(self,n):
        self.n=n
        fact=1
        if n>=1:
            for i in range(1,n+1):
                fact=fact*i


            print("Factorial of a number is:", fact)

    def run(self,n):
        print("Hello from thread")
        self.fact(n)

obj=Myclass()
# obj.start(5)
obj.run(5)
# obj.fact(5)