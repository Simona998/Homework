def add(x, y):      # This function adds two numbers
    return x + y

def subtract(x, y):     # This function subtracts two numbers
    return x - y

def multiply(x, y):     # This function multiplies two numbers
    return x * y

def divide(x, y):       # This function divides two numbers
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choiceOp = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choiceOp in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:      
            print("Invalid input. Please enter a number.")  # when inappropriate value is received
            continue

        if choiceOp == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choiceOp == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choiceOp == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choiceOp == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation 
        new_calculation = input("Would you like to do a new calculation? (yes/no): ")
        if new_calculation == "no":            # if answer is no break the while loop
          break
    else:
        print("Invalid Input")