import threading
from pprint import pprint

lock = threading.Lock()
semaphore = threading.Semaphore(5)

def thread1():
    r = []
    for i in range(200):
        r.append(i)
    with lock:    
        print("thread1",r)

def thread2():
    with lock:        
        for i in range(200):
            print("thread2",i)

def main():
    th1 = threading.Thread(target=thread1)
    th2 = threading.Thread(target=thread2)
    
    th1.start()
    th2.start()
    
    th1.join()
    th2.join()
    print("la fin du code")

if __name__=='__main__':
    main()
