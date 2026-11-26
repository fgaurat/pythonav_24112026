from pprint import pprint


def make_incrementor(initial_value):
    
    def inc(increment_value):
        return initial_value+increment_value
    
    return inc

def main():
    do_inc = make_incrementor(12)
    
    r = do_inc(1)
    print(r) # 13

if __name__=='__main__':
    main()
