message=input('How many people are there for dinner?')
message=int(message)  #函数int将字符串转化为数字。
if message>8:
    print('There are no seats left!')
else:
    print("welcome to eat!")