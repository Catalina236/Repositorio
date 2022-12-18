Número=1
while Número<=1000:
    Contador=1
    x=0
    while Contador<=Número:
        if Número%Contador==0:
            x=x+1
        Contador=Contador +1
    if x==2:
        print(Número)
    Número=Número+1
