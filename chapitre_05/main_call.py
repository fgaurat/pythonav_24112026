class Test:
    
    def __init__(self,name):
        self.name = name
    
    def __call__(self):
        print("__call__",self.name)

def main():
    t = Test("fred")
    
    t()

if __name__=='__main__':
    main()
