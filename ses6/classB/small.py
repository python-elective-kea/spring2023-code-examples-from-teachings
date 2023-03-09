import time

def log(func):
    def wrapper(*args):
        f = open('log.txt', 'a')
        f.write(f'{time.ctime()}  {args} {func(*args)} \n')
        return func(*args)
        

    return wrapper



@log
def add(*args):
    return sum(args)

@log
def printer(txt):
    return f'Hello {txt}'


# add = log(add)

