import time
from multiprocessing import Process, Lock

def f(i, l):
    l.acquire()
    try:
        print("Hello from ",i)
        time.sleep(1)
    finally:
        l.release()

if __name__=='__main__':
    lock = Lock()
    for num in range(10):
        Process(target=f, args=(num,lock)).start()
