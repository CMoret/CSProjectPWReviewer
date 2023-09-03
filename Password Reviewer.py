# PasswordReviewer
# This program allows you to enter a username and password. It prints your username in plain text,
# masks the password with asterisks, displays the password's length, and provides security measures
# if your password is too short.


#Input username and password
username= input('\nPlease enter your username: ' )
password= input('Please enter your password: ')

#Determine password length and converts password into asterisks
pw_length= len(password)
secret_pw= '*'* pw_length


print(f'\n Your username is: {username}\n Your password is: {secret_pw}, and it is {pw_length} characters long')

if pw_length > 10:
   print('\nYou are safe from password attacks')
else:
   print('\nYour password is short. \nPlease use a more complex password to protect your data from attacks!')

print('Goodbye, end of program!')
