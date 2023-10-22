
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def subtract(x, y):
    return x - y

def devide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    

def remainder(x, y):
    return x % y

print("Select the operation")
print("1. Add")
print("2. Multiply")
print("3. Subtract")
print("4. Devide")
print("5. Remainder")

while True:
    choice = input("Enter your choice(1/2/3/4/5): ")
    if choice in ("1", "2", "3", "4", "5"):
        try:
            first_number = int(input("Enter the first number: "))
            second_number = int(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter the valid input.")
            continue
        
        if choice == "1":
            print(first_number, "+", second_number, "=", add(first_number, second_number))
        
        elif choice == "2":
            print(first_number, "*", second_number, multiply(first_number, second_number))
        
        elif choice == "3":
            print(first_number, "-", second_number, "=", subtract(first_number, second_number))
            
        elif choice == "4":
            print(first_number, "/", second_number, "=", devide(first_number, second_number))
            
        elif choice == "5":
            print(first_number, "%", second_number, "=", remainder(first_number, second_number))
            
        next_calculation = input("Would you like to do another calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid input")