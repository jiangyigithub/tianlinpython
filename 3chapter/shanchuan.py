mountain=["tai shan","huang shan","heng shan","song shan","hu qiu"]
print(mountain) #输出原始数据

print("the new one:")
print(sorted(mountain)) #临时排序
print("the old one:") #核实原始数据
print(mountain)

sorted(mountain,reverse=True)#按字母倒序排序
print(f"the third one:\n{mountain}") 


mountain.reverse()#修改排序
print(f"the forth one:\n{mountain}")


mountain.reverse()#再次修改排序
print(f"the fifth one:\n{mountain}")

mountain.sort()#按字母顺序排序
print(f"the sixth one:\n{mountain}")

mountain.sort(reverse=True)#按字母倒序排序
print(f"the seventh one:\n{mountain}")