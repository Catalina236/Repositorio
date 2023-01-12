hora=int(input("Ingrese hora: "))
minuto=int(input("Ingrese minutos: "))
segundos=int(input("Ingrese segundos: "))
Hora=24
Minuto=59
Segundo=59
if segundos<=Segundo:
    Seg=segundos+1
if minuto<=Minuto:
    Min=minuto+1
if hora<=Hora:
    Hor=hora+1
if hora>Hora or minuto>Minuto or segundos>Segundo:
    print("Hora inválida")
elif Hor>Hora and Min>Minuto and Seg>Segundo:
    print("La hora dentro de un segundo será: 01:","00:","00")
elif Min>Minuto and Seg>Segundo:
    print("La hora dentro de un segundo será ",Hor,"00","00")
elif Seg>Segundo:
    print("La hora dentro de un segundo será",Hor,Min,"00")
elif Min>Minuto and Seg<Segundo:
    print("La hora dentro de un segundo será",hora,minuto,Seg)
elif Min<Minuto and Seg<Segundo:
    print("La hora dentro de un segundo será",hora,minuto,Seg)