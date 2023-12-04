import random

def passwordGenerator(len, complexity):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
    loCaseChar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    upCaseChar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
    
    password = ""    
    if(complexity==1):
        chars = loCaseChar + upCaseChar
        for i in range(len):
            char = random.choice(chars)
            password = password + char
    elif(complexity==2):
        chars = loCaseChar + upCaseChar + digits
        for i in range(len):
            char = random.choice(chars)
            password = password + char
    else:
        chars = loCaseChar + upCaseChar + digits + symbols
        for i in range(len):
            char = random.choice(chars)
            password = password + char

    return password
    
len = int(input("""The satisfactory length of password is 8 characters\nEnter the Length of the password: """))
print("Choose the complexity of the password to generate from the options below:\n1. Simple(lowerCaseCharacters + upperCaseCharacters)\n2. Moderate(lowerCaseCharacters + upperCaseCharacters + digits)\n3. Tough(lowerCaseCharacters + upperCaseCharacters + digits + specialCharacters)")
complexity = int(input("Enter the option number: "))
print(passwordGenerator(len, complexity))