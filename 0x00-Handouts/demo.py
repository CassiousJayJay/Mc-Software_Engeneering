def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y 

def devide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Division by zero is not allowed."

def remainder(x, y):
    return x % y
   

print("Select the operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Devide")
print("5. Remainder")

while True:
    choice = input("Enter your choice (1/2/3/4/5)")
    if choice in ("1", "2", "3", "4", "5"):
        try:
            num_1 = int(input("Enter the first number: "))
            num_2 = int(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid input.")
            continue
        if choice == "1":
            print(num_1, "+", num_2, "=", add(num_1, num_2))
        
        elif choice == "2":
            print(num_1, "-", num_2, "=", subtract(num_1, num_2))
            
        elif choice == "3":
            print(num_1, "*", num_2, "=", multiply(num_1, num_2))
            
        elif choice == "4":
            print(num_1, "/", num_2, "=", devide(num_1, num_2))
            
        elif choice == "5":
            print(num_1, "%", num_2, "=", remainder(num_1, num_2))
            
        next_calculation = input("Would you like to do another calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid input")
            