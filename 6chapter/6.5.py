river_0={'nile':'EGYPT',
 'HUANG HE':'China',
 'Chang Jiang':'China',
 'Ganga':'India',
 'Mississippi':'America',
 'Volga':'Russia',
 }
for river,country in river_0.items():
    print(f'The {river} run through {country}.\n')  #函数f ,里面的内容用引号，字典用大括号
for  river in river_0.keys():
    print(f'{river}\n')
for country in set(river_0.values()):   #set 集合set中的每个元素独一无二
    print(country)
