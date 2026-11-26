from pprint import pprint

# def mult2(l):
#     r = []
#     for i in l:
#         r.append(i*2)
    
#     return r


def mult2(i):
    return i*2

def main():
    l = [10,20,30,40,50]
    
    # l2 = mult2(l)
    
    # l2 = map(mult2,l)
    # print(*l2)   # [20,40,60,80,100]
    
    
    # l2 = list(map(mult2,l))
    # mult2 = lambda i:i*2
    
    mult2(1)
    
    
    l2 = list(map(lambda i:i*2,l))
    print(l2)
    
    l = [10,20,30,40,50]
    r = []
    for i in l:
        r.append(i*2)
    r = list(map(lambda i:i*2,l))

    r = [i*2 for i in l if i<30]

if __name__=='__main__':
    main()
