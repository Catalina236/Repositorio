Lista=[1,2,5,4,8,9,7,6,3,10]
Lista.sort()
Total=len(Lista)
if Total%2!=0:
    mediana=Lista(Total//2)
else:
    a=Lista[Total//2]
    b=Lista[Total//2-1]
    mediana=a+b/2
print("La mediana es ", mediana)
