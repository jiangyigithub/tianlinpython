name_list=['jiang kang kuaile','mei yanan','fo guang','opqrst']
print(name_list)

absent=name_list[0]

print(f"{absent.title()} can not to attend the supper meeting.")
name_list.remove('jiang kang kuaile') 
print(f"\n{name_list[-1].title()} ,welcome to attend this supper meeting!")
print(f"\n{name_list[-2].title()} ,welcome to attend this supper meeting!")
print(f"\n{name_list[-3].title()} ,welcome to attend this supper meeting!")
print(f"\nI find a bigger meeting room!")

name_list.insert(0,'jiang wenxin')
print(name_list)
name_list.insert(2,'xiao shunzi')
print(name_list)
name_list.append('xiao huzi')
print(name_list)

print(f"\n{name_list[-1].title()} ,welcome to attend this supper meeting!")
print(f"\n{name_list[-2].title()} ,welcome to attend this supper meeting!")
print(f"\n{name_list[-3].title()} ,welcome to attend this supper meeting!")
print(f"\n{name_list[-4].title()} ,welcome to attend this supper meeting!")
print(f"\n{name_list[-5].title()} ,welcome to attend this supper meeting!")
print(f"\n{name_list[-6].title()} ,welcome to attend this supper meeting!")
print("sorry,I can only welcome two person to attend this meeting!")
popped_name_list=name_list.pop()
print(f"sorry,I can not  welcome {popped_name_list.title()} to attend this meeting!")
popped_name_list=name_list.pop()
print(f"sorry,I can not  welcome {popped_name_list.title()} to attend this meeting!")
popped_name_list=name_list.pop()
print(f"sorry,I can not  welcome {popped_name_list.title()} to attend this meeting!")

del name_list[0]
print(name_list)
del name_list[0]
print(name_list)
del name_list[0]
print(name_list)