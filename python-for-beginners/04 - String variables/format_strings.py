# Ask the user for their first and last name
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

# the capitalize function will return the string with 
# the first letter uppercase and the rest of the word lowercase
print ('Hello ' + first_name.capitalize() + ' ' \
       + last_name.capitalize())
print (first_name.upper())
print (first_name.lower())
print (first_name.capitalize())
print (first_name.count('e'))