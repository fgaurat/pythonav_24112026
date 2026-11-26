import lib
from pprint import pprint
import sys
# from lib import somme
# from lib12 import somme as somme12

# def somme(x,y):
#     return x+y

def main():
    result = lib.somme(2,3)
    print("le resultat",result)
    # somme(2,3)

    a = 2
    b = 2
    
    print(hex(id(a)))
    print(hex(id(b)))
    
    b=12

    
    print(sys.getrefcount(123546354621123546548699))
    c= 123546354621123546548699
    print(sys.getrefcount(123546354621123546548699))
    
    
    s = "toto"
    # s[0]="j"
    
    b = 2
    s = "toto "*b
    print(s)
    
    print("#"*50)
    
    
    print(12)


if __name__=='__main__':
    main()

