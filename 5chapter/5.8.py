users_names=['Jiang yi','Tian lin','Xiao shunzi','xiao laohu','pretty baby','admin']
for users_name in users_names:
    if users_name=='admin':
        print(f'Hello {users_name.title()} ,would you like to see a status report?')
    else:
        print(f'Hello {users_name.title()},thank you for logging in again.')