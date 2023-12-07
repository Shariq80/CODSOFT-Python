print("Simple Calculator")

# function to get the input of two numbers from the user:
def getNums():
    num1 = float(input("\nEnter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2

# function to get the operation to be done on the given numbers:
def getOperator():
    print("\nChoose the operation to perform on the two numbers:\n1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (*)\n4. Division (/)\n5. Modulo (%)")
    operator = int(input("Enter the option number: "))
    return operator

# function to get the result after performing the specified operation on the given numbers:
def getResult(num1, num2, operator):
    # if operation == addition:
    if(operator==1):
        printResult(num1 + num2)
    # if operation == subtraction:
    elif(operator==2):
        printResult(num1 - num2)
    # if operation == multiplication:
    elif(operator==3):
        printResult(num1 * num2)
    # if operation == division:
    elif(operator==4):
        # checks to not get "Division by Zero" error:
        if(num2==0):
            print("Division by zero is invalid")
            restart()
        printResult(num1 / num2)
    # if operation == modulo division:
    elif(operator==5):
        printResult(num1 % num2)
    # if the user enters invalid input:
    else:
        print("Enter a number from the given options (1 to 5)")
        restart()

# function to print the result:
def printResult(result):
    print("Result is: " + str(result))
    restart()

# function to start the program:
def start():       
    num1, num2 = getNums()
    operator = getOperator()
    getResult(num1, num2, operator)

# function to restart the program:
def restart():
    print("\n\nDo you want to do another caculation?\nEnter 1 if YES\nEnter any other number if NO")
    restart = int(input("Enter your choice: "))
    if(restart==1):
        start()
    else:
        print("\nThank You")
        exit()    

# initial start of the program:
start()
restart()
