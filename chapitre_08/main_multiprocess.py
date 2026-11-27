from pprint import pprint
import os
import time
from multiprocessing import Pool

def longwork():
    t = 2
    start = time.time()
    while time.time()-start < t:
        pass
    
def f(x):
    longwork()
    return x*x

    
def main():
    print(os.cpu_count())
    
    with Pool(4) as p:
        print(p.map(f, range(500)))    

if __name__=='__main__':
    main()
