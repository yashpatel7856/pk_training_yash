import time

def timer(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        print(f"{func.__name__} function executed in {end-start} seconds")
        return result
    return wrapper

@timer
def exampleFunc(n):
    time.sleep(n)

exampleFunc(2)