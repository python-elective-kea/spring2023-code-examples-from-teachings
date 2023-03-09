import time


def log_decorator(func):
    def wrapper(*args):
        # write the timestamp to a log file
        f = open('log.txt', 'a')
        f.write(f'{time.ctime()} {list(args)} {func(*args)}\n')
        return func(*args)

    return wrapper


@log_decorator
def add(*args):
    return sum(args)

@log_decorator
def printer(x):
    return f'This is printet {x}'



# add = log_decorator(add)
