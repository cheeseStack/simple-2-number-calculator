# Keith Rochfort KR22090004774
# DS T24 Compulsory Task 1

# Simple calculator that asks for 2 numbers and an operation, then outputs the equations to a teext file.
# Use error handling (such as Division by Zero error)
# Extend the program to allow the user to read all the equations from a new text file they choose the name of.
# Use error exceptions to prevent crashes if file does not exist

# Pseudocode:
# Part 1
# Specify a list of operators and output as a list for user to choose. Use while loop to loop round if user enters an invalid operation.
# Inputs: specify integers or floats. Use ValueError exception to protect from use of characters etc. 
# create an empty list variable, or a dictionary, to store each equation and answer for writing later
# while loop of if statements for each operation type, considering errors for each, such as division by zero. 
# user to enter 'quit' or 'q' or similar to quit the program.
# quitting the program triggers the write function, with exception for file not found. use "with open(file, 'w')" to write if file not found


# Start of code
# import the operation functions for the calculation function
from operations import add, subtract, multiply, divide, quot, rem, pow

# list of calcs to write to txt file
calcs = []

# define the main calculation part of the program
def calculation():

        # specify user input, explain program
    print("\nChoose 2 numbers and a mathematical operation to perform the operation and see the result.")
    
    # Take input of numbers, with try-except block to check for valid entries:
    print('\nChoose 2 numbers: ')
    while True:
        try:
            num1 = float(input('\t1st number: '))
            break
        except ValueError:
            print('Enter a valid number.')
            continue
            
            
    while True:
        try:
            num2 = float(input('\t2nd number: '))
            break
        except ValueError:
            print('Enter a valid number.')
            continue
        
    print('''\nHere are the operation choices:
        'a' : addition
        's' : subtraction
        'm' : multiplication
        'd' : division (first number divided by second number)
        'q' : quotient (division of first number by second number, without any remainder)
        'r' : remainder (of first number divided by second number)
        'p' : power (first number to the power of the second)
        ''')
    
    # while loop for the options
    # After each turn the calculation printed to the Terminal, written to the calculations.txt file, showing calculations of all sessions, and added to the calcs list so they can be written and read (option 'b' in the main menu)
    while True:
        try: # covers invalid input of values with ValueError
            option = input(f"Enter your operation choice for {num1} and {num2}: ")

            # options for the calculation, where 'r' is the result shorthand
            if option == 'a':
                r = add(num1,num2)
                print(r)
                calcs.append(r)
                append_to_calcs_file(r)
                break
            
            elif option == 's':
                r = subtract(num1,num2)
                print(r)
                calcs.append(r)
                append_to_calcs_file(r)
                break
            
            elif option == 'm':
                r = multiply(num1,num2)
                print(r)
                calcs.append(r)
                append_to_calcs_file(r)
                break
            
            elif option == 'd':
                r = divide(num1,num2)
                print(r)
                calcs.append(r)
                append_to_calcs_file(r)
                break
            
            elif option == 'q':
                r = quot(num1,num2)
                print(r)
                calcs.append(r)
                append_to_calcs_file(r)
                break
            
            elif option == 'r':
                r = rem(num1,num2)
                print(r)
                calcs.append(r)
                append_to_calcs_file(r)
                break
            
            elif option == 'p':
                r = pow(num1,num2)
                print(r)
                calcs.append(r)
                append_to_calcs_file(r)
                break
            
            # else statement to catch incorrent entries
            else:
                print("Selection not valid.\nEnter either 'a', 's', 'm', 'd', 'q', 'r', or 'p'") 
                continue   
            
        except ValueError: # eg if numbers inputted
            print('Enter a valid selection')
            continue  
    return calcs # for use writing txt file 


# Main Calculator function that takes in the above functions
def calculator():
    # Ask for user to either enter 2 numbers or print out the calculations
    while True:
        choice = input('''\nChoose an option:
        a - Perform a calculation
        b - Write the calculations to a txt file and print them to the Terminal
        c - Read calculations from an existing txt file
        x - exit the program
Enter a, b, c (or x for exit): ''')
        if choice == 'a':
            calculation()
        elif choice == 'b':
            # ask user for new file name and output results
            while True:
                file_input = input('Type your chosen file name (no spaces or fullstops): ')
                if '.' in file_input or ' ' in file_input:
                    print('Not a valid filename')
                    continue
                else:
                    filename = file_input + '.txt'
                    break
            # write the file       
            with open(filename, 'w+') as f:
                for calc in calcs:
                    f.write(calc + '\n')
            # print file contents to the terminal  
            print('Here are the calculations:\n')      
            with open(filename, 'r') as f_read:
                lines = f_read.read().splitlines()
                for line in lines:
                    print(line) 
        # read an existing (new?) file the user selects                          
        elif choice == 'c':
            read_new_file()    
                
        elif choice == 'x': # exit the program
            exit()
            
        else: 
            print('Invalid option.')
            continue
    
    
# Define the append function to add the calculations to the txt file as they are entered
# take the calc(ulation) as the argument and append to the txt file
def append_to_calcs_file(calc):
    filename = 'calculations.txt'
    with open(filename, 'a') as f:
        f.write('\n' + calc)


# Add extension part function: add an option to read all the equations, add to a new txt file, and print the results
# This option is to read an existing but NEW file (second part of task), creating an error message if it does not exist            
def read_new_file():
    file_name = ''
    while file_name != 'q':
        file_name = input("\nEnter the file name you want to open (eg. 'calculations.txt', or 'q' to quit): ")
        if file_name == 'q':
            break
        try:
            with open (file_name, 'r') as f_read:
                lines = f_read.read().splitlines()
                print(f'\nHere are the calculation in file {file_name}: \n')
                for line in lines:
                    print(line) 
        # file not found error to prevent crashing
        except FileNotFoundError:
            print("\nSorry, the file {file_name} does not exist. Make sure you include the .txt at the end.")  
            continue   
    
            
# call the calculator function to run the program
calculator()


# End of code       