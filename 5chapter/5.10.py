current_users=['Jiang yi','Tian lin','Xiao shunzi','SHI MEI','CONG BING']
new_users=['jiang yi','tian lin','bai yun','hui shui','qing cao']
for new_user in new_users:
    for current_user in current_users: 
       if new_user.lower() in  current_user.lower():
        print('please enter the other name!')
    else :
        print('This name has not been used!')