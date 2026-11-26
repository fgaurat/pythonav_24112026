from pprint import pprint

from rectangle import Rectangle
from data_rectangle import DataRectangle

def main():
    # region start
    r = Rectangle(10,12)
    r1 = Rectangle(10,12)
    
    
    print(r1.longueur) # 2
    r1.longueur = 12
    print(r1.longueur) # 12
    print(r1.longueur) # 12

    print(r1.surface)
    
    
    s = str(r)
    print(s)
    r2 = Rectangle(2,3)
    r3 = Rectangle(2,3)    
    
    # if r2.__eq__(r3):
    if r2 == r3:
        print("ok")
    else:
        print("ko")
    
    # print("Rectangle._cpt",Rectangle._cpt)
    print("Rectangle.get_cpt()",Rectangle.get_cpt())
    r4 = Rectangle.build_from_str("2;3")    
    print(r4)
    # endregion

    d = DataRectangle(2,3)
    print(d)
    print(d.surface)
if __name__=='__main__':
    main()
