import time

def timer_wrapper(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_num_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

@timer_wrapper
def prime_num_getter(n):
    generator = prime_num_generator()
    primes = [next(generator) for _ in range(n)]
    return primes

n = 30
prime_numbers = prime_num_getter(n)
print(f"Перші {n} простих чисел:", prime_numbers)
