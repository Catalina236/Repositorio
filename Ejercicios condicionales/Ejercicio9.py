Horas=int(input("Ingrese la hora: "))
Minutos=int(input("Ingrese los minutos: "))
Segundos=int(input("Ingrese los segundos: "))
if Segundos==59:
        Minutos=Segundos+1
        if Minutos==60:
            Horas+=1
            Minutos=Segundos-59
            Segundos-=59
            print("La hora es: ",Horas,":",Minutos,":",Segundos)
elif Minutos<59:
    Minutos+=1
    Segundos+=1
    print("La hora será dentro de un segundo: ",Horas,":",Minutos,":",Segundos)