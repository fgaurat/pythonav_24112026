import time
import threading
import multiprocessing

def count():
    x = 0
    for _ in range(20_000_000):
        x+=1

def run_seq():
    start = time.perf_counter()
    count()
    count()
    end = time.perf_counter()    
    print(f"run_seq {end-start:0.3f}s")

def run_thread():
    start = time.perf_counter()
    th1 = threading.Thread(target=count)
    th2 = threading.Thread(target=count)
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    end = time.perf_counter()    
    print(f"run_thread {end-start:0.3f}s")

def run_process():
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=count)
    p2 = multiprocessing.Process(target=count)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.perf_counter()    
    print(f"run_process {end-start:0.3f}s")
            

def run_process2():
    s = time.perf_counter()
    p1 = multiprocessing.Process(target=count)
    p2 = multiprocessing.Process(target=count)
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    e = time.perf_counter()
    print(f"Function  executed in {(e - s):.4f}s")        

def main():
    run_seq()
    run_thread()
    run_process()
    run_process2()

if __name__=='__main__':
    main()
