# Keith Rochfort KR22090004774
# DS T24 Compulsory Task 1

# Operations file to create functions and import into calculator.py

# addition
def add(num1, num2):
    result = num1 + num2
    output = f'{num1} + {num2} = {result}'
    return output


# subtraction
def subtract(num1, num2):
    result = num1 - num2
    output = f'{num1} - {num2} = {result}'
    return output


# multiplication, rounded to 2 dp
def multiply(num1, num2):
    result = round((num1 * num2), 2)
    output = f'{num1} x {num2} = {result}'
    return output


# division, rounded to 2 dp
def divide(num1, num2):
    try:
        result = round((num1 / num2), 2)
        output = f'{num1} / {num2} = {result}'
        return output
    except ZeroDivisionError:
        message = "You can't divide by zero!"
        output = f'{num1} / {num2} = {message}'
        return output


# quotient (division floor)
def quot(num1, num2):
    try:
        result = num1 // num2
        output = f'{num1} // {num2} = {result}'
        return output
    except ZeroDivisionError:
        message = "You can't divide by zero!"
        output = f'{num1} // {num2} = {message}'
    return output


# power  or exponent, rounded to 2 dp
def pow(num1, num2):
    result = round((num1 ** num2), 2)
    output = f'{num1} ^{num2} = {result}'
    return output


# remainder (modulus), rounded to 2 dp
def rem(num1, num2):
    result = round((num1 % num2), 2)
    output = f'remainder of {num1} / {num2} = {result}'
    return output
