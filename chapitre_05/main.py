from pprint import pprint
from rectangle_singleton import Rectangle as RectangleSingleton
from rectangle import Rectangle

def main():
    a = 2
    print(type(type(a)))
    print(type(type(a)))
    
    r = RectangleSingleton(1,2)    
    r1 = RectangleSingleton(12,28)    
    print(r.surface)
    print(r.surface)
    print(hex(id(r)))
    print(hex(id(r1)))
    r.longueur = 1000
    print(r1)
    r2 = Rectangle(2,3)
    r3 = Rectangle(5,6)
    print(hex(id(r2)))
    print(hex(id(r3)))
    print(r2.surface)
    print(r3.surface)
if __name__=='__main__':
    main()
