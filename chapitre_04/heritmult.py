from pprint import pprint

class A:
    
    def show(self):
        print('A')

class B2(A):
    
    def show(self):
        print('B2')

class B(B2):
    
    def show(self):
        print('B')

class C(A):
    
    def show(self):
        print('C')

class D(B,C):
    
    def show(self):
        print('D')
        super().show()
        super(B,self).show() # appel de B2.show()
        super(B2,self).show() # appel de C.show()
        super(C,self).show() # appel de A.show()

def main():
    print(D.mro())
    d = D()
    d.show()

if __name__=='__main__':
    main()
