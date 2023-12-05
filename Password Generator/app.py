import random

def passwordGenerator(len, complexity):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
    loCaseChar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    upCaseChar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
    
    password = ""
    # password of the specified complexity:
    # if the password to be generated is SIMPLE:
    if(complexity==1):
        chars = loCaseChar + upCaseChar
        for i in range(len):
            char = random.choice(chars)
            password = password + char
    # if the password to be generated is MODERATE:
    elif(complexity==2):
        chars = loCaseChar + upCaseChar + digits
        for i in range(len):
            char = random.choice(chars)
            password = password + char
    # if the password to be generated is TOUGH:
    else:
        chars = loCaseChar + upCaseChar + digits + symbols
        for i in range(len):
            char = random.choice(chars)
            password = password + char

    # printing the generated password:
    print("\nGenerated Password is: " + str(password))

# getting the length of the password from the user:
len = int(input("""The satisfactory length of password is 8 characters\nEnter the Length of the password: """))
print("Choose the complexity of the password to generate from the options below:\n1. Simple(lowerCaseCharacters + upperCaseCharacters)\n2. Moderate(lowerCaseCharacters + upperCaseCharacters + digits)\n3. Tough(lowerCaseCharacters + upperCaseCharacters + digits + specialCharacters)")

# getting the complexity from the user:
complexity = int(input("Enter the option number: "))
passwordGenerator(len, complexity)