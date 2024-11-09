# ask a user to enter their first name and store it in a variable
# ask a user to enter their last name and store it in a variable
# print their full name
# Make sure you have a space between first and last name
# Make sure the first letter of first name and last name is uppercase
# Make sure the rest of the name is lowercase
first_name = input('What is your first name?: ')
last_name = input('What is your last name?: ')

print (first_name.capitalize() + ' ' + last_name.capitalize())

# custom string formating or concatenation using output
output = 'Hello, ' + first_name + ' ' + last_name
output1 = 'Hello, {} {}'.format(first_name, last_name)
output2 = 'Hello, {0} {1}'.format(first_name, last_name)
output3 = f'Hello, {first_name} {last_name}'

print (output)
print (output1)
print (output2)
print (output3)