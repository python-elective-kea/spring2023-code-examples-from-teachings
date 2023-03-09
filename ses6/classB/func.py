
def add():
    pass

def add(num):
         return num + num

def add(*args):
        print(args)
        return sum(args)


def add(*args):
        if all(type(element) == type(args[0]) for element in args):
            return sum(args)


# 1. python functions is first class citizens / objects / function

def my_func(x):
    return x



# 2. python has inner functions

def outer():
    def inner():
        return 'This is from inner function'
    
    # print(inner())

    return inner



# 3 . decorators

def my_decorator(func):
    def wrapper(*args):
        x = 'Before \n'
        x += func(*args) + '\n'
        x += 'After'
        return x
    return wrapper

@my_decorator
def greet():
    return 'Hello'

@my_decorator
def msg(name):
    return f'Hello {name}'



# wrapper = my_decorator(greet)
# greet = my_decorator(greet)










































