from functools import wraps


def input_validator(in_func):
    @wraps(in_func)
    def wrapper_func(*args, **kwargs):
        if args[0]>=0 and args[1]>0:
            return in_func(*args,**kwargs)
        else:
            raise Exception("Both x and y have to be positive for function {} to work".format(in_func.__name__))
            
    return wrapper_func

def logger(in_func):
    @wraps(in_func)
    def wrapper_func(*args, **kwargs):
        print(in_func.__name__)
        return in_func(*args,**kwargs)
    return wrapper_func

@input_validator
@logger
def devide(firstNum,SecondNum):
    return firstNum/SecondNum

#print(devide(2,0))

