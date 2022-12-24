import math
list= [1,2,5,4,8,9,7,6,3,10]
print("List : " + str(list))

mean = sum(list) / len(list)
var = sum((l-mean)**2 for l in list) / len(list)
st_dev = math.sqrt(var)

print("Desviación estándar: " + str(st_dev))