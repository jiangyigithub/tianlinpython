users_names=[]
if users_names:
   for users_name in users_names:          
    if users_names=='admin':
        print(f'Hello {users_name.title()} ,would you like to see a status report?')
    else :
        print(f'Hello {users_name.title()},thank you for logging in again.')
else:
        print('We need to find some users!')