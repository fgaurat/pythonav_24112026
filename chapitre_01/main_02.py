from pprint import pprint
import copy
def main():
    l = [10,20,30,40,50]
    
    print(l)
    print(len(l))
    print(l[0])
    print(l[-1])
    print(l[1:3]) # [20,30,40[
    print(l[1:4]) # [20,30,40[
    
    print(50*'-')
    
    # l1 = l.copy()
    l1 = l[:]
    l1 = copy.copy(l)
    l[0]=1000
    print(l)
    print(l1)
    print(50*'-')
    
    l = [
        [10,20,30],
        [40,50,60],
        [70,80,90]
    ]
    
    l1 = copy.deepcopy(l)
    l[1][1] = 5000
    print(l)
    print(l1)
    
if __name__=='__main__':
    main()
