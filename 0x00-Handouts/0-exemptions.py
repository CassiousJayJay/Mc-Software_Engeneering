
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by by zero is not allowed.")
finally:
    print("Excution completed.")