def divisores(num):
    for divisor in range(1,num+1):
        if num%divisor==0:
            print(divisor)
num=int(input("Ingrese un número: "))
print(divisores(num))

