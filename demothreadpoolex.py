import threading
from concurrent.futures import ThreadPoolExecutor
def task():
    print("Executing task")
    res=0

    i=0
    for i in range(20):
        res+=i
        print("{}" .format(res))
        print("Task Executed {}".format(threading.current_thread()))
def main():
    executor=ThreadPoolExecutor(max_workers=3)
    task1=executor.submit(task)
    task2=executor.submit(task)
if __name__=='__main__':
    main()