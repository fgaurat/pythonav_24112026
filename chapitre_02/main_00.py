
a = 12
def f():
    if False:
        b=1000
    else:
        print(b)
        
    # print(b)


default_value = 12


def f2(a=default_value):
    print(a)

default_value = "Une autre valeur"

def main():
    # print(a)
    # f()
    # print(a)
    f2()

if __name__=='__main__':
    main()
