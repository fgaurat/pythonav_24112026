from pprint import pprint
import timeit
from perf import bench,chrono

@bench(number=1_000_000)
def init_loop():
    r = []
    for i in range(100):
        r.append(i)

@bench(number=1_000_000)
def init_map():
    r = list(map(lambda i:i,range(100)))

@bench(number=1_000_000)
def init_comp():
    r = [i for i in range(100)]
    
    
def main():
    # t1 = timeit.timeit(init_loop)
    # print(t1,"s")
    # t2 = timeit.timeit(init_map)
    # print(t2,"s")
    # t3 = timeit.timeit(init_comp)
    # print(t3,"s")
    init_loop()
    init_map()
    init_comp()

if __name__=='__main__':
    main()
