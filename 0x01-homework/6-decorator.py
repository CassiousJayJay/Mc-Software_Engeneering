import time

def measure_excution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        excution_time = end_time - start_time
        print(f"Function {func.__name__} took {excution_time:.4f} seconds to excute")
        return result
    return wrapper
@measure_excution_time
def calculate_multiply(numbers):
    tot = 1
    for x in numbers:
        tot *= x
result = calculate_multiply([1, 2, 3, 4, 5])
print("Result:", result)