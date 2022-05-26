cubes=[]
for value in range(1,10):
    cube=value**3
    cubes.append(cube)
print(cubes)


cubes=[value**3 for value in range(1,10)]
print(cubes)