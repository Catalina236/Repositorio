n=1
def primos(n):
    while n<=1000:
        contador=1
        x=0
        while contador<=n:
            if n%contador==0:
                x=x+1
            contador=contador+1
        if x==2:
            print(n)
        n=n+1
(primos(n))