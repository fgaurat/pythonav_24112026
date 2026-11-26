

def div(a,b):
    return a/b


def call_div(a,b):
    try:
        print("OPEN LOG FILE")
        r = div(a,b)
    # except Exception as e:
    #     raise NotImplementedError() from e 
    finally:
        print("CLOSE LOG FILE")
    
    return r




def main():
    try:
        a = 2
        b = 0
        c = call_div(a,b)
        print(c)
    except (ZeroDivisionError,TypeError) as e:
        print(e)
    # except TypeError as e:
    #     print(e)
    except Exception as e:
        print(e)
    else:
        print("pas d'erreur")


    print("la suite du code...")

if __name__=='__main__':
    main()
