from pprint import pprint

# def hello(name,firstname):
def hello(**kwargs):
    print(kwargs)
    print('Hello',kwargs.values())
    # print('Hello',*kwargs.items())

def add(*l):
    print(l)
    return sum(l)

def main():
    # region partie 01
    l = [10,20,30,40,50]
    
    # r = add(l) 
    # assert r == 150
    r = add(10,20,30,40,50) 
    r = add(*l) # add(10,20,30,40,50) 
    # r = add(10,20,30) 
    print(r) #150


    # a,b,*c = 0,1,2,3,4,5
    a,*b,c = 0,1,2,3,4,5
    # print(a,b,c)
    # a,b,c,d,e = [*l]
    # endregion

# hello("GAURAT","Fred")
hello(name = "GAURAT",firstname= "Fred")
hello(firstname= "Fred",name = "GAURAT")
hello(firstname= "Fred",name = "GAURAT",job="dev",age=50)

if __name__=='__main__':
    main()
