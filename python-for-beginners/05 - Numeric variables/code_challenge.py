# Ask a user to enter a number
# Ask a user to enter a second number
# Calculate the total of the two numbers added together
# Print 'first number + second number = answer' 
# For example if someone enters 4 and 6 the output should read
# 4 + 6 = 10
first_num = input('Enter first number: ')
second_num = input('Enter second number: ')

output = int(first_num) + int(second_num)
print (str(first_num) + ' + ' + str(second_num) + ' = ' + str(output))
# this is correct, but both print the same result
print (first_num + ' + ' + second_num + ' = ' + str(output))