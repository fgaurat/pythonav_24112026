from pprint import pprint
from functools import wraps
import inspect
# region deco1
# def do_log(func):
    
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         print("LOG",*args,**kwargs)
#         result = func(*args,**kwargs)
#         print("LOG",result)
#         return result
    
#     return wrapper
# endregion


def do_log(log_file):
    def decorator(func):
        
        @wraps(func)
        def wrapper(*args,**kwargs):

            print(f"LOG to {log_file}",*args,**kwargs)
            result = func(*args,**kwargs)
            print(f"LOG to {log_file}",result)
            return result
        
        return wrapper
    return decorator

@do_log("lefichier.log")
def say_hello(name):
    """
    Dire bonjour
    """

    return f"Bonjour {name}"



def main():
    r = say_hello('Fred')
    
    print(r)
    
    print(say_hello.__name__)
    print(say_hello.__doc__)
    
    # print(say_hello.__wrapped__)
    print(hasattr(say_hello,"__wrapped__"))
    
    o = inspect.unwrap(say_hello)    
    print(o.__name__)
    print(o.__qualname__)
    
if __name__=='__main__':
    main()
