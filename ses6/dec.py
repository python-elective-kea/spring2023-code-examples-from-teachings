# 1. function in python is a first class object or a first class functionw

def func(x):
    return x



# 2. In python you can create inner function

def outer():
    def inner():
        print('inner')
    

    # execute the inner function
    inner()

    # or return the inner function
    return inner

# 3. Decorator function

def my_decorator(func):
    def wrapper(*args):
        x = 'do somthing here'
        x += func(*args)
        x += 'do something else'
        return x
    return wrapper

@my_decorator
def message():
    return 'Hello from message function'


@my_decorator
def message2(name):
    return f'Hello from {name}'





# wrapper = my_decorator(message)

# x = my_decorator(message)

# message = my_decorator(message)





















