# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'. The default operation is 'add'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator
#
def calculator (first_number, second_number, operation = 'ADD'):
    if operation == 'ADD':
        return (first_number + second_number)
    elif operation == 'SUBTRACT':
        return (first_number - second_number)
    else:
        if operation == 'DIVIDE':
            return ('Invalid operation please specify ADD or SUBTRACT')
        

# Test your function using named notation passing in only the numbers 6 and 4
# Should return 10
#
print(str(calculator(6,4, 'ADD')))

# Test your function using named notation with the values 6,4, subtract 
# Should return 2
# 
print(str(calculator(6,4, 'SUBTRACT')))

# BONUS: Test your function with the values 6, 4 and divide 
# Have your function return an error message when invalid values are received
print(str(calculator(6,4, 'DIVIDE')))

# Testing default
print(str(calculator(6,4,)))