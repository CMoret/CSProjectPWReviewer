#PasswordReviewer
#This program allows you to enter a username and password, prints your username is clear/plain text, prints password out in astersik, gives you the length of your password and more security measures if your password is too short

#Enter username and password
username= input('\nPlease enter your username: ' )
password= input('Please enter your password: ')

#determins password length and converts password into asterisk
pw_length= len(password)
secret_pw= '*'* pw_length


print(f'\n Your username is: {username}\n Your password is: {secret_pw}, and it is {pw_length} characters long')

if pw_length > 10:
   print('\nYou are safe from password attacks')
else:
   print('\nYour password is short. \nPlease use a more complex password to protect your data from attacks!')

print('Goodbye, end of program!')