# Ask a user their name
first_name = input ('What is your  first name?: ')
last_name = input ('What is your last name?: ')

# If their first name starts with A or B 
# tell them they go to room AB

if first_name[0].upper() in ['A','B']:
    print('Please go to room AB')

# IF their first name starts with C
# tell them to go to room CD

elif first_name[0].upper() in ['C','D']:
    print('Please go to room CD')

# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z

else:
    if last_name[0].upper() == 'Z':
        print('Please go to room Z')
# if their last name starts with any other letter, tell them to go to room OTHER
    else:
        print('Please go to room OTHER')
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z
