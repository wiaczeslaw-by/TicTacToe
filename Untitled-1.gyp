n = -4
array = []
last_number = 0
last_number = 0
for i in range(0,n,-1):
    array.append(last_number + i)
    last_number = array[i*-1]
print(array)